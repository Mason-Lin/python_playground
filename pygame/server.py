import asyncio
import logging

from fastapi import FastAPI
from pydantic import BaseModel

from food import FoodServer
from snakes import Direction, SnakeServer

logging.basicConfig(level=logging.ERROR)
BOUNDS = (720, 480)
BLOCK_SIZE = 20
USERS = {}

app = FastAPI()
food = FoodServer(BLOCK_SIZE, BOUNDS)


async def main_loop():
    while True:
        await asyncio.sleep(0.06)
        for _, user_snake in USERS.items():
            if user_snake.game_over:
                continue

            user_snake: SnakeServer
            user_snake.move()
            user_snake.check_for_food(food)
            if user_snake.check_bounds() or user_snake.check_tail_collision():
                logging.warn(f"{user_snake.user_name} game over")
                user_snake.game_over = True


asyncio.create_task(main_loop())


class SteerModel(BaseModel):
    user_name: str
    direction: Direction


@app.get("/")
async def root():
    return {"version": "0.2.0"}


@app.post("/connect")
def connect(user_name):
    if user_name in USERS:
        del USERS[user_name]
    logging.info(f"{user_name} join the game")
    USERS[user_name] = SnakeServer(BLOCK_SIZE, BOUNDS, user_name)


@app.post("/steer")
def steer(req: SteerModel):
    user_snake: SnakeServer = USERS[req.user_name]
    user_snake.steer(req.direction)


@app.get("/users")
def users():
    return USERS


@app.get("/bounds")
def bounds():
    return BOUNDS


@app.get("/block_size")
def block_size():
    return BLOCK_SIZE


@app.get("/status")
def status():
    return {"user": USERS, "food": food}
