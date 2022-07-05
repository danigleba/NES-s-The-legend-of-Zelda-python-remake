import pygame
import tlozClasses as cl
screen = pygame.display.set_mode((768, 720))
pygame.init()


# Variables
allow_start = False
sound = pygame.mixer.Sound("overworld_theme.wav")


# Functions
def move_courtins(court, speed):
    global allow_start
    if court.rect.centerx > - 180:
        court.rect.centerx -= speed
    else:
        allow_start = True
        topUI.sprite = 1
        sound.play(-1)


def move_courtins_r(court, speed):
    if court.rect.left < 768:
        court.rect.centerx += speed


# Sprites & Animations
topUI_animation = [pygame.image.load("images/overworld-ui/top_ui-1.bmp").convert_alpha(),
                   pygame.image.load("images/overworld-ui/top_ui.bmp").convert_alpha(),
                   pygame.image.load("images/overworld-ui/top_ui2.bmp").convert_alpha()]
pause_menu_animation = [pygame.image.load("images/overworld-ui/pause_screen1.bmp").convert_alpha(),
                        pygame.image.load("images/overworld-ui/pause_screen2.bmp").convert_alpha()]


# Objects
topUI = cl.AnimatedAsset(screen, topUI_animation, 1, 0, 0, 0)
pause_menu = cl.AnimatedAsset(screen, pause_menu_animation, 0.1, 0, 0, -552)
background = cl.UI(screen, "images/overworld-ui/overworld.bmp", 0, 0)
flore = cl.UI(screen, "images/overworld-ui/flore.bmp", 0, 84)
cb = cl.Rectangle(screen, (155, 155, 155), 768, 53, 0, 579)
courtin = cl.Rectangle(screen, (0, 0, 0), 360, 768, 0, 0)
courtin2 = cl.Rectangle(screen, (0, 0, 0), 400, 768, 408, 0)
cave_entrance = cl.UI(screen, "images/overworld-ui/cave_entrance.bmp", -171, -120)
