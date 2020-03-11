# coding =utf-8
import time

from selenium import webdriver

from base.register_base import FindElement


class ActionMethod:
    """执行基础操作"""

    def __init__(self):
        """默认为Chrome浏览器"""
        self.driver = None
        # self.driver.get(
        #     "http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/")

    # @staticmethod
    def open_browser(self, browser, tag):
        if tag:
            if browser == "firefox":
                self.driver = webdriver.Firefox()
            elif browser == "ie":
                self.driver = webdriver.Ie()
            elif browser == "edge":
                self.driver = webdriver.Edge()
            elif browser == "chrome":
                self.driver = webdriver.Chrome()
                print("您输入的浏览器名称不正确")
            else:
                print("您输入的浏览器名称不正确")

    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def get_element(self, content):
        find_element = FindElement(self.driver)
        # print("sssssxxxxxx"+content)
        element = find_element.get_element(content)
        # time.sleep(2)
        # print(element)
        return element

    def send_value(self, content, value):
        element = self.get_element(content)
        element.send_keys(value)

    def click_element(self, content, tag):
        if tag:
            self.get_element(content).click()

    @staticmethod
    def sleep_time(t=None):
        # t =
        if t is None:
            t = 3
        time.sleep(int(t))

    def driver_close(self, tag):
        if tag:
            self.driver.close()

    def is_page(self, title):
        page_title = self.driver.title
        if title in page_title:
            return True
        else:
            return False


if __name__ == '__main__':
    am = ActionMethod()
    # am.get_element("user_email")
    am.send_value("user_email", "2222")
