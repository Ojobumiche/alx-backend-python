import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.'''
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay



wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
