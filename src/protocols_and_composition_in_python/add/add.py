import logging
from datetime import time
# here we will implement different ways and use composition programming
# this is simple implenentation
def add(a: int, b: int) -> int:
    return a + b

# lets add logger to the add function

logger = logging.getLogger(__name__)

def add1(a: int, b: int) -> int:
    result = a + b
    logger.debug("adding %s and %s gives %s", a, b, result)
    return result



# now we need to see the time taken by the function to perform addition then

def add2(a: int, b: int) -> int:
    t_start = time.perf_counter()
    result = a + b
    t_end = time.perf_counter()
    logger.debug("adding %s and %s gives %s", a, b, result)
    took = t_end - t_start
    logger.debug("took %s seconds", took)
    return result


