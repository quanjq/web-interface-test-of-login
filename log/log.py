# -*-encoding:utf-8 -*-


import logging
import logging.config
#import log_config
logging.config.fileConfig('log_config.ini',disable_existing_loggers=False)

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')


