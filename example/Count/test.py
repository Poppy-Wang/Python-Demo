import unittest
from count import Count
class Test(unittest.TestCase):
    def setUp(self):
        self.j=Count(3,4)

    def test_add(self):
        self.add = self.j.add()
        self.assertEqual(self.add, 7)
    def tearDown(self):
        pass
if __name__=='main':
    suite=unittest.TestSuite
    suite.addTest(Test("test_add"))
    runner=unittest.TextTestRunner
    runner.run()