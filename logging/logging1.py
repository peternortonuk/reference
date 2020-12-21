"""
Levels are:
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

Default behaviour is that messages of WARNING or above are reported

Basic Configurations
Use the basicConfig(**kwargs) method to configure
    level: The root logger will be set to the specified severity level.
    filename: This specifies the file.
    filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
    format: This is the format of the log message.


"""
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')


a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
