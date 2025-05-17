#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QQ邮箱IMAP连接测试脚本 - 专门测试"QQMail XMIMAP4Server ready"响应问题
"""

import imaplib
import time
import os
import sys
sys.path.append('d:/CursorPro修改自动登录/github/xf-cursor-auto')

from dotenv import load_dotenv
import logging
import email
import re

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class QQMailTestScript:
    def __init__(self):
        print(f"当前工作目录: {os.getcwd()}")
        print(f"当前脚本文件: {__file__}")
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
        print(f".env绝对路径: {env_path}")
        # 加载环境变量
        self.load_env()
        
        # 获取配置
        self.imap_server = os.getenv('IMAP_SERVER', 'imap.qq.com')
        self.imap_port = int(os.getenv('IMAP_PORT', '993'))
        self.imap_user = os.getenv('IMAP_USER', '')
        self.imap_pass = os.getenv('IMAP_PASS', '')
        self.imap_dir = os.getenv('IMAP_DIR', 'INBOX')
                # 测试邮箱
        self.account = "joseph638@cqfg.fun"
        
        # 验证配置
        self.validate_config()
    
    def load_env(self):
        """加载.env文件中的环境变量"""
        # 查找上级目录（即xf-cursor-auto目录）下的.env
        dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
        print(f"[DEBUG] 实际查找的.env路径: {dotenv_path}")
        if os.path.exists(dotenv_path):
            logging.info("加载环境变量...")
            load_dotenv(dotenv_path)
            logging.info("环境变量加载成功")
        else:
            logging.warning(".env文件不存在，将使用默认配置或手动输入")
            
            # 如果没有.env文件，手动输入配置
            if not os.getenv('IMAP_USER'):
                self.prompt_for_config()
    
    def prompt_for_config(self):
        """手动输入邮箱配置"""
        print("\n=== 请输入QQ邮箱配置 ===")
        imap_user = input("QQ邮箱地址: ")
        imap_pass = input("QQ邮箱授权码: ")
        
        # 设置环境变量
        os.environ['IMAP_SERVER'] = 'imap.qq.com'
        os.environ['IMAP_PORT'] = '993'
        os.environ['IMAP_USER'] = imap_user
        os.environ['IMAP_PASS'] = imap_pass
        os.environ['IMAP_DIR'] = 'INBOX'
    
    def validate_config(self):
        """验证配置是否完整"""
        if not self.imap_user or not self.imap_pass:
            logging.error("邮箱配置不完整，请检查.env文件或手动输入配置")
            sys.exit(1)
        
        logging.info(f"使用邮箱: {self.imap_user}")
        logging.info(f"IMAP服务器: {self.imap_server}:{self.imap_port}")
    
    def test_imap_connection(self, retry=0, max_retries=5):
        """测试IMAP连接，包含重试机制和特殊响应处理"""
        if retry > 0:
            time.sleep(2)
            logging.info(f"重试连接({retry}/{max_retries})...")
        
        if retry >= max_retries:
            logging.error("已达到最大重试次数，连接失败")
            return False
        
        mail = None
        try:
            # 第一步：创建SSL连接
            logging.info("尝试创建IMAP SSL连接...")
            mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            logging.info("SSL连接创建成功")
            
            # 第二步：登录
            logging.info("尝试登录...")
            mail.login(self.imap_user, self.imap_pass)
            logging.info("登录成功")
            
            # 第三步：选择邮箱
            logging.info(f"选择邮箱目录: {self.imap_dir}")
            status, messages = mail.select(self.imap_dir)
            
            if status != 'OK':
                logging.error(f"选择邮箱失败: {status}")
                return False
            
            logging.info("邮箱选择成功")
            
            # 第四步：搜索邮件（简单测试）
            logging.info("尝试搜索最新10封邮件...")
            status, messages = mail.search(None, 'TO', '"msbwbeim389819@cqfg.fun"')
            
            if status != 'OK':
                logging.error(f"搜索邮件失败: {status}")
                return False
            
            mail_ids = messages[0].split()
            mail_count = len(mail_ids)
            logging.info(f"邮箱中共有 {mail_count} 封邮件")
            
            # 展示最新的几封邮件的主题
            if mail_count > 0:
                logging.info("获取最新邮件主题...")
                latest_ids = mail_ids[-min(5, mail_count):]
                
                for mail_id in reversed(latest_ids):
                    status, msg_data = mail.fetch(mail_id, '(RFC822)')
                    if status != 'OK':
                        continue
                    raw_email = msg_data[0][1]
                    email_message = email.message_from_bytes(raw_email)
                    body = self._extract_imap_body(email_message)
                    if body:
                        # 避免 6 位数字的域名被误识别成验证码
                        body = body.replace(self.account, '')
                        code_match = re.search(r"\b\d{6}\b", body)
                        if code_match:
                            code = code_match.group()
                            logging.info(f"邮件ID {mail_id.decode()} 的验证码: {code}")
                        else:
                            logging.info(f"邮件ID {mail_id.decode()} 未找到验证码")



            # 清理工作
            logging.info("关闭连接...")
            mail.close()
            mail.logout()
            logging.info("连接已关闭")
            
            return True
            
        except Exception as e:
            error_str = str(e)
            logging.error(f"连接过程中发生错误: {error_str}")
            
            # 特殊处理QQ邮箱的响应
            if "QQMail XMIMAP4Server ready" in error_str:
                logging.info("检测到QQ邮箱服务器欢迎信息，这不是真正的错误，将继续尝试...")
                return self.test_imap_connection(retry=retry + 1, max_retries=max_retries)
            
            # 其他错误可能需要特殊处理
            if "authentication failed" in error_str.lower():
                logging.error("认证失败，请检查邮箱地址和授权码是否正确")
                return False
                
            # 一般错误重试
            logging.info("将在2秒后重试...")
            return self.test_imap_connection(retry=retry + 1, max_retries=max_retries)
            
        finally:
            # 确保连接被关闭
            if mail:
                try:
                    mail.close()
                    mail.logout()
                except:
                    pass


    def _extract_imap_body(self, email_message):
        # 提取邮件正文
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    charset = part.get_content_charset() or 'utf-8'
                    try:
                        body = part.get_payload(decode=True).decode(charset, errors='ignore')
                        return body
                    except Exception as e:
                        logging.error(f"解码邮件正文失败: {e}")
        else:
            content_type = email_message.get_content_type()
            if content_type == "text/plain":
                charset = email_message.get_content_charset() or 'utf-8'
                try:
                    body = email_message.get_payload(decode=True).decode(charset, errors='ignore')
                    return body
                except Exception as e:
                    logging.error(f"解码邮件正文失败: {e}")
        return ""





    def run_modified_version(self):
        """运行修改后的EmailVerificationHandler版本（直接内嵌）"""
        class ModifiedEmailHandler:
            def __init__(self, account, imap_config):
                self.account = account
                self.imap = imap_config
            
            def get_mail_code(self, retry=0, max_retries=5):
                """测试获取邮件验证码的核心逻辑"""
                if retry > 0:
                    time.sleep(2)
                    logging.info(f"重试获取验证码({retry}/{max_retries})...")
                
                if retry >= max_retries:
                    logging.error("已达到最大重试次数，获取验证码失败")
                    return None
                
                mail = None
                try:
                    # 连接到IMAP服务器
                    logging.info("尝试连接IMAP服务器...")
                    mail = imaplib.IMAP4_SSL(self.imap['imap_server'], self.imap['imap_port'])
                    logging.info("IMAP SSL连接成功")
                    
                    logging.info("尝试登录...")
                    mail.login(self.imap['imap_user'], self.imap['imap_pass'])
                    logging.info("登录成功")
                    
                    logging.info(f"选择邮箱: {self.imap['imap_dir']}")
                    mail.select(self.imap['imap_dir'])
                    
                    # 搜索邮件
                    logging.info(f"搜索发送给 {self.account} 的邮件...")
                    status, messages = mail.search(None, 'TO', f'"{self.account}"')
                    
                    if status != 'OK':
                        logging.error(f"搜索邮件失败: {status}")
                        return None
                    
                    mail_ids = messages[0].split()
                    mail_count = len(mail_ids)
                    logging.info(f"找到 {mail_count} 封相关邮件")
                    
                    # 获取邮件内容并查找验证码
                    if mail_count > 0:
                        for mail_id in reversed(mail_ids):
                            status, msg_data = mail.fetch(mail_id, '(RFC822)')
                            if status == 'OK':
                                logging.info(f"成功获取邮件ID {mail_id.decode()}")
                                raw_email = msg_data[0][1]
                                email_message = email.message_from_bytes(raw_email)
                                # 解析正文
                                body = ""
                                if email_message.is_multipart():
                                    for part in email_message.walk():
                                        content_type = part.get_content_type()
                                        content_disposition = str(part.get("Content-Disposition"))
                                        if content_type == "text/plain" and "attachment" not in content_disposition:
                                            charset = part.get_content_charset() or 'utf-8'
                                            try:
                                                body = part.get_payload(decode=True).decode(charset, errors='ignore')
                                                break
                                            except Exception as e:
                                                logging.error(f"解码邮件正文失败: {e}")
                                else:
                                    content_type = email_message.get_content_type()
                                    if content_type == "text/plain":
                                        charset = email_message.get_content_charset() or 'utf-8'
                                        try:
                                            body = email_message.get_payload(decode=True).decode(charset, errors='ignore')
                                        except Exception as e:
                                            logging.error(f"解码邮件正文失败: {e}")
                                # 查找6位验证码
                                code_match = re.search(r"\\b\\d{6}\\b", body)
                                if code_match:
                                    code = code_match.group()
                                    logging.info(f"邮件ID {mail_id.decode()} 的验证码: {code}")
                                else:
                                    logging.info(f"邮件ID {mail_id.decode()} 未找到验证码")
                    
                    mail.close()
                    mail.logout()
                    return "测试成功"
                    
                except Exception as e:
                    error_str = str(e)
                    
                    # 重点：处理QQ邮箱的特殊响应
                    if "QQMail XMIMAP4Server ready" in error_str:
                        logging.info("检测到QQ邮箱服务器欢迎信息，这是正常情况，将继续操作...")
                        return self.get_mail_code(retry=retry + 1, max_retries=max_retries)
                    else:
                        logging.error(f"获取邮件验证码时发生错误: {error_str}")
                        return None
                        
                finally:
                    if mail:
                        try:
                            mail.close()
                            mail.logout()
                        except:
                            pass
        
        # 创建配置
        imap_config = {
            'imap_server': self.imap_server,
            'imap_port': self.imap_port,
            'imap_user': self.imap_user,
            'imap_pass': self.imap_pass,
            'imap_dir': self.imap_dir
        }
        

        
        logging.info("\n=== 测试修改后的邮件验证码处理器 ===")
        handler = ModifiedEmailHandler(test_account, imap_config)
        result = handler.get_mail_code()
        
        if result:
            logging.info("修改后的验证码处理器测试成功！")
        else:
            logging.error("修改后的验证码处理器测试失败")

def main():
    print("=" * 50)
    print("QQ邮箱IMAP连接测试脚本 - 测试'QQMail XMIMAP4Server ready'问题")
    print("=" * 50)
    
    tester = QQMailTestScript()
    
    # 测试基本连接
    print("\n=== 测试1: 基本IMAP连接 ===")
    if tester.test_imap_connection():
        print("\n✅ 基本IMAP连接测试成功！")
    else:
        print("\n❌ 基本IMAP连接测试失败！")
    
    # 测试修改后的处理方式
    print("\n=== 测试2: 修改后的验证码获取处理 ===")
    tester.run_modified_version()
    
    print("\n" + "=" * 50)
    print("测试完成")
    print("=" * 50)

if __name__ == "__main__":
    main()