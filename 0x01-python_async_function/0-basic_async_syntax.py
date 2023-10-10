import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.'''
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


# Example usage
async def main():
    result = await wait_random()
    print(f"The random delay is: {result} seconds")


asyncio.run(main())
