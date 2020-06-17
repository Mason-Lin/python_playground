import logging


def this_keyword_exist_in_pythonlib(message):
    logging.info(message)
    logging.debug(message)
    logging.error(message)

    this_keyword_not_exist_in_pythonlib()

    return 'OK'
