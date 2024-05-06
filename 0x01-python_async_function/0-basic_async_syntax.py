#!/usr/bin/env python3
"""import asyncio and random modules"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """takes an interger and waits for a random number of seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
