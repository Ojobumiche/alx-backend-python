#!/usr/bin/env python3

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''This is an asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.'''
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


