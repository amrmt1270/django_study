import asyncio
import websockets

async def echo(websocket):
    print('新しいクライアントと接続しました')
    async for message in websocket:
        print(f'クライアントからのメッセージ:{message}')
        await websocket.send('こんにちは！')

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket サーバー起動中 (ws://localhost:8765)")
        await asyncio.Future()  # 無限に待機して終了しないようにする

if __name__ == "__main__":
    asyncio.run(main())
