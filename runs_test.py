# -*-encoding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
#import test_case.get_event_list_interface_test

##这是用 addtest添加测试需要执行的案例放入测试套
#suite = unittest.TestSuite()
#suite.addTest(test_case.get_event_list_interface_test.GetEventListTest('test_get_event_list_eid_success'))
#suite.addTest(test_case.get_event_list_interface_test.GetEventListTest('test_get_event_list_eid_bull'))

### 这个利用 discover的用法添加测试需要执行的案例放入测试套
discover_dir = './test_case'
discover = unittest.defaultTestLoader.discover(discover_dir, pattern='*test.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #runner.run(suite)
    #now = time.strftime('%Y-%m-%d %H_%M_%S')
    #reportfilename = './report/' + now +'_result.html'
    #fp = file(reportfilename, 'wb')
    #runner =HTMLTestRunner(stream=fp,title='guest manage system interface test report',description='implentation example with:')

    runner.run(discover)
   # fp.close()


