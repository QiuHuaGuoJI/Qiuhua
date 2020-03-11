
from selenium import webdriver

from test_selenium.find_element import findElement
from util.read_ini import ReadIni


class FindElement():
    """查找元素"""

    def __init__(self, driver):
        self.driver = driver
        self.element = None

    def get_element(self, content, path=None):
        r_i = ReadIni(path)
        element_list = r_i.getVlue(content)
        key = element_list.split(":")[0]
        value = element_list.split(":")[1]
        try:
            if key == "id":
                self.element = self.driver.find_element_by_id(value)
            elif key == "class_name":
                self.element = self.driver.find_element_by_class_name(value)
            elif key == "name":
                self.element = self.driver.find_element_by_nmae(value)
            elif key == "xpath":
                self.element = self.driver.find_element_by_xpath(value)
        except BaseException as e:
            # 用例失败是，截图
            # self.driver.save_screenshot("../image/%s.png" % value)
            print("出现了异常：%s" % e)
            self.element = None
        return self.element


if __name__ == '__main__':

    w_driver = webdriver.Chrome()
    w_driver.get("http://www.5itest.cn/register?goto=http%3A//www.5itest.cn/")
    f = findElement(w_driver)
    # fs="../config/"
    t = f.get_element("user_email", "../config/LocalElement.ini")
    # t.click()

    print(t)
