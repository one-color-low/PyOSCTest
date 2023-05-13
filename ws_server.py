#!/usr/bin/env python

import asyncio
import websockets
import time

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")

    time.sleep(1)

    await websocket.send("oioi")

    time.sleep(1)
    
    await websocket.send("shinuwa")

    time.sleep(1)
    
    await websocket.send("aitsu")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())