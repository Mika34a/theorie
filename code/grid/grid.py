import pygame
import sys
import platform

if platform.system() == "Windows":

        pygame.init()

        width = 800; height = 800
        screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Grid of 50/50")

        def draw_grid():
                        
                row = col = 50
                row_width = width // row
                col_height = height // col

                x = 0; y = 0

                for i in range(row):
                        x += row_width
                        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, height))

                for i in range(col):
                        y += col_height
                        pygame.draw.line(screen, (255, 255, 255), (0, y), (width, y))

        def main():

                running = True
                        
                while running:

                        screen.fill((0, 0, 0))

                        draw_grid()

                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        running = False
                                        sys.exit(0)

                        pygame.display.update()

        main()

        pygame.image.save_extended("pygame test")

