import logging
import inspect


def test_loggingdemo():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("its a warning")
    logger.error("A major error has occurred")
    logger.critical("Critical issue")
