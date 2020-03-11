# utf-8
from handle.register_handle import RegisterHandle


class RegisterBusiness():
    """负责连接case与handle"""

    def __init__(self, driver, path):
        self.register_h = RegisterHandle(driver, path)

    def login_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    def register_function(self, email, name, password, code, assertCode, assertText):
        self.login_base(email, name, password, code)
        if self.register_h.get_error_text(
                assertCode, assertText) is None:
            print("邮箱校验不成功!")
            return True
        else:
            return False

    def login_email_error(self, email, name, password, code):
        """执行 操作"""
        self.login_base(email, name, password, code)
        if self.register_h.get_error_text(
                "email_error", "请输入有效的的电子邮件地址") is None:
            print("邮箱校验不成功!")
            return True
        else:
            return False

    def login_nickname_error(self, email, name, password, code):
        self.login_base(email, name, password, code)
        if self.register_h.get_error_text(
                "nickname_error", "字符长度必须大于等于4，一个中文字算2个字符") is None:
            print("用户名校验不成功!")
            return True
        else:
            return False

    def login_password_error(self, email, name, password, code):
        self.login_base(email, name, password, code)
        if self.register_h.get_error_text(
                "password_error", "最少需要输入 5 个字符") is None:
            print("密码校验不成功!")
            return True
        else:
            return False

    def login_vcode_error(self, email, name, password, code):
        self.login_base(email, name, password, code)
        if self.register_h.get_error_text(
                "captcha_code_error", "验证码错误") is None:
            print("验证码校验不成功!")
            return True
        else:
            return False

    def login_success(self, email, name, password, code):
        self.login_base(email, name, password, code)
        self.register_h.click_register_button()
        if self.register_h.get_register_button_text() is None:
            print("注册成功!")
            return True
        else:
            return False
