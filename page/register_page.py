# codeing=utf-8
from base.register_base import FindElement


class RegisterPage:
    """获取页面元素"""

    def __init__(self, driver, path):
        self.find_e = FindElement(driver)
        self.path = path

    def get_email_element(self):
        return self.find_e.get_element("user_email", self.path)
        pass

    def get_username_element(self):
        return self.find_e.get_element("user_name", self.path)

    def get_password_element(self):
        return self.find_e.get_element("password", self.path)

    def get_vcode_element(self):
        return self.find_e.get_element("code_text", self.path)

    def get_resister_button(self):
        return self.find_e.get_element("register_btn", self.path)

    def get_email_element_error(self):
        return self.find_e.get_element("register_email_error", self.path)

    def get_username_element_error(self):
        return self.find_e.get_element("register_nickname_error", self.path)

    def get_password_element_error(self):
        return self.find_e.get_element("register_password_error", self.path)

    def get_vcode_element_error(self):
        return self.find_e.get_element("captcha_code_error", self.path)
