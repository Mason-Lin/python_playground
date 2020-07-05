import logging

FORMAT = '%(asctime)s <%(funcName)s:%(lineno)d> %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def foo():
    logging.debug('bar')


logging.debug('a')
foo()

x = 10
logging.debug(f'x {type(x)}')
