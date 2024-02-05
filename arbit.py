import asyncio
from exchangesConfig import exchanges
from websockets.server import serve

async def echo(websocket):
    async for messages in websocket:
        await websocket.send(messages)
        

async def main(): 
    async with serve(echo ,"localhost", 8425 ):
        await asyncio.Future()

asyncio.run(main())