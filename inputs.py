import pygame
import sys


# Variables
allow_enter = True


# Objects
class Input_check():
    """Looks for and controls user inputs"""
    def __init__(self):
        # Input variables
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.a = False
        self.b = False
        self.shift = False
        self.enter = False
        self.stop_space = False
        self.last = None
        self.stop = False
    def check(self):
        global allow_enter
        """Checks for inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.right = True
                elif event.key == pygame.K_LEFT:
                    self.left = True
                elif event.key == pygame.K_UP:
                    self.up = True
                elif event.key == pygame.K_DOWN:
                    self.down = True
                elif event.key == pygame.K_SPACE:
                    if not self.stop_space:
                        self.space = True
                        self.stop_space = True
                elif event.key == pygame.K_LSHIFT:
                    self.shift = True
                elif event.key == pygame.K_a:
                    self.a = True
                elif event.key == pygame.K_s:
                    self.b = True
                elif event.key == pygame.K_RETURN:
                    self.enter = True
                elif event.key == pygame.K_KP_ENTER:
                    if allow_enter:
                        self.enter = True
                    else:
                        self.enter = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right = False
                    self.last = "right"
                if event.key == pygame.K_LEFT:
                    self.left = False
                    self.last = "left"
                if event.key == pygame.K_UP:
                    self.up = False
                    self.last = "up"
                if event.key == pygame.K_DOWN:
                    self.down = False
                    self.last = "down"
                elif event.key == pygame.K_SPACE:
                    self.space = False
                    self.stop_space = False
                elif event.key == pygame.K_LSHIFT:
                    self.shift = False
                elif event.key == pygame.K_a:
                    self.a = False
                elif event.key == pygame.K_s:
                    self.b = False
                elif event.key == pygame.K_RETURN:
                    self.enter = False
                elif event.key == pygame.K_KP_ENTER:
                    self.enter = False


input = Input_check()
