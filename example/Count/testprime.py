#coding=utf-8
import unittest
import numbers
class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_case(self):
        self.prime = numbers.is_prime(5)
        self.assertTrue(self.prime,msg="Is not prime!")
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()