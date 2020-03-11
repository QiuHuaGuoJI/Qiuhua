# codeing = utf-8

import unittest


class FistUTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("执行所有用例前的初始化")
        print("--------------------")

    @classmethod
    def tearDownClass(cls) -> None:
        print("----------------------")
        print("执行所有用例后的结束操作")

    def setUp(self) -> None:
        print("###########")
        print("这是前置条件")

    def tearDown(self) -> None:
        print("这是后置条件")

    @staticmethod
    def test_case01():
        print("测试用例1")

    @staticmethod
    @unittest.skip("跳过此条")
    def test_case02():
        print("测试用例2")

    @staticmethod
    def test_case03():
        print("测试用例3")

    @staticmethod
    def test_case04():
        print("测试用例4")


if __name__ == '__main__':
    # fut=FistUTest()
    # unittest.main()
    t_u = unittest.TestSuite()
    t_u.addTest(FistUTest('test_case03'))
    t_u.addTest(FistUTest('test_case01'))
    # t_u.addTest(FistUTest('test_case02'))
    # t_u.addTest(FistUTest('test_case04'))

    unittest.TextTestRunner().run(t_u)
