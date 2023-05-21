import asyncio
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
import websockets

dispatcher = Dispatcher()

# OSCデータを受信した時の処理を定義
def osc_handler(address, *args):
    print(f"Received OSC message: {address}, {args}")
    asyncio.ensure_future(send_websocket_data(args))

# "*" は全てのOSCメッセージをキャプチャします
dispatcher.map("*", osc_handler)

# Websocket接続を保存
connected_websockets = set()

async def websocket_handler(websocket, path):
    connected_websockets.add(websocket)
    try:
        await websocket.recv()
    finally:
        connected_websockets.remove(websocket)

async def send_websocket_data(data):
    if connected_websockets:  # If there are any connected websockets
        await asyncio.wait([ws.send(str(data)) for ws in connected_websockets])

# OSCサーバーとWebSocketサーバーを同時に起動
async def main():
    osc_server = AsyncIOOSCUDPServer(("0.0.0.0", 8000), dispatcher, asyncio.get_event_loop())
    osc_server_task = asyncio.create_task(osc_server.create_serve_endpoint())  # ここを変更
    
    websocket_server = await websockets.serve(websocket_handler, "0.0.0.0", 8080)
    
    await asyncio.gather(osc_server_task, websocket_server.serve_forever())

# メイン関数を呼び出す
asyncio.run(main())
