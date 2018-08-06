# -*-encoding:utf-8 -*-

import unittest
import requests

class AddEventTest(unittest.TestCase):
    def setUp(self):
        baseurl ='http://127.0.0.1:8000/api/'
        addeventpath = 'add_event/'
        self.addeventurl =baseurl+addeventpath
    def tearDown(self):
        print(self.result)

    def htest_addevent_success(self):
        '''成功添加发布会'''
        param ={'eid':36,'name':u'华为86发布会','limit':50,'address':u'深圳龙岗','start_time':'2018-08-01 10:00:00'}
        r = requests.post(self.addeventurl,data= param)
        self.result =r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'add event success!')
    def test_addevent_exict(self):
        '''添加重复的id'''
        param ={'eid':31,'name':u'华为8发布会','limit':50,'address':u'深圳龙岗','start_time':'2018-08-01 10:00:00'}
        r = requests.post(self.addeventurl,data= param)
        self.result =r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'event id already')
    def test_addevent_id_isnull(self):
        param ={'name':u'华为8发布会','limit':50,'address':u'深圳龙岗','start_time':'2018-08-01 10:00:00'}
        r = requests.post(self.addeventurl,data= param)
        self.result =r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter is error')
    if __name__ == '__main__' :
        unittest.main()


