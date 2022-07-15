import asyncio
import itertools
import json
import websockets
from connect4 import PLAYER1, PLAYER2, Connect4

# Manual handling of ConnectionClosedOK
async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)


# Shorter code to handle ConnectionClosedOK
async def handler(websocket):
    async for message in websocket:
        print(message)


# Game Handler
async def handler(websocket):
    # Initialize a Connect Four game.
    game = Connect4()

    # Players take alternate starting turns, using the same browser.
    turns = itertools.cycle([PLAYER1, PLAYER2])
    player = next(turns)

    async for message in websocket:
        # Parse a "play" event from the UI.
        event = json.loads(message)
        assert event["type"] == "play"
        column = event["column"]

        try:
            # Play the move.
            row = game.play(player, column)
        except RuntimeError as exc:
            # Send an "error" event if the move was illegal.
            event = {
                "type": "error",
                "message": str(exc),
            }
            await websocket.send(json.dumps(event))
            continue

        # Send a "play" event to update the UI.
        event = {
            "type": "play",
            "player": player,
            "column": column,
            "row": row,
        }
        await websocket.send(json.dumps(event))

        # If move is winning, send a "win" event.
        if game.winner is not None:
            event = {
                "type": "win",
                "player": game.winner,
            }
            await websocket.send(json.dumps(event))

        player = next(turns)


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
