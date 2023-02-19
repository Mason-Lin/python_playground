import logging
from PythonLib import pythonlib


def this_keyword_exist_in_robotlib(message):
    logging.info(message)
    logging.debug(message)
    logging.error(message)

    pythonlib.this_keyword_exist_in_pythonlib('hello pythonlib')

    this_keyword_not_exist_in_robotlib()  # noqa: F821
    return 'OK'
