import httpx
import pygame

from snakes import Direction

USER_NAME = "123"
SERVER = "127.0.0.1"
PORT = "12345"
BOUNDS = httpx.get(f"http://{SERVER}:{PORT}/bounds").json()
BLOCK_SIZE = httpx.get(f"http://{SERVER}:{PORT}/block_size").json()

pygame.init()
window = pygame.display.set_mode(BOUNDS)
pygame.display.set_caption("Snake")
httpx.post(f"http://{SERVER}:{PORT}/connect?user_name={USER_NAME}")
font = pygame.font.SysFont("comicsans", 60, True)


def _draw(game, window, status):
    # draw snake
    for user in status.get("user", {}):
        for x, y in status["user"][user]["body"]:
            pygame.draw.rect(window, (0, 0, 255), (x, y, BLOCK_SIZE, BLOCK_SIZE))

        # draw head
        x, y = status["user"][user]["body"][-1]
        pygame.draw.rect(window, (0, 255, 255), (x, y, BLOCK_SIZE, BLOCK_SIZE))

    # draw food
    game.draw.rect(window, (0, 255, 0), (status["food"]["x"], status["food"]["y"], BLOCK_SIZE, BLOCK_SIZE))


run = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    move = None
    if keys[pygame.K_LEFT]:
        move = Direction.LEFT.value
    elif keys[pygame.K_RIGHT]:
        move = Direction.RIGHT.value
    elif keys[pygame.K_UP]:
        move = Direction.UP.value
    elif keys[pygame.K_DOWN]:
        move = Direction.DOWN.value
    if move is not None:
        httpx.post(f"http://{SERVER}:{PORT}/steer", json={"user_name": USER_NAME, "direction": move})

    window.fill((0, 0, 0))
    status = httpx.get(f"http://{SERVER}:{PORT}/status").json()
    _draw(pygame, window, status)
    if not status["user"].get(USER_NAME) or status["user"][USER_NAME]["game_over"]:
        window.blit(font.render("Game Over", True, (255, 255, 255)), (0, 0))
        run = False

    pygame.display.update()

pygame.time.delay(1000)
