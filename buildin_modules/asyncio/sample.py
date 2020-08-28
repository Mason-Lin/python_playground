import asyncio
import time

import requests

url = "http://www.google.com.tw"
loop = asyncio.get_event_loop()
start = time.time()


async def send_request(url):
    t = time.time()
    print(f"start {t}")
    res = await loop.run_in_executor(None, requests.get, url)
    print(res)
    t = time.time()
    print(f"end {t}")


tasks = []


for i in range(10):
    task = loop.create_task(send_request(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
