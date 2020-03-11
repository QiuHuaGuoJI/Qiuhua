# utf-8
import datetime
import os
import time
import unittest
import warnings

from selenium import webdriver

import HTMLTestRunner
from business.register_business import RegisterBusiness
from log.register_log import RegisterLog
from test_selenium.identification_v_code import IdentifyVCode


class FirstCase(unittest.TestCase):
    """测试用例"""
    #
    r_log = None
    count = 0

    @classmethod
    def setUpClass(cls) -> None:
        # cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()
        warnings.simplefilter("ignore", ResourceWarning)
        cls.r_log = RegisterLog()

        cls.register_log = cls.r_log.get_log()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.r_log.close_log()
        time.sleep(3)

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.register_log.info(
            "this is Chrome")
        self.r_log.output_log()
        self.driver.maximize_window()
        path = "../config/LocalElement.ini"
        i_vcode = IdentifyVCode(self.driver, self._testMethodName, path)
        # self.v_code = i_vcode.get_jj_varify_code("code_image")



        self.register_b = RegisterBusiness(self.driver, path)

    def tearDown(self) -> None:
        curr_time = datetime.datetime.now()
        str_time = str(curr_time.time())
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(
                    "../report/" + case_name + str_time + ".png")
                self.driver.save_screenshot(file_path)
        time.sleep(2)

        self.driver.close()

    def test_login_email_error(self):
        """测试登录错误的情况"""
        email_statue = self.register_b.login_email_error(
            "1111", "mingzhi", "123456", "1234")
        self.assertFalse(email_statue, "邮箱不合法，怎么会登录成功呢！测试失败！")
        # if email_statue is True:
        #     print("很遗憾，邮箱不合法，注册失败了！")
        # elif email_statue is False:
        #     print("邮箱不合法，怎么会登录成功呢！")

    def test_login_nickname_error(self):
        nickname_statue = self.register_b.login_nickname_error(
            "12323@qq.com", "我是名字", "111111", "1234")
        self.assertFalse(nickname_statue, "用户名不合法，怎么会注册成功呢！测试失败！")
        # if nickname_statue is True:
        #     print("很遗憾，用户名不合法，注册失败了！")
        # elif nickname_statue is False:
        #     print("用户名不合法，怎么会注册成功呢！")

    def test_login_password_error(self):
        password_statue = self.register_b.login_password_error(
            "123234@qq.com", "2322", "1", "1234")
        self.assertFalse(password_statue, "用户名不合法，怎么会注册成功呢！测试失败！")
        # if nickname_statue is True:
        #     print("很遗憾，用户名不合法，注册失败了！")
        # elif nickname_statue is False:
        #     print("用户名不合法，怎么会注册成功呢！")

    def test_login_vcode_error(self):
        vcode_statue = self.register_b.login_vcode_error(
            "12345@qq.com", "mingzhi", "123456", "1234")
        self.assertFalse(vcode_statue, "验证码不正确，怎么会注册成功呢！测试失败！")
        # if vcode_statue is True:
        #     print("很遗憾，验证码不正确，注册失败了")
        # elif vcode_statue is False:
        #     print("验证码不正确，怎么会注册成功呢！")

    def test_login_success(self):
        login_statue = self.register_b.login_success(
            "123ww4@qq.com", "mingzhi", "123456", "v_code")
        self.assertFalse(login_statue, "注册失败")

    def test_login_success1(self):
        login_statue = self.register_b.login_success(
            "123ww4@qq.com", "mingzhi", "123456", "v_code")
        self.assertFalse(login_statue, "注册失败")
        # if login_statue is True:
        #     print("注册成功")
        # elif login_statue is False:
        #     print("注册失败")

    # @staticmethod
    # def main():
    #
    #     test_case.test_login_email_error()
    #     test_case.test_login_nickname_error()
    #     test_case.test_login_password_error()
    #     test_case.test_login_vcode_error()


if __name__ == '__main__':
    # unittest.main()
    ts = unittest.TestSuite()
    ts.addTest(FirstCase("test_login_vcode_error"))
    ts.addTest(FirstCase("test_login_success"))
    ts.addTest(FirstCase("test_login_success1"))

    # ts.addTest(FirstCase("test_login_nickname_error"))
    unittest.TextTestRunner().run(ts)

    # report_html_paht = os.path.join(
    #     os.getcwd() + "/report/testcase_report.html")
    # report_html_path = "D:/Workspaces/Pworkspace/report/testcase_report2.html"
    # html_f = open(report_html_path, 'wb')
    # html_runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=html_f, title="this is report2", description="这是我的第一个测试用例报告2")
    # html_runner.run(ts)
