# -*-coding:utf-8-*-
'''
@FileName:Logger.py 
@Author:Piepis
@Date:2022/4/8 23:06 
@Desc:该日志类可以把不同级别的日志输出到不同的日志文件中
'''
import os
import logging

class Logger:

    def __init__(self):
        handlers = {
            logging.DEBUG: "logs/debug.log",
            logging.INFO: "logs/info.log",
            logging.WARNING: "logs/warning.log",
            logging.ERROR: "logs/error.log",
            logging.CRITICAL: "logs/critical.log",
        }
        self.__loggers = {}
        logLevels = handlers.keys()
        fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
        for level in logLevels:
            # 创建logger
            logger = logging.getLogger(str(level))
            logger.setLevel(level)
            # 创建hander用于写日日志文件
            log_path = os.path.abspath(handlers[level])
            fh = logging.FileHandler(log_path)
            ch = logging.StreamHandler()
            # 定义日志的输出格式
            fh.setFormatter(fmt)
            fh.setLevel(level)
            ch.setFormatter(fmt)
            ch.setLevel(level)
            # 给logger添加hander
            logger.addHandler(fh)
            logger.addHandler(ch)
            self.__loggers.update({level: logger})

    def info(self, message):
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        self.__loggers[logging.CRITICAL].critical(message)

if __name__ == "__main__":

    logger = Logger()
    
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
