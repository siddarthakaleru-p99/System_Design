from logger import SingletonLogger


logger1 = SingletonLogger().get_logger()
logger2 = SingletonLogger().get_logger()

logger1.info("Application started")
logger2.warning("This is a warning message")

print(logger1 is logger2)