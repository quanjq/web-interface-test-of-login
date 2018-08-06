# -*-encoding:utf-8 -*-
import logging
#不要在basicConfig前面添加 创建logger的方法，不然会失效
#basicConfig是配置信息，配置日志的级别，不过这个含糊，logger要是和handler不一样的话，这个就没办法区分，需要后面自己设置区分
logging.basicConfig(level=logging.DEBUG,
                    #filename='new.log',
                    #filemode='a',
                    format= '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__) #以当前模块名称创建
logger.setLevel(logging.WARNING) #将INFO级别级以上的捕捉，可以覆盖basicConfig中logger的level设置
# create a file handler
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.DEBUG) #将logger中DEBUG级别级以上的输出到终端，不能覆盖 basicConfig中handle的level设置
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

logger.info('Hello info') #logger中有这部分的信息，handler将其输出
logger.debug('Hello debug') #logger中有这部分的信息，handler没办法输出
logger.warn('Hello warning') #logger中有这部分的信息，handler没办法输出
logger.error('Hello error') #logger中有这部分的信息，handler没办法输出