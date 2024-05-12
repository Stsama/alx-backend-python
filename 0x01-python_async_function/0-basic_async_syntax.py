#!/usr/bin/env python3
# created by Albert Ezoula
import random
import asyncio


async def wait_random(max_delay=10):
    """waits for a random delay between 0 and max_delay"""
    waited = random.random() * max_delay
    await asyncio.sleep(waited)
    return waited
