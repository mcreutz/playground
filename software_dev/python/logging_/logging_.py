import logging


# Setup root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # Not sure if necessary

# Create console handler and add to root logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARN)
console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)
root_logger.addHandler(console_handler)

# Create file handler and add to root logger
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename="logging_/file.log",
    when='midnight')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
root_logger.addHandler(file_handler)

# Create logger for this module (do separately in every module/class)
logger = logging.getLogger(__name__)

# Use logger
logger.info("Testmessage")
