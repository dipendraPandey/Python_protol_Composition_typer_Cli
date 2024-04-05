# Protocol-based implementation for the above addition
from logging import Logger
from typing import Protocol
from datetime import time

class AddServiceProtocol(Protocol):
    "Represents functionality of adding two numbers."

    def add(self, a: int, b: int) -> int:
        ...
    # A protocol is Python's take on "structural subtyping"

# writing service to satisfy above protocal

class AddService:
    "Implements AddServiceProtocol."

    def add(self, a: int, b: int) -> int:
        return a + b
    
# lets use compostion technique to add logging service to add function
class LoggingAddService:
    """
    Implements AddServiceProtocol. Wraps AddService and adds basic logging.
    """

    def __init__(self, service: AddServiceProtocol, logger: Logger) -> None:
        self._inner = service
        self._logger = logger

    def add(self, a: int, b: int) -> int:
        result = self._inner.add(a, b)
        self._logger.debug("[add] adding %s and %s gives %s", a, b, result)
        return result
    
    # this loggingAddService is not much of different from above AddService 
    # it just add logging feature to the add function


# lets make another component that adds timing functionality to LoggingAddService

class TimingAddService:
    """
    Implements AddServiceProtocol. Wraps AddService and adds timing of method calls.
    """

    def __init__(self, service: AddServiceProtocol, logger: Logger) -> None:
        self._inner = service
        self._logger = logger

    def add(self, a: int, b: int) -> int:
        start = time.perf_counter()
        result = self._inner.add(a, b)
        end = time.perf_counter()
        elapsed = end - start
        self._logger.debug(f"[add] took {elapsed:0.8f} seconds")
        return result
    
    # Yes, it's all repetitive and a bit boring, but I'd argue this is a good thing!
    #  It doesn't take a lot of effort to understand