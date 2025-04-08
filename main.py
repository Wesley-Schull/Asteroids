import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0 # delta_time - the time since the last frame was drawn

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_is_running = True

    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()