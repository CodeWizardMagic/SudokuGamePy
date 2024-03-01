import pygame
import sys

import Levels
import info
from settings import WIDTH, HEIGHT, CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 3)))


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 36)
        self.menu_active = True
        self.options = ["Start Game", "Your Records", "Quit Game"]
        self.selected_option = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                # Start Game
                Levels.main()

            elif self.selected_option == 1:
                info.main()
            elif self.selected_option == 2:
                pygame.quit()

    def draw(self, screen, screen_width, screen_height):
        for i, option in enumerate(self.options):
            text_color = 'green' if i == self.selected_option else 'black'
            option_surf = self.font.render(option, False, text_color)
            option_rect = option_surf.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50))
            screen.blit(option_surf, option_rect)

        pygame.display.flip()

    def run(self, screen, screen_width, screen_height):
        while self.menu_active:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.draw(screen, screen_width, screen_height)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 3)))
    pygame.display.set_caption("Sudoku")
    menu = Menu(screen)
    menu.run(screen, 600, 600)
