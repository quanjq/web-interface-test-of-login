# -*-encoding:utf-8 -*-

import unittest
import requests

class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url_event_list='http://127.0.0.1:8000/api/get_event_list/'
    def tearDown(self):
        print(self.result)
    def test_get_event_list_eid_success(self):
        '''通过id查询成功'''
        #canshu = {'eid':'8'}
        r = requests.get(self.url_event_list,params={'eid':8})
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')
        self.assertEqual(self.result['date']['name'], 'xiaomi8')
        self.assertEqual(self.result['date']['address'], 'sehnzhen')
        self.assertEqual(self.result['date']['start_time'],'2018-06-30T18:00:00')


    def test_get_event_list_eid_bull(self):
        '''通过id为空查询'''
        #canshu = {'eid':''}
        r = requests.get(self.url_event_list,params={'eid':''})
        self.result = r.json()
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')
    def test_get_event_list_eid_notexict(self):
        '''通过id不存在查询'''
        #canshu = {'eid':'92'}
        r = requests.get(self.url_event_list,params={'eid':92})
        self.result = r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'query is empty')
    def get_event_list_name_notexict(self):
        '''通过name不存在查询'''
        #canshu = {'name':'hdjhgj'}
        r = requests.get(self.url_event_list,params={'name':'hdjhgj'})
        self.result = r.json()
        self.assertEqual(self.result['status'],10022)
        self.assertEqual(self.result['message'],'query is empty')
    def ddddtest_get_event_list_name_success(self):
        '''通过name查询成功'''
       # canshu = {'name':'xiaomi8'}
        r = requests.get(self.url_event_list,params={'name':u'xiaomi8'})
        self.result = r.json()
        self.assertEqual(self.result['status'],200)
        self.assertEqual(self.result['message'],'success')
        self.assertEqual(self.result['date']['name'], u'xiaomi8')
        self.assertEqual(self.result['date']['address'], u'sehnzhen')
    if __name__ == '__main__':
        unittest.main()






