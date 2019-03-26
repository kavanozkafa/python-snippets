"""

    Debug (10): These are used to give Detailed information, typically of interest only when diagnosing problems.
    Info (20): These are used to Confirm that things are working as expected
    Warning (30): These are used an indication that something unexpected happened, or indicative of some problem in the near future
    Error (40): This tells that due to a more serious problem, the software has not been able to perform some function
    Critical (50): This tells serious error, indicating that the program itself may be unable to continue running



There are several logger objects offered by the module itself.

    Logger.info(msg) : This will log a message with level INFO on this logger.
    Logger.warning(msg) : This will log a message with level WARNING on this logger.
    Logger.error(msg) : This will log a message with level ERROR on this logger.
    Logger.critical(msg) : This will log a message with level CRITICAL on this logger.
    Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.
    Logger.exception(msg) : This will log a message with level ERROR on this logger.
    Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. This means that all the messages below this level will be ignored.
    Logger.addFilter(filt) : This adds a specific filter filt to the to this logger.
    Logger.removeFilter(filt) : This removes a specific filter filt to the to this logger.
    Logger.filter(record) : This method applies the logger’s filter to the record provided and returns True if record is to be processed. Else, it will return False.
    Logger.addHandler(hdlr) : This adds a specific handler hdlr to the to this logger.
    Logger.removeHandler(hdlr) : This removes a specific handler hdlr to the to this logger.
    Logger.hasHandlers() : This checks if the logger has any handler configured or not.

"""


#importing module
import logging

#create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')

#create an object
logger=logging.getLogger()

#setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test mesagges
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
