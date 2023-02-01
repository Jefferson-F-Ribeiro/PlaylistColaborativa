import asyncio
import websockets

async def handle_client(websocket, path):
    async for message in websocket:
        await websocket.send(message)

async def start_server():
    server = await websockets.serve(handle_client, 'localhost', 8765)
    await server.wait_closed()

async def close_server(server):
    server.close()
    await server.wait_closed()

async def send_message(websocket, message):
    await websocket.send(message)

async def handle_errors(websocket, path):
    try:
        await handle_client(websocket, path)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()