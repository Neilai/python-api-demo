# -*- coding:utf-8 -*-
import logging
import logging.config

# ************
#logging初级
#配置日志文件，配置时间，配置等级
#************

# logging.basicConfig(filename='logger.log', format='[%(levelname)s] %(asctime)s:%(message)s', datefmt='%Y%m%d %H:%M:%S',level=logging.INFO)
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')

# ************
#logging中级
#配置日志文件，配置时间，配置等级
#利用面向对象的方法
#首先创建一个logger 再创建一个handler  handler可以设置等级和formatter
# 最后调用addhandler方法
#************


# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# ************
#logging高级
#利用config文件进行配置
#************
#
# logging.config.fileConfig('logging.conf')
#
#
# logger = logging.getLogger('simpleExample')
#
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


