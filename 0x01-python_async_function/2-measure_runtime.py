import asyncio
import time
from concurrent_coroutines import wait_n  # Correct the import statement


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the total time coroutines took to complete'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n


if __name__ == '__main__':
    print(measure_time(5, 3))
    print(measure_time(5, 9))
