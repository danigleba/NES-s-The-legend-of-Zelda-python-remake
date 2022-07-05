import pygame
import time
import tlozInputs as ip
import tlozClasses as cl


# Variables
running = True
pygame.init()
screen_menu = pygame.display.set_mode((768, 720))
pygame.display.set_caption("The legend of Zelda")
bg_color = (252, 188, 176)
icon = pygame.image.load("images/triforce_icon.bmp")
pygame.display.set_icon(icon)
pygame.mixer.music.load("tlozMainTheme.mp3")
pygame.mixer.music.play(-1)
start = False


# Functions
def transition_waterfall():
    """Adapts the waterfall's animation to the menu transition"""
    transition_waterfall_dict = {6: 1, 7: 2, 8: 3, 8: 4, 10: 5}
    if menu_bkg.animation == menu_bkg.animations[1]:
        for change in transition_waterfall_dict:
            if menu_bkg.sprite > change:
                waterfall.animation = waterfall.animations[transition_waterfall_dict[change]]


def scroll(image):
    """Scrolls the image"""
    image.y -= image.speed
    image.rect.y = image.y
    if image.rect.top == image.screen_rect.top:
        pygame.time.wait(4000)
        image.y -= 1
        image.rect.y = image.y
    if image.rect.bottom == image.screen_rect.bottom:
        image.speed = 0


# Sprites & Animations
background_default = [pygame.image.load("images/menu/menu_background.bmp")]
background_flash = [pygame.image.load("images/menu/transition/transition1.bmp"),
                    pygame.image.load("images/menu/transition/transition2.bmp"),
                    pygame.image.load("images/menu/transition/transition3.bmp"),
                    pygame.image.load("images/menu/transition/transition4.bmp"),
                    pygame.image.load("images/menu/transition/transition5.bmp"),
                    pygame.image.load("images/menu/transition/transition6.bmp"),
                    pygame.image.load("images/menu/transition/transition7.bmp"),
                    pygame.image.load("images/menu/transition/transition8.bmp"),
                    pygame.image.load("images/menu/transition/transition9.bmp"),
                    pygame.image.load("images/menu/transition/transition10.bmp"),
                    pygame.image.load("images/menu/transition/transition11.bmp"),
                    pygame.image.load("images/menu/transition/transition12.bmp")]
background_animations = [background_default, background_flash]
waterfall_animation = [pygame.image.load("images/menu/waterfall1.bmp"), pygame.image.load("images/menu/waterfall2.bmp"),
                       pygame.image.load("images/menu/waterfall3.bmp"), pygame.image.load("images/menu/waterfall4.bmp"),
                       pygame.image.load("images/menu/waterfall5.bmp"), pygame.image.load("images/menu/waterfall6.bmp"),
                       pygame.image.load("images/menu/waterfall7.bmp"), pygame.image.load("images/menu/waterfall8.bmp"),
                       pygame.image.load("images/menu/waterfall9.bmp"),
                       pygame.image.load("images/menu/waterfall10.bmp"),
                       pygame.image.load("images/menu/waterfall11.bmp"),
                       pygame.image.load("images/menu/waterfall12.bmp")]
waterfall_transition1 = [pygame.image.load("images/menu/transition/waterfall_transition1_1.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_2.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_3.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_4.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_5.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_6.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_7.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_8.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_9.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_10.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_11.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition1_12.bmp")]
waterfall_transition2 = [pygame.image.load("images/menu/transition/waterfall_transition2_1.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_2.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_3.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_4.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_5.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_6.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_7.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_8.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_9.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_10.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_11.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition2_12.bmp")]
waterfall_transition3 = [pygame.image.load("images/menu/transition/waterfall_transition3_1.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_2.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_3.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_4.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_5.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_6.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_7.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_8.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_9.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_10.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_11.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition3_12.bmp")]
waterfall_transition4 = [pygame.image.load("images/menu/transition/waterfall_transition4_1.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_2.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_3.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_4.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_5.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_6.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_7.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_8.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_9.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_10.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_11.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition4_12.bmp")]
waterfall_transition5 = [pygame.image.load("images/menu/transition/waterfall_transition5_1.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_2.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_3.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_4.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_5.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_6.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_7.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_8.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_9.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_10.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_11.bmp"),
                         pygame.image.load("images/menu/transition/waterfall_transition5_12.bmp")]
waterfall_animations = [waterfall_animation, waterfall_transition1, waterfall_transition2, waterfall_transition3,
                        waterfall_transition4, waterfall_transition5]
triforce_animation = [pygame.image.load("images/menu/triforce1.bmp"), pygame.image.load("images/menu/triforce1.bmp"),
                      pygame.image.load("images/menu/triforce1.bmp"), pygame.image.load("images/menu/triforce1.bmp"),
                      pygame.image.load("images/menu/triforce5.bmp"), pygame.image.load("images/menu/triforce5.bmp"),
                      pygame.image.load("images/menu/triforce7.bmp"), pygame.image.load("images/menu/triforce7.bmp"),
                      pygame.image.load("images/menu/triforce9.bmp"), pygame.image.load("images/menu/triforce9.bmp"),
                      pygame.image.load("images/menu/triforce9.bmp"), pygame.image.load("images/menu/triforce9.bmp"),
                      pygame.image.load("images/menu/triforce7.bmp"), pygame.image.load("images/menu/triforce7.bmp"),
                      pygame.image.load("images/menu/triforce5.bmp"), pygame.image.load("images/menu/triforce5.bmp")]
plot_animation = [pygame.image.load("images/menu/plot.bmp"), pygame.image.load("images/menu/plot2.bmp")]


# Objects
menu_bkg = cl.MultiAnimatedAsset(screen_menu, background_animations, 0, 0.3, 0, False, 0, 0)
waterfall = cl.MultiAnimatedAsset(screen_menu, waterfall_animations, 0, 0.5, 0, True, 0, 0)
triforce = cl.AnimatedAsset(screen_menu, triforce_animation, 0.4, 0, 0, 0)
plot = cl.AnimatedAsset(screen_menu, plot_animation, 0.1, 0.5, 0, 820)


# Run
while running:
    pygame.display.flip()
    screen_menu.fill(bg_color)
    ip.input.check()
    transition_waterfall()
    if not start:
        menu_bkg.draw()
        waterfall.draw()
        waterfall.animate()
        if not menu_bkg.animation == menu_bkg.animations[1]:
            triforce.draw()
            triforce.animate()
    if ip.input.enter:
        menu_bkg.animation = menu_bkg.animations[1]
    if menu_bkg.animation == menu_bkg.animations[1]:
        menu_bkg.animate()
        if menu_bkg.sprite >= len(menu_bkg.animations[1]) - 1:
            start = True
    if start:
        menu_bkg.animation = menu_bkg.animations[0]
        bg_color = (0, 0, 0)
        plot.draw()
        plot.animate()
        scroll(plot)
        if ip.input.enter:
            from tlozFiles import screen_select
