import logging
import signal
import time
import sys

LOGGER = logging.getLogger(__name__)


def do_exit(signum, stack):
    LOGGER.info('Received signal: %s', signum)
    LOGGER.info('Exiting now.')
    raise SystemExit('Exiting application.')


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level="INFO")
    signal.signal(signal.SIGTERM, do_exit)

    while True:
        LOGGER.info('Heartbeat')
        time.sleep(10)
