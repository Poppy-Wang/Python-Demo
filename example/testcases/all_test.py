import unittest
import test_baidu
import test_youdao

if __name__=='main':
    suite = unittest.TestSuite()
    suite.addTest(test_baidu.Test_baidu('test_baidu'))
    suite.addTest(test_youdao.Test_youdao('test_youdao'))
    runner=unittest.TextTestRunner()
    runner.run(suite)