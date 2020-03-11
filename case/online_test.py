import unittest
from ddt import ddt, data

@ddt
class FooTestCase(unittest.TestCase):

    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        print(value)




if __name__ == '__main__':
    unittest.main()