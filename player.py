import pygame
import tlozUI as ui
import tlozInputs as ip
import tlozClasses as cl


# Variables
screen = pygame.display.set_mode((768, 720))
attacking = False
wooden_sword = False
bloq_movements = False


# Functions
def move(player):
    """Moves the player's character"""
    global attacking
    movement_dict = {ip.input.right: [player.speed, 0, 2], ip.input.left: [-player.speed, 0, 3],
                     ip.input.down: [0, player.speed, 0], ip.input.up: [0, -player.speed, 1]}
    for movement in movement_dict:
        if movement and not bloq_movements:
            if not ip.input.stop:
                player.rect.centerx += movement_dict[movement][0]
                player.rect.centery += movement_dict[movement][1]
                if not attacking:
                    player.animation = player.animations[movement_dict[movement][2]]
            player.animate()


def attack(weapon):
    """Allows the player to attack"""
    global attacking
    sword_speed = 1
    sword_thrown = False
    link.speed = 0
    link.animation_speed = 0.15
    link.animate()
    attack_direction_dict = {0: [0, sword_speed, 180, 5, 180],
                             1: [0, -sword_speed, 0, 6, 0],
                             2: [-sword_speed, -0, 90, 7, -90],
                             3: [sword_speed, 0, 270, 8, 90]}
    for direction in attack_direction_dict:
        if link.animation == link.animations[direction]:
            if sword_thrown:
                sword_speed = 0
            else:
                weapon.rect.centerx += attack_direction_dict[direction][0]
                weapon.rect.centery += attack_direction_dict[direction][1]
            pygame.transform.rotate(sword_default_animation[0], 180)
            pygame.transform.rotate(weapon.image, attack_direction_dict[direction][2])
            link.animation = link.animations[attack_direction_dict[direction][3]]


def check_collision(player):
    """Checks for collision"""
    if ui.cb.activated:
        if player.rect.left < ui.cb.rect.right and player.rect.right > ui.cb.rect.left:
            if player.rect.bottom > ui.cb.rect.top > player.rect.top or \
                    player.rect.top < ui.cb.rect.bottom < player.rect.bottom:
                ip.input.down = False
                player.stop_down = True
                if ip.input.down:
                    player.rect.centery -= 2
            else:
                player.stop_down = False
        else:
            player.stop_down = False
        if player.rect.left < ui.cb.rect.right and player.rect.right > ui.cb.rect.left:
            if player.rect.top < ui.cb.rect.bottom < player.rect.bottom:
                ip.input.up = False
                player.stop_up = True
            else:
                player.stop_up = False
        else:
            player.stop_up = False
        if player.rect.top < ui.cb.rect.bottom and player.rect.bottom > ui.cb.rect.top:
            if player.rect.left < ui.cb.rect.right < player.rect.right:
                ip.input.left = False
                player.stop_left = True
            else:
                player.stop_left = False
        else:
            player.stop_left = False
        if player.rect.top < ui.cb.rect.bottom and player.rect.bottom > ui.cb.rect.top:
            if player.rect.right > ui.cb.rect.left > player.rect.left:
                ip.input.right = False
                player.stop_right = True
            else:
                player.stop_right = False
        else:
            player.stop_right = False


# Sprites & Animations
link_down = [pygame.image.load("images/link/link_down1.bmp").convert_alpha(),
             pygame.image.load("images/link/link_down2.bmp").convert_alpha(),
             pygame.image.load("images/link/link_down1.bmp").convert_alpha(),
             pygame.image.load("images/link/link_down2.bmp").convert_alpha()]
link_up = [pygame.image.load("images/link/link_up1.bmp").convert_alpha(),
           pygame.image.load("images/link/link_up2.bmp").convert_alpha(),
           pygame.image.load("images/link/link_up1.bmp").convert_alpha(),
           pygame.image.load("images/link/link_up2.bmp").convert_alpha()
           ]
link_right = [pygame.image.load("images/link/link_right1.bmp").convert_alpha(),
              pygame.image.load("images/link/link_right2.bmp").convert_alpha(),
              pygame.image.load("images/link/link_right1.bmp").convert_alpha(),
              pygame.image.load("images/link/link_right2.bmp").convert_alpha()
              ]
link_left = [pygame.image.load("images/link/link_left1.bmp").convert_alpha(),
             pygame.image.load("images/link/link_left2.bmp").convert_alpha(),
             pygame.image.load("images/link/link_left1.bmp").convert_alpha(),
             pygame.image.load("images/link/link_left2.bmp").convert_alpha()
             ]
link_get_item = [pygame.image.load("images/link/link_pick_item1.bmp").convert_alpha(),
                 pygame.image.load("images/link/link_pick_item1.bmp").convert_alpha(),
                 pygame.image.load("images/link/link_pick_item1.bmp").convert_alpha(),
                 pygame.image.load("images/link/link_pick_item1.bmp").convert_alpha()
                 ]
link_atack_down = [pygame.image.load("images/link/atack/link_atack_down1.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_down2.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_down2.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_down3.bmp").convert_alpha(),
                   pygame.image.load("images/link/link_down2.bmp").convert_alpha()]
link_atack_up = [pygame.image.load("images/link/atack/link_atack_up1.bmp").convert_alpha(),
                 pygame.image.load("images/link/atack/link_atack_up2.bmp").convert_alpha(),
                 pygame.image.load("images/link/atack/link_atack_up2.bmp").convert_alpha(),
                 pygame.image.load("images/link/atack/link_atack_up3.bmp").convert_alpha(),
                 pygame.image.load("images/link/link_up2.bmp").convert_alpha()]
link_atack_right = [pygame.image.load("images/link/atack/link_atack_right1.bmp").convert_alpha(),
                    pygame.image.load("images/link/atack/link_atack_right2.bmp").convert_alpha(),
                    pygame.image.load("images/link/atack/link_atack_right2.bmp").convert_alpha(),
                    pygame.image.load("images/link/atack/link_atack_right3.bmp").convert_alpha(),
                    pygame.image.load("images/link/link_right1.bmp").convert_alpha()]
link_atack_left = [pygame.image.load("images/link/atack/link_atack_left1.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_left2.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_left2.bmp").convert_alpha(),
                   pygame.image.load("images/link/atack/link_atack_left3.bmp").convert_alpha(),
                   pygame.image.load("images/link/link_left1.bmp").convert_alpha()]
link_animations = [link_down, link_up, link_right, link_left, link_get_item, link_atack_down, link_atack_up,
                   link_atack_right, link_atack_left]
link_speed = 2
link_animation_speed = 0.15
sword_default_animation = [pygame.image.load("images/cave/sword.bmp").convert_alpha()]
sword_explode_animation = [pygame.image.load("images/link/atack/sword/sword_explosion1.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion2.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion3.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion4.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion5.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion6.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion7.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion8.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion9.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion10.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion11.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion12.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion13.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion14.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion15.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion16.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion17.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion18.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion19.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion20.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion21.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion22.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion23.bmp").convert_alpha(),
                           pygame.image.load("images/link/atack/sword/sword_explosion24.bmp").convert_alpha(),]
sword_animations = [sword_default_animation, sword_explode_animation]


# Objects
link = cl.MultiAnimatedAsset(screen, link_animations, 1, link_animation_speed, link_speed, True, 365, 400)
link.stop_right = False
link.stop_left = False
link.stop_up = False
link.stop_down = False
link.inside = False
sword = cl.UI(screen, "images/link/atack/sword_down.bmp", link.rect.centerx, link.rect.centery)
sword_weapon = cl.MultiAnimatedAsset(screen, sword_animations, 0, 0.5, 3, False, 365, 400)
