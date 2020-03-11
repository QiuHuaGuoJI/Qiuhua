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
    def test_caseA() :
        print("测试用例A")

    @unittest.skip("跳过此条")
    def test_caseB(self):
        print("测试用例B")

    @staticmethod
    def test_caseC():
        print("测试用例C")

    @staticmethod
    def test_caseD():
        print("测试用例D")


if __name__ == '__main__':
    # fut=FistUTest()
    # unittest.main()
    t_u = unittest.TestSuite()
    t_u.addTest(FistUTest('test_caseC'))
    # t_u.addTest(FistUTest('test_case01'))
    # t_u.addTest(FistUTest('test_case02'))
    # t_u.addTest(FistUTest('test_case04'))

    unittest.TextTestRunner().run(t_u)
