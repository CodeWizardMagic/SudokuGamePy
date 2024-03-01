import pygame
import sys

import pygame
import sys

import menu
from settings import WIDTH, HEIGHT, CELL_SIZE


class SudokuInfoWindow:
    def __init__(self,screen, width=600, height=600):
        self.screen = screen
        self.menu_active = True
        pygame.init()
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 3)))
        pygame.display.set_caption("How to Play Sudoku")
        self.font_title = pygame.font.SysFont(None, 19)
        self.font_text = pygame.font.SysFont(None, 14)
        self.info_text = [
            "How to Play Sudoku using Pygame:",
            "",
            "Objective:",
            "The goal of Sudoku is to fill a 9x9 grid with numbers so that each row, each column,",
            "and each of the nine 3x3 subgrids (also known as regions or blocks) contain all of",
            "the digits from 1 to 9. Each number can only appear once in each row, column,",
            "and 3x3 subgrid.",
            "",
            "The Grid:",
            "- Sudoku is played on a Pygame window displaying a 9x9 grid, divided into 3x3 subgrids.",
            "- The grid starts partially filled with numbers. These numbers are called 'givens' or 'clues.'",
            "",
            "How to Play:",
            "1. Use the mouse to select an empty cell in the grid.",
            "2. Press a number key from 1 to 9 to input a number into the selected cell.",
            "3. The selected number should not conflict with any other number in the same row, column,",
            "   or 3x3 subgrid.",
            "4. If you make a mistake, you can overwrite the number in the cell with a different one.",
            "5. Continue filling in numbers until the entire grid is filled, following the Sudoku rules.",
            "",
            "Hints and Strategies:",
            "- Start by identifying the missing numbers in each row, column, and 3x3 subgrid.",
            "- Look for numbers that can only appear in one cell within a row, column, or subgrid.",
            "  These are called 'hidden singles' and can help you progress.",
            "- Use the process of elimination to deduce the possible numbers for each cell.",
            "- Be patient and methodical. Sudoku requires logic and deduction, not guesswork.",
            "",
            "Winning the Game:",
            "- Successfully filling the entire grid according to the Sudoku rules constitutes winning the game.",
            "- Once all cells are filled correctly, the Sudoku puzzle is solved.",
            "",
            "Tips:",
            "- Familiarize yourself with the Pygame interface for selecting cells and inputting numbers.",
            "- Practice regularly to improve your Sudoku-solving skills."
        ]

    def display_text(self):
        y = 20
        for line in self.info_text:
            if line:
                if line[0].isdigit():
                    text = self.font_text.render(line, True, (0, 0, 0))

                else:
                    text = self.font_title.render(line, True, (0, 0, 0))
                text_rect = text.get_rect(center=(self.width // 2, y))
                self.win.blit(text, text_rect)
                y += text_rect.height + 10

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            menu.main()

    def run(self, screen, screen_width, screen_height):
        while self.menu_active:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.handle_input()
            self.display_text()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT + (CELL_SIZE[1] * 3)))
    info_window = SudokuInfoWindow(screen)
    info_window.run(screen, 600, 600)
