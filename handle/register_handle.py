# utf-8
from page.register_page import RegisterPage


class RegisterHandle:
    """操作页面元素"""

    def __init__(self, driver, path):
        self.page_get = RegisterPage(driver, path)
        # self.path = path

    def send_user_email(self, email):
        """输入email"""
        self.page_get.get_email_element().send_keys(email)
        pass

    def send_user_name(self, user_name):
        """输入name"""
        self.page_get.get_username_element().send_keys(user_name)
        pass

    def send_user_password(self, password):
        """输入password"""
        self.page_get.get_password_element().send_keys(password)
        pass

    def send_user_code(self, v_code):
        """输入code"""
        self.page_get.get_vcode_element().send_keys(v_code)
        pass

    def click_register_button(self):
        self.page_get.get_resister_button().click()

    def get_error_text(self, info, error_info):

        try:
            if info == "email_error":
                # text = self.page_get.get_email_element_error().get_attribute("value")
                text = self.page_get.get_email_element_error().text
            elif info == "nickname_error":
                text = self.page_get.get_username_element_error().text
            elif info == "password_error":
                text = self.page_get.get_password_element_error().text
            elif info == "captcha_code_error":
                text = self.page_get.get_vcode_element_error().text
        except BaseException:
            text = None
        return text

    def get_register_button_text(self):
        return self.page_get.get_resister_button()
