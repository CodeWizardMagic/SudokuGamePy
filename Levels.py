import pygame, sys

from settings import WIDTH, HEIGHT, CELL_SIZE
from table import Table


class Level:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.FPS = pygame.time.Clock()
        self.lives_font = pygame.font.SysFont("monospace", CELL_SIZE[0] // 2)
        self.message_font = pygame.font.SysFont('Bauhaus 93', (CELL_SIZE[0]))
        self.color = pygame.Color("darkgreen")
        self.table = Table(self.screen, difficulty)

    def play_level(self):
        while True:
            self.screen.fill("gray")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.table.game_over:
                        self.table.handle_mouse_click(event.pos)

            # Lower screen display
            if not self.table.game_over:
                my_lives = self.lives_font.render(f"Lives Left: {self.table.lives}", True, pygame.Color("black"))
                self.screen.blit(my_lives,
                                 ((WIDTH // self.table.SRN) - (CELL_SIZE[0] // 2), HEIGHT + (CELL_SIZE[1] * 2.2)))
            else:
                if self.table.lives <= 0:
                    message = self.message_font.render("GAME OVER!!", True, pygame.Color("red"))
                    self.screen.blit(message, (CELL_SIZE[0] + (CELL_SIZE[0] // 2), HEIGHT + (CELL_SIZE[1] * 2)))
                elif self.table.lives > 0:
                    message = self.message_font.render("You Made It!!!", True, self.color)
                    self.screen.blit(message, (CELL_SIZE[0], HEIGHT + (CELL_SIZE[1] * 2)))

            self.table.update()
            pygame.display.flip()
            self.FPS.tick(30)


class LevelsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 36)
        self.menu_active = True
        self.options = ["Easy", "Medium", "Hard"]
        self.selected_option = 0
        self.EasyLevel = Level(screen, 4)
        self.MediumLevel = Level(screen, 8)
        self.HardLevel = Level(screen, 12)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.options)

        if keys[pygame.K_RETURN]:
            if self.selected_option == 0:
                self.menu_active = False  # Easy
                self.EasyLevel.play_level()
            elif self.selected_option == 1:
                self.menu_active = False  # Medium
                self.MediumLevel.play_level()
            elif self.selected_option == 2:
                self.menu_active = False  # Hard
                self.HardLevel.play_level()

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
    levelMenu = LevelsMenu(screen)
    levelMenu.run(screen, 600, 600)
