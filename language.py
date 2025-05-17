import os

class Language:
    def __init__(self):
        self.current_language = "cn"  # Default language is Chinese
        self.translations = {
            "cn": {
                # System messages
                "error": "❌",
                "warning": "⚠️",
                "info": "ℹ️",
                
                # Main program flow messages
                "initializing_program": "\n=== 初始化程序 ===",
                "select_operation_mode": "\n请选择操作模式:",
                "reset_machine_code_only": "1. 仅重置机器码",
                "complete_registration": "2. 完整注册流程",
                "only_sign_up": "3. 仅注册",
                "disable_auto_update": "4. 禁止自动升级",
                "select_saved_account": "5. 选择已保存账号并应用",
                "enter_option": "请输入选项: ",
                "invalid_option": "无效的选项,请重新输入",
                "enter_valid_number": "请输入有效的数字",
                "machine_code_reset_complete": "机器码重置完成",
                "initializing_browser": "正在初始化浏览器...",
                "get_user_agent_failed": "获取user agent失败，使用默认值",
                "configuration_info": "\n=== 配置信息 ===",
                "generating_random_account": "正在生成随机账号信息...",
                "generated_email_account": "生成的邮箱账号: {email}",
                "initializing_email_verification": "正在初始化邮箱验证模块...",
                "starting_registration": "\n=== 开始注册流程 ===",
                "visiting_login_page": "正在访问登录页面: {url}",
                "getting_session_token": "正在获取会话令牌...",
                "updating_auth_info": "更新认证信息...",
                "resetting_machine_code": "重置机器码...",
                "all_operations_completed": "所有操作已完成",
                "session_token_failed": "获取会话令牌失败，注册流程未完成",
                "program_error": "程序执行出现错误: {error}",
                
                # Turnstile verification messages
                "detecting_turnstile": "正在检测 Turnstile 验证...",
                "verification_success": "验证成功 - 已到达{status}页面",
                "retry_verification": "第 {count} 次尝试验证",
                "detected_turnstile": "检测到 Turnstile 验证框，开始处理...",
                "turnstile_verification_passed": "Turnstile 验证通过",
                "verification_failed_max_retries": "验证失败 - 已达到最大重试次数 {max_retries}",
                "turnstile_exception": "Turnstile 验证过程发生异常: {error}",
                
                # Cookie and session messages
                "getting_cookie": "开始获取cookie",
                "cookie_attempt_failed": "第 {attempts} 次尝试未获取到CursorSessionToken，{retry_interval}秒后重试...",
                "cookie_max_attempts": "已达到最大尝试次数({max_attempts})，获取CursorSessionToken失败",
                "cookie_failure": "获取cookie失败: {error}",
                "retry_in_seconds": "将在 {seconds} 秒后重试...",
                
                # Account registration messages
                "start_account_registration": "=== 开始注册账号流程 ===",
                "visiting_registration_page": "正在访问注册页面: {url}",
                "filling_personal_info": "正在填写个人信息...",
                "input_first_name": "已输入名字: {name}",
                "input_last_name": "已输入姓氏: {name}",
                "input_email": "已输入邮箱: {email}",
                "submitting_personal_info": "提交个人信息...",
                "registration_page_access_failed": "注册页面访问失败: {error}",
                "setting_password": "正在设置密码...",
                "submitting_password": "提交密码...",
                "password_setup_complete": "密码设置完成，等待系统响应...",
                "password_setup_failed": "密码设置失败: {error}",
                "registration_failed_email_used": "注册失败：邮箱已被使用",
                "registration_success": "注册成功 - 已进入账户设置页面",
                "getting_email_verification": "正在获取邮箱验证码...",
                "verification_code_failure": "获取验证码失败",
                "verification_code_success": "成功获取验证码: {code}",
                "inputting_verification_code": "正在输入验证码...",
                "verification_code_input_complete": "验证码输入完成",
                "verification_code_process_error": "验证码处理过程出错: {error}",
                "waiting_system_processing": "等待系统处理中... 剩余 {seconds} 秒",
                "getting_account_info": "正在获取账户信息...",
                "account_usage_limit": "账户可用额度上限: {limit}",
                "registration_complete": "\n=== 注册完成 ===",
                "cursor_account_info": "Cursor 账号信息:\n邮箱: {email}\n密码: {password}",
                
                # Config related messages
                "imap_server": "IMAP服务器: {server}",
                "imap_port": "IMAP端口: {port}",
                "imap_username": "IMAP用户名: {username}",
                "imap_password": "IMAP密码: {password}",
                "imap_inbox_dir": "IMAP收件箱目录: {dir}",
                "temp_mail": "临时邮箱: {mail}",
                "domain": "域名: {domain}",
                
                # End messages
                "end_message": "=" * 30 + "\n所有操作已完成\n\n=== 获取更多信息 ===\n📺 B站UP主: 想回家的前端\n🔥 公众号: code 未来\n" + "=" * 30,
                
                # Error messages
                "file_not_exists": "文件 {path} 不存在",
                "domain_not_configured": "域名未配置，请在 .env 文件中设置 DOMAIN",
                "temp_mail_not_configured": "临时邮箱未配置，请在 .env 文件中设置 TEMP_MAIL",
                "imap_server_not_configured": "IMAP服务器未配置，请在 .env 文件中设置 IMAP_SERVER",
                "imap_port_not_configured": "IMAP端口未配置，请在 .env 文件中设置 IMAP_PORT",
                "imap_user_not_configured": "IMAP用户名未配置，请在 .env 文件中设置 IMAP_USER",
                "imap_pass_not_configured": "IMAP密码未配置，请在 .env 文件中设置 IMAP_PASS",
                "imap_dir_invalid": "IMAP收件箱目录配置无效，请在 .env 文件中正确设置 IMAP_DIR",
                
                # Language selection
                "select_language": "请选择语言 / Please select language:",
                "chinese": "1. 中文",
                "english": "2. English",
                "language_selected": "已选择中文作为系统语言",
                
                # System info
                "current_operating_system": "当前操作系统: {system}",
                "executing_macos_command": "执行macOS命令",
                "executing_linux_command": "执行Linux命令",
                "executing_windows_command": "执行Windows命令",
                "unsupported_operating_system": "不支持的操作系统: {system}",
                
                # Logging
                "logger_initialized": "日志系统初始化，日志目录: {dir}",
                "open_source_prefix": "[开源项目：https://github.com/wangffei/wf-cursor-auto-free.git] {msg}",
                "account_usage_info_failure": "获取账户额度信息失败: {error}",
                "env_variables_loaded": "环境变量加载成功！",
                "error_prefix": "错误: {error}",
                
                # Exit message
                "program_exit_message": "\n程序执行完毕，按回车键退出...",
                
                # File warnings
                "names_file_not_found": "未找到names-dataset.txt文件!",
                
                # Account saving
                "saving_account_info": "正在保存账号信息...",
                "account_saved_successfully": "账号信息已成功保存到 {path}",
                "account_save_failed": "账号信息保存失败: {error}",
                "account_info_saved": "账号信息已成功保存",
                "failed_to_save_account_info": "保存账号信息失败",
                
                # Disable auto update
                "cursor_dir_not_found": "Neither Cursor nor cursor directory found in {dir}",
                "also_checked_dir": "Also checked {dir}",
                "cursor_install_reminder": "Please make sure Cursor is installed and has been run at least once",
                "storage_dir_not_found": "Storage directory not found: {dir}",
                "storage_file_found": "Storage file found: {path}",
                "file_size": "File size: {size} bytes",
                "file_permissions": "File permissions: {permissions}",
                "file_owner": "File owner: {owner}",
                "file_group": "File group: {group}",
                "file_stats_error": "Error getting file stats: {error}",
                "permission_denied": "Permission denied: {path}",
                "try_chown": "Try running: chown {user}:{user} {path}",
                "try_chmod": "And: chmod 644 {path}",
                "storage_file_empty": "Storage file is empty: {path}",
                "file_corrupted": "The file might be corrupted, please reinstall Cursor",
                "storage_file_valid": "Storage file is valid and contains data",
                "storage_file_read_error": "Error reading storage file: {error}",
                "file_corrupted_reinstall": "The file might be corrupted. Please reinstall Cursor",
                "storage_file_not_found": "Storage file not found: {path}",
                "linux_paths_error": "Error checking Linux paths: {error}",
                "file_modified": "File modified successfully",
                "file_modify_failed": "Failed to modify file: {error}",
                "terminating_cursor_processes": "Terminating Cursor processes",
                "cursor_processes_terminated": "Cursor processes terminated successfully",
                "process_termination_failed": "Failed to terminate processes: {error}",
                "unsupported_os": "Unsupported operating system",
                "removing_updater_directory": "Removing updater directory...",
                "updater_directory_removed": "Updater directory removed",
                "updater_directory_locked": "Updater directory is locked, skipping removal: {path}",
                "directory_removal_failed": "Failed to remove directory: {error}",
                "clearing_update_config": "Clearing update configuration file...",
                "update_config_cleared": "Update configuration file cleared",
                "update_config_locked": "Update configuration file is locked, skipping clearing",
                "update_config_not_exist": "Update configuration file does not exist",
                "clear_config_failed": "Failed to clear update configuration file: {error}",
                "unsupported_os_with_name": "Unsupported operating system: {system}",
                "creating_blocking_files": "Creating blocking files...",
                "blocking_file_created": "Blocking file created: {path}",
                "blocking_file_locked": "Blocking file is locked, skipping creation",
                "update_config_content": "# This file is locked to prevent auto-updates\nversion: 0.0.0\n",
                "update_config_locked_success": "Update configuration file locked: {path}",
                "update_config_already_locked": "Update configuration file is already locked, skipping modification",
                "create_blocking_file_failed": "Failed to create blocking file: {error}",
                "starting_disable_update": "Starting to disable auto update...",
                "auto_update_disabled": "Auto update successfully disabled",
                "disable_update_failed": "Failed to disable auto update: {error}",
                "disable_cursor_auto_update_title": "Disable Cursor Auto Update",
                "press_enter_continue": "Press Enter to continue...",
                
                # Accounts management
                "accounts_dir_not_found": "账号目录 {dir} 不存在",
                "no_account_files_found": "在 {dir} 目录中未找到账号文件",
                "saved_accounts_title": "\n=== 已保存的账号 ===",
                "account_created_time": "创建时间",
                "reading_error": "读取错误",
                "return_to_main_menu": "返回上级菜单",
                "select_account_number": "请选择要应用的账号编号",
                "invalid_selection": "无效的选择，请重新输入",
                "please_enter_number": "请输入数字",
                "loading_account_info": "正在从 {path} 加载账号信息",
                "using_account": "使用账号: {email}",
                "incomplete_account_info": "账号信息不完整，缺少必要字段",
                "apply_account_failed": "应用账号信息失败",
                "apply_account_error": "应用账号时出错: {error}",
                
                # GUI related messages
                "closing_browser": "正在关闭浏览器...",
                "browser_closed": "浏览器已关闭",
                "polling_login_result": "正在轮询登录结果...",
                "login_successful": "登录成功！",
                "waiting_for_code": "等待验证码中...",
                "code_received": "已接收到验证码！",
                "applying_settings": "正在应用设置...",
                "settings_applied": "设置已应用",
                "initializing_ui": "正在初始化界面...",
                "ui_ready": "界面已就绪",
                "processing_request": "正在处理请求...",
                "request_completed": "请求已完成",
                "connection_failed": "连接失败",
                "retrying_connection": "正在重新连接...",
                "login_not_completed": "登录还未完成，请稍等..."
            },
            "en": {
                # System messages
                "error": "❌",
                "warning": "⚠️",
                "info": "ℹ️",
                
                # Main program flow messages
                "initializing_program": "\n=== Initializing Program ===",
                "select_operation_mode": "\nPlease select operation mode:",
                "reset_machine_code_only": "1. Reset machine code only",
                "complete_registration": "2. Complete registration process",
                "only_sign_up": "3. Sign up only",
                "disable_auto_update": "4. Disable auto update",
                "select_saved_account": "5. Select and apply saved account",
                "enter_option": "Please enter option (1 or 2): ",
                "invalid_option": "Invalid option, please enter again",
                "enter_valid_number": "Please enter a valid number",
                "machine_code_reset_complete": "Machine code reset complete",
                "initializing_browser": "Initializing browser...",
                "get_user_agent_failed": "Failed to get user agent, using default value",
                "configuration_info": "\n=== Configuration Info ===",
                "generating_random_account": "Generating random account information...",
                "generated_email_account": "Generated email account: {email}",
                "initializing_email_verification": "Initializing email verification module...",
                "starting_registration": "\n=== Starting Registration Process ===",
                "visiting_login_page": "Visiting login page: {url}",
                "getting_session_token": "Getting session token...",
                "updating_auth_info": "Updating authentication information...",
                "resetting_machine_code": "Resetting machine code...",
                "all_operations_completed": "All operations completed",
                "session_token_failed": "Failed to get session token, registration process incomplete",
                "program_error": "Program execution error: {error}",
                
                # Turnstile verification messages
                "detecting_turnstile": "Detecting Turnstile verification...",
                "verification_success": "Verification successful - Reached {status} page",
                "retry_verification": "Attempt {count} of verification",
                "detected_turnstile": "Detected Turnstile verification box, starting processing...",
                "turnstile_verification_passed": "Turnstile verification passed",
                "verification_failed_max_retries": "Verification failed - Reached maximum retry count {max_retries}",
                "turnstile_exception": "Turnstile verification process exception: {error}",
                
                # Cookie and session messages
                "getting_cookie": "Starting to get cookies",
                "cookie_attempt_failed": "Attempt {attempts} failed to get CursorSessionToken, retrying in {retry_interval} seconds...",
                "cookie_max_attempts": "Reached maximum attempts ({max_attempts}), failed to get CursorSessionToken",
                "cookie_failure": "Failed to get cookie: {error}",
                "retry_in_seconds": "Will retry in {seconds} seconds...",
                
                # Account registration messages
                "start_account_registration": "=== Starting Account Registration Process ===",
                "visiting_registration_page": "Visiting registration page: {url}",
                "filling_personal_info": "Filling personal information...",
                "input_first_name": "Input first name: {name}",
                "input_last_name": "Input last name: {name}",
                "input_email": "Input email: {email}",
                "submitting_personal_info": "Submitting personal information...",
                "registration_page_access_failed": "Registration page access failed: {error}",
                "setting_password": "Setting password...",
                "submitting_password": "Submitting password...",
                "password_setup_complete": "Password setup complete, waiting for system response...",
                "password_setup_failed": "Password setup failed: {error}",
                "registration_failed_email_used": "Registration failed: Email already in use",
                "registration_success": "Registration successful - Entered account settings page",
                "getting_email_verification": "Getting email verification code...",
                "verification_code_failure": "Failed to get verification code",
                "verification_code_success": "Successfully got verification code: {code}",
                "inputting_verification_code": "Inputting verification code...",
                "verification_code_input_complete": "Verification code input complete",
                "verification_code_process_error": "Verification code process error: {error}",
                "waiting_system_processing": "Waiting for system processing... {seconds} seconds remaining",
                "getting_account_info": "Getting account information...",
                "account_usage_limit": "Account usage limit: {limit}",
                "registration_complete": "\n=== Registration Complete ===",
                "cursor_account_info": "Cursor account information:\nEmail: {email}\nPassword: {password}",
                
                # Config related messages
                "imap_server": "IMAP server: {server}",
                "imap_port": "IMAP port: {port}",
                "imap_username": "IMAP username: {username}",
                "imap_password": "IMAP password: {password}",
                "imap_inbox_dir": "IMAP inbox directory: {dir}",
                "temp_mail": "Temporary email: {mail}",
                "domain": "Domain: {domain}",
                
                # End messages
                "end_message": "=" * 30 + "\nAll operations completed\n\n=== Get More Information ===\n📺 Bilibili UP: 想回家的前端\n🔥 WeChat: code 未来\n" + "=" * 30,
                
                # Error messages
                "file_not_exists": "File {path} does not exist",
                "domain_not_configured": "Domain not configured, please set DOMAIN in .env file",
                "temp_mail_not_configured": "Temporary email not configured, please set TEMP_MAIL in .env file",
                "imap_server_not_configured": "IMAP server not configured, please set IMAP_SERVER in .env file",
                "imap_port_not_configured": "IMAP port not configured, please set IMAP_PORT in .env file",
                "imap_user_not_configured": "IMAP username not configured, please set IMAP_USER in .env file",
                "imap_pass_not_configured": "IMAP password not configured, please set IMAP_PASS in .env file",
                "imap_dir_invalid": "IMAP inbox directory configuration invalid, please set IMAP_DIR correctly in .env file",
                
                # Language selection
                "select_language": "请选择语言 / Please select language:",
                "chinese": "1. 中文",
                "english": "2. English",
                "language_selected": "English has been selected as the system language",
                
                # System info
                "current_operating_system": "Current operating system: {system}",
                "executing_macos_command": "Executing macOS command",
                "executing_linux_command": "Executing Linux command",
                "executing_windows_command": "Executing Windows command",
                "unsupported_operating_system": "Unsupported operating system: {system}",
                
                # Logging
                "logger_initialized": "Logger initialized, log directory: {dir}",
                "open_source_prefix": "[Open source project: https://github.com/wangffei/wf-cursor-auto-free.git] {msg}",
                "account_usage_info_failure": "Failed to get account usage information: {error}",
                "env_variables_loaded": "Environment variables loaded successfully!",
                "error_prefix": "Error: {error}",
                
                # Exit message
                "program_exit_message": "\nProgram execution completed, press Enter to exit...",
                
                # File warnings
                "names_file_not_found": "names-dataset.txt file not found!",
                
                # Account saving
                "saving_account_info": "Saving account information...",
                "account_saved_successfully": "Account information successfully saved to {path}",
                "account_save_failed": "Failed to save account information: {error}",
                "account_info_saved": "Account information saved successfully",
                "failed_to_save_account_info": "Failed to save account information",
                
                # Disable auto update
                "cursor_dir_not_found": "Neither Cursor nor cursor directory found in {dir}",
                "also_checked_dir": "Also checked {dir}",
                "cursor_install_reminder": "Please make sure Cursor is installed and has been run at least once",
                "storage_dir_not_found": "Storage directory not found: {dir}",
                "storage_file_found": "Storage file found: {path}",
                "file_size": "File size: {size} bytes",
                "file_permissions": "File permissions: {permissions}",
                "file_owner": "File owner: {owner}",
                "file_group": "File group: {group}",
                "file_stats_error": "Error getting file stats: {error}",
                "permission_denied": "Permission denied: {path}",
                "try_chown": "Try running: chown {user}:{user} {path}",
                "try_chmod": "And: chmod 644 {path}",
                "storage_file_empty": "Storage file is empty: {path}",
                "file_corrupted": "The file might be corrupted, please reinstall Cursor",
                "storage_file_valid": "Storage file is valid and contains data",
                "storage_file_read_error": "Error reading storage file: {error}",
                "file_corrupted_reinstall": "The file might be corrupted. Please reinstall Cursor",
                "storage_file_not_found": "Storage file not found: {path}",
                "linux_paths_error": "Error checking Linux paths: {error}",
                "file_modified": "File modified successfully",
                "file_modify_failed": "Failed to modify file: {error}",
                "terminating_cursor_processes": "Terminating Cursor processes",
                "cursor_processes_terminated": "Cursor processes terminated successfully",
                "process_termination_failed": "Failed to terminate processes: {error}",
                "unsupported_os": "Unsupported operating system",
                "removing_updater_directory": "Removing updater directory...",
                "updater_directory_removed": "Updater directory removed",
                "updater_directory_locked": "Updater directory is locked, skipping removal: {path}",
                "directory_removal_failed": "Failed to remove directory: {error}",
                "clearing_update_config": "Clearing update configuration file...",
                "update_config_cleared": "Update configuration file cleared",
                "update_config_locked": "Update configuration file is locked, skipping clearing",
                "update_config_not_exist": "Update configuration file does not exist",
                "clear_config_failed": "Failed to clear update configuration file: {error}",
                "unsupported_os_with_name": "Unsupported operating system: {system}",
                "creating_blocking_files": "Creating blocking files...",
                "blocking_file_created": "Blocking file created: {path}",
                "blocking_file_locked": "Blocking file is locked, skipping creation",
                "update_config_content": "# This file is locked to prevent auto-updates\nversion: 0.0.0\n",
                "update_config_locked_success": "Update configuration file locked: {path}",
                "update_config_already_locked": "Update configuration file is already locked, skipping modification",
                "create_blocking_file_failed": "Failed to create blocking file: {error}",
                "starting_disable_update": "Starting to disable auto update...",
                "auto_update_disabled": "Auto update successfully disabled",
                "disable_update_failed": "Failed to disable auto update: {error}",
                "disable_cursor_auto_update_title": "Disable Cursor Auto Update",
                "press_enter_continue": "Press Enter to continue...",
                
                # Accounts management
                "accounts_dir_not_found": "Accounts directory {dir} does not exist",
                "no_account_files_found": "No account files found in directory {dir}",
                "saved_accounts_title": "\n=== Saved Accounts ===",
                "account_created_time": "Created",
                "reading_error": "Reading error",
                "return_to_main_menu": "Return to main menu",
                "select_account_number": "Please select account number to apply",
                "invalid_selection": "Invalid selection, please try again",
                "please_enter_number": "Please enter a number",
                "loading_account_info": "Loading account information from {path}",
                "using_account": "Using account: {email}",
                "incomplete_account_info": "Incomplete account information, missing required fields",
                "apply_account_failed": "Failed to apply account information",
                "apply_account_error": "Error applying account: {error}",
                
                # GUI related messages
                "closing_browser": "Closing browser...",
                "browser_closed": "Browser closed",
                "polling_login_result": "Polling for login result...",
                "login_successful": "Login successful!",
                "waiting_for_code": "Waiting for verification code...",
                "code_received": "Verification code received!",
                "applying_settings": "Applying settings...",
                "settings_applied": "Settings applied",
                "initializing_ui": "Initializing user interface...",
                "ui_ready": "User interface ready",
                "processing_request": "Processing request...",
                "request_completed": "Request completed",
                "connection_failed": "Connection failed",
                "retrying_connection": "Retrying connection...",
                "login_not_completed": "please wait a minutes"
            }
        }
    
    def set_language(self, language_code):
        """Set the current language"""
        if language_code in self.translations:
            self.current_language = language_code
            return True
        return False
    
    def get(self, key, **kwargs):
        """Get translation for a key with optional format parameters"""
        if key not in self.translations[self.current_language]:
            # Fallback to Chinese if key not found in current language
            if key in self.translations["cn"]:
                text = self.translations["cn"][key]
            else:
                return f"[Missing translation: {key}]"
        else:
            text = self.translations[self.current_language][key]
        
        # Apply format if kwargs are provided
        if kwargs:
            try:
                return text.format(**kwargs)
            except KeyError as e:
                return f"{text} (FORMAT ERROR: {str(e)})"
        return text
    
    def select_language_prompt(self):
        """Display language selection prompt and return selected language code"""
        print(self.translations["cn"]["select_language"])
        print(self.translations["cn"]["chinese"])
        print(self.translations["cn"]["english"])
        
        while True:
            try:
                choice = int(input().strip())
                if choice == 1:
                    self.set_language("cn")
                    print(self.get("language_selected"))
                    return "cn"
                elif choice == 2:
                    self.set_language("en")
                    print(self.get("language_selected"))
                    return "en"
                else:
                    print(self.translations["cn"]["invalid_option"])
            except ValueError:
                print(self.translations["cn"]["enter_valid_number"])

# Global language instance
language = Language()

def get_translation(key, **kwargs):
    """Helper function to get translation"""
    return language.get(key, **kwargs)

# For direct testing
if __name__ == "__main__":
    language.select_language_prompt()
    print(get_translation("initializing_program"))
    print(get_translation("cursor_account_info", email="test@example.com", password="password123")) 