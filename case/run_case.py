# coding=utf-8

import os
import unittest


class RunCase(unittest.TestCase):
    """管控所有Case"""

    @staticmethod
    def test_case01():
        case_path = os.path.join(os.getcwd(), "")
        print(case_path)
        udd = unittest.defaultTestLoader.discover(case_path, "unittest_*.py")
        unittest.TextTestRunner().run(udd)


if __name__ == '__main__':
    unittest.main()
