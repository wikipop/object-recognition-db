from typing import Callable
import logging


class Event:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Continue(Event):
    def __init__(self):
        super().__init__(False)


class Break(Event):
    def __init__(self):
        super().__init__(True)


class Module:
    def __init__(self, loop_function: Callable[[], Continue | Break]):
        self.loop_function = loop_function
        self.loop()

    def __start__(self):
        logging.info(f"Starting {self.__class__.__name__} module...")

    def __end__(self):
        logging.info(f"Ending {self.__class__.__name__} module...")

    def loop(self):
        self.__start__()

        try:
            while self.loop_function() == Continue():
                pass

            self.__end__()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            self.__end__()
            raise e
