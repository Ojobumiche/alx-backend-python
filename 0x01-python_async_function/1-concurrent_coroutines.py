from typing import List
import asyncio
from random import uniform


async def wait_random(max_delay: int) -> float:
    '''
    Async function that waits for a random delay between 0 and max_delay (inclusive)
    and then returns it as a float.
    '''
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async function that spawns n instances of wait_random with the specified max_delay.
    Returns a list of all the delays in ascending order.
    '''
    delay_list = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)

    delay_list.sort()
    return delay_list


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 2)))
    print(asyncio.run(wait_n(7, 4)))
    print(asyncio.run(wait_n(10, 0)))
