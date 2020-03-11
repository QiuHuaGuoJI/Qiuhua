# coding = utf-8
import datetime
import os
import time
import warnings
import HTMLTestRunner
import ddt
import unittest

from selenium import webdriver
from business.register_business import RegisterBusiness
from report.excel_util import ExcelUtil
from test_selenium.identification_v_code import IdentifyVCode


@ddt.ddt
class DdtDataFirst(unittest.TestCase):
    """提供注册所用邮箱、用户名、密码、验证码，以及错误信息定位元素、错误提示信息"""
    ex = ExcelUtil()
    data = ex.get_data()

    @classmethod
    def setUpClass(cls) -> None:
        # cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()

        warnings.simplefilter("ignore", ResourceWarning)

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
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
        time.sleep(5)
        self.driver.close()

    # @ddt.data(
    #     ["2323", "这是新用户名", "11111", "xddsd", "email_error", "请输入有效的的电子邮件地址"],
    #     ["sfds", "这是新用户名", "11111", "xddsd", "email_error", "请输入有效的的电子邮件地址"],
    #     ["2323@qq.com", "这是新用户名", "11111", "xddsd", "email_error", "请输入有效的的电子邮件地址"]
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_login_success(
            self,
            email,
            name,
            password,
            code,
            assertCode,
            assertText):
        login_statue = self.register_b.register_function(
            email, name, password, code, assertCode, assertText)
        self.assertFalse(login_statue, "测试失败")


if __name__ == '__main__':
    # unittest.main()
    #
    report_html_path = "D:/Workspaces/Pworkspace/report/test_report1.html"
    html_f = open(report_html_path, "wb")
    ts = unittest.TestLoader().loadTestsFromTestCase(DdtDataFirst)
    html_runner = HTMLTestRunner.HTMLTestRunner(
        stream=html_f,
        title="this is report1",
        description=u"这是我的第一个测试用例报告1"
    )
    html_runner.run(ts)
    html_f.close()
