# Trying to use the TQDM progress bar in combination with console log messages

from time import sleep
import logging

from tqdm import trange, tqdm
from tqdm.contrib.logging import logging_redirect_tqdm


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setStream(tqdm)  # <-- important
handler = log.addHandler(handler)

for i in trange(10):
    log.info("Test")
    sleep(0.2)
