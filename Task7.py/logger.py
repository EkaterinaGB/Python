# from datetime import datetime as dt
# from time import time as t

# def number_logger(data):
#     t = dt.now().strtime('%H:%M')
#     with open('log.csv', 'a') as file:
#         file.write('{};number;{}'
#                      .format(t, data))

import logging

logging.basicConfig(
    level=logging.INFO,
    filename='phonebook.log',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)

