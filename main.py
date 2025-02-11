import pygame
from constants import *


def main():
    pygame.init()
    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        elap_time = clock.tick(60)
        dt = elap_time / 1000


if __name__ == "__main__":
    main()
