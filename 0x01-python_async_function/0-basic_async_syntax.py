#!/usr/bin/env python3
import random
import asyncio
"""import asyncio and random modules"""

async def wait_random(max_delay: int = 10):
    """takes an interger and waits for a random number of seconds between 0 and the integer value passed as argument."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
