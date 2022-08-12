#!/usr/bin/env python3
"""Parallel Comprehension"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynchronous coroutine that returns the execution time"""
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    """tasks.append(asyncio.create_task(async_comprehension()))"""
    await asyncio.gather(*tasks)
    return time.time() - start
