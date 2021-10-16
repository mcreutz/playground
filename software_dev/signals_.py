"""
Graceful exiting an app by handling the interrupt signal
"""

import signal
import time


class SignalHandler():
    __state = False

    def __init__(self):
        signal.signal(signal.SIGINT, SignalHandler.change_state)

    @classmethod
    def change_state(cls, signum, frame):
        """Interrupt method, called by system, when Ctrl-C is detected."""

        print(" Ctrl-C detected. Press again for immediate exit.")
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        cls.__state = True

    @classmethod
    def check_exit_requested(cls):
        """Check if the user pressed Ctrl-C."""
        return cls.__state


if __name__ == "__main__":
    sh = SignalHandler()
    sh2 = SignalHandler()  # Multiple usage possible
    while True:
        time.sleep(3)
        print(f"Gracefult exit requested: {sh.check_exit_requested()}")
