import logging
import logging.config


logging.config.fileConfig('log_config.ini')
logger=logging.getLogger('debuglogger')
logger.debug('debug')
logger.warn('Updating records ...')
logger.error('Finish updating records')