# -*-encoding:utf-8 -*-


import logging

#不要在basicConfig前面添加 创建logger的方法，不然会失效
#basicConfig是配置信息，配置日志的级别，不过这个含糊，logger要是和handler不一样的话，这个就没办法区分，需要后面自己设置区分
logging.basicConfig(level=logging.DEBUG,
                    #filename='new.log',
                    #filemode='a',
                    format= '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)

logger.info('Start reading database')
# read database here
records = {'john': 55, 'tom': 66}
logger.debug('Records: %s', records)
logger.warn('Updating records ...')
# update records here
logger.error('Finish updating records')


