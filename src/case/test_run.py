#-*-coding:utf-8-*-

import unittest
import ddt
from ExcelUtil import ExcelUtil

excel = ExcelUtil('case.xlsx', 'Sheet1')


@ddt.ddt
class DataTest(unittest.TestCase):

    @ddt.data(*excel.next())
    def testLogin(self, data):
        print(data['name'])
        print(data['password'])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
