import asyncio
import time
from typing import List


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay) and returns total_time / n'''
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n


if __name__ == '__main__':
    print(measure_time(5, 3))
    print(measure_time(5, 9))
