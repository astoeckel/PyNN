import logging
import pylogging as pylog

appenderFile = None
filenameLogger = ''


def loggerInit():
    # Connect pylogging to the Python logging module
    pylog.reset()
    pylog.append_to_logging("PyNN")

    # Log levels are already controled in the C++ code
    # so use a low log level in the Python backend
    logging.getLogger("PyNN").setLevel(0)


def loggerAppendFile(filename):
    global appenderFile, filenameLogger

    if appenderFile is None:
        layout = pylog.ColorLayout(False, 'ABSOLUTE')
        appenderFile = pylog.FileAppender(layout, filename, False)
        logger = pylog.get_root()
        logger.addAppender(appenderFile)
        filenameLogger = filename
    elif filename != filenameLogger:
        raise Exception('Change of logfile not supported yet!')
     # this causes overwrite of logfile
        # appenderFile.setFile(filename)
        # appenderFile.activateOptions()


def loggerSetLevel(loglevel):
    # compatibility to old log levels
    assert loglevel < 5, 'invalid log level'
    logLevelList = [pylog.LogLevel.ERROR, pylog.LogLevel.WARN,
                    pylog.LogLevel.INFO, pylog.LogLevel.DEBUG, pylog.LogLevel.TRACE]
    logger = pylog.get_root()
    pylog.set_loglevel(logger, logLevelList[loglevel])

logger = None
loggerInit()
