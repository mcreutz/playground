from time import sleep
from logging import getLogger

_logger = getLogger(__name__)

while True:
    _logger.info('Example log message')
    sleep(1)