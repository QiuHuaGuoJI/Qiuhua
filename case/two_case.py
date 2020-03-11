# coding = utf-8

import ddt
import unittest


@ddt.ddt
class TwoTest(unittest.TestCase):

    def setUp(self) -> None:
        print("嘿！小女子~")

    def tearDown(self) -> None:
        print("走！回家啊~")

    @ddt.data(["妞儿~", "哎~"], ["小", "娘子~"], ["小", "姐姐~"])
    @ddt.unpack
    def test_test(self, a, b):
        print("别害羞啊~" + a + b)


if __name__ == '__main__':
    unittest.main()
