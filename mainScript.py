import pygame
import tlozInputs as ip
import tlozLink as lk
import tlozUI as ui
import tlozClasses as cl


# Variables
# Outside cave
running = True
pygame.init()
screen = pygame.display.set_mode((768, 720))
pygame.display.set_caption("The legend of Zelda")
bg_color = (252, 207, 182)
icon = pygame.image.load("images/triforce_icon.bmp")
pygame.display.set_icon(icon)
state = 0
text1_Y = 290
text2_y = 320
has_sword = False
current_time = 0
move_time = 0
ui.topUI.sprite = 1

# Inside Cave
font = pygame.font.Font("nes_zelda_font.ttf", 27)
text = "It's dangerous to go"
text2 = "alone! Take this."
sentence = ""
sentence2 = ""
clock = pygame.time.Clock()
leaving_cave = 0
draw_sword = False
item_colected = False
animation_ended = False
cave_entered = False
in_cave = False
ui.cb.deactivate()
pause_state = 0
allow_pause = True
allow_un_pause = False
move_time_text = 0
i = 0
n = 0


if state == 1:
    lk.link.rect.centerx = 355
    lk.link.rect.top = lk.link.screen_rect.bottom + 30


# Functions
def pause():
    global allow_pause
    global text1_Y
    global text2_y
    global pause_state
    global in_cave
    if ip.input.enter and not in_cave and allow_pause:
        pause_state = 1
    if pause_state == 1 and ui.pause_menu.rect.centery <= 275:
        ui.background.rect.centery += 4
        ui.pause_menu.rect.centery += 4
        ui.topUI.rect.centery += 4
        ui.cave_entrance.rect.centery += 4
        cave_bkg.rect.centery += 4
        text1_Y += 4
        text2_y += 4
    if ui.pause_menu.rect.centery > 275 and pause_state == 1:
        pause_state = 2


def un_pause():
    global text1_Y
    global text2_y
    global pause_state
    global allow_un_pause
    if pause_state == 2:
        if not ip.input.enter:
            allow_un_pause = True
    if allow_un_pause and ip.input.enter:
        pause_state = 3
    if pause_state == 3 and ui.pause_menu.rect.centery > -275:
        ui.background.rect.centery -= 4
        ui.pause_menu.rect.centery -= 4
        ui.topUI.rect.centery -= 4
        ui.cave_entrance.rect.centery -= 4
        cave_bkg.rect.centery -= 4
        text1_Y -= 4
        text2_y -= 4
        ip.input.enter = False
    if pause_state == 3 and ui.pause_menu.rect.centery <= -275:
        pause_state = 0
        allow_un_pause = False


def get_sword():
    global pause_state
    global has_sword
    global animation_ended
    global current_time
    global move_time
    global sentence
    global sentence2
    global item_colected
    if lk.link.rect.left < sword.rect.right - 15 and lk.link.rect.right > sword.rect.right or lk.link.rect.right > sword.rect.left +15 and lk.link.rect.left < sword.rect.left:
        if lk.link.rect.bottom > sword.rect.top + 25 and lk.link.rect.top < sword.rect.top or lk.link.rect.top < sword.rect.bottom -25 and lk.link.rect.bottom > sword.rect.bottom \
                or sword.rect.top < lk.link.rect.centery < sword.rect.bottom:
            if not animation_ended:
                lk.bloq_movements = True
                ip.allow_enter = False
                move_time = pygame.time.get_ticks()
                item_colected = True
                sound = pygame.mixer.Sound("find_object_sound_efect.wav")
                sound.set_volume(0.3)
                sound.play(0)
    if item_colected and pause_state == 0:
        ip.allow_enter = False
        sentence = ""
        sentence2 = ""
        lk.link.speed = 0
        lk.link.animation = lk.link.animations[4]
        sword.rect.centery = lk.link.rect.centery - 47
        sword.rect.centerx = lk.link.rect.centerx - 12
        ui.topUI.sprite = 2
        oldman_solo.animate()
        oldman_solo.animation = oldman_solo.animations[1]
        if current_time - move_time > 1250:
            oldman_solo.rect.centerx = 1000
        if current_time - move_time > 2500:
            animation_ended = True
            item_colected = False
            move_time = pygame.time.get_ticks()
            has_sword = True
    else:
        lk.link.speed = 2
        if animation_ended:

            if current_time - move_time > 1000 and lk.link.animation == lk.link.animations[4]:
                animation_dict = {"down": lk.link.animations[0], "up": lk.link.animations[1],
                                  "right": lk.link.animations[2], "left": lk.link.animations[3]}
                for animation in animation_dict:
                    if ip.input.last == animation:
                        lk.link.animation = animation_dict[animation]
            if not lk.link.animation == lk.link.animations[4]:
                sword.rect.centerx = 1000
                if sword.rect.centerx == 1000:
                    lk.bloq_movements = False


def animate_text():
    global pause_state
    global current_time
    global move_time_text
    global text
    global text2
    global sentence
    global sentence2
    global cave_entered
    global item_colected
    global i
    global n
    text_list = list(text)
    text2_list = list(text2)
    if cave_entered and not item_colected and pause_state == 0:
        lk.link.speed = 0
        lk.link.animation_speed = 0
        sound = pygame.mixer.Sound("cave_letters_sound_effect.wav")
        if not sentence == text:
            for letter in text:
                if current_time - move_time_text > 100:
                    sentence += text_list[i]
                    i += 1
                    sound.play()
                    move_time_text = pygame.time.get_ticks()
        elif not sentence2 == text2:
            for letter in text2:
                if current_time - move_time_text > 100:
                    sentence2 += text2_list[n]
                    n += 1
                    sound.play()
                    move_time_text = pygame.time.get_ticks()
        elif sentence2 == text2:
            lk.link.speed = lk.link_speed
            lk.link.animation_speed = lk.link_animation_speed
            lk.bloq_movements = False
    elif item_colected:
        text = ""
        text2 = ""


def scene():
    global has_sword
    global cave_entered
    if not cave_entered:
        lk.bloq_movements = True
        oldman.animation_speed = 1
        if lk.link.rect.top > 630:
            lk.link.rect.centery -= 2
            lk.link.animation = lk.link.animations[1]
            lk.link.animate()
            ip.input.stop = True
        elif lk.link.rect.top < 631:
            lk.link.animation_speed = 0
            if has_sword:
                oldman.animation = oldman.animations[2]
                if pause_state == 0:
                    oldman.draw()
                oldman.animate()
                if oldman.sprite >= len(oldman.animations[2]) - 1:
                    ip.input.stop = False
                    cave_entered = True
            elif not has_sword:
                if pause_state == 0:
                    oldman.draw()
                oldman.animate()
                if oldman.sprite >= len(oldman.animations[0]) - 1:
                    cave_entered = True


def run_second_oldman_animation():
    global cave_entered
    if cave_entered:
        if sentence2 == text2:
            ip.input.stop = False
            lk.link.animation_speed = 0.15
        if pause_state == 0:
            oldman.draw()
        oldman.animation = oldman.animations[1]
        oldman.animate()
        oldman.animation_speed = 0.1


def leave_cave():
    global state
    global cave_entered
    global sentence
    global sentence2
    global i
    global n
    if cave_entered:
        if lk.link.rect.centery > 721:
            oldman.animation = oldman.animations[0]
            oldman.sprite = 0
            oldman_solo.sprite = 0
            state = 0
            sound = pygame.mixer.Sound("stairs_sound_effect.mp3")
            sound.play()
            lk.link.rect.centerx = 211
            lk.link.rect.centery = 288
            cave_entered = False
            sentence = ""
            sentence2 = ""
            i = 0
            n = 0


def enter_cave():
    global state
    global in_cave
    if lk.link.rect.bottom < ui.cave_entrance.rect.bottom:
        if lk.link.rect.left < ui.cave_entrance.rect.right and lk.link.rect.right > ui.cave_entrance.rect.left:
            if pause_state == 0:
                ui.sound.stop()
                sound = pygame.mixer.Sound("stairs_sound_effect.mp3")
                sound.play()
                in_cave = True
    if in_cave:
        ui.flore.rect.centerx = 384
        ui.flore.draw()

        lk.link.rect.centerx = 211
        lk.link.rect.centery += 1
        if ip.input.up:
            lk.link.rect.centery += 3
        elif ip.input.down:
            lk.link.rect.centery -= 1
        lk.link.animation = lk.link.animations[1]
        lk.link.animate()
        if lk.link.rect.top == ui.cave_entrance.rect.bottom:
            state = 1
            if not lk.link.inside:
                lk.link.rect.centerx = 355
                lk.link.rect.top = lk.link.screen_rect.bottom + 30
            in_cave = False


# Sprites & Animations
oldman_animation1 = [pygame.image.load("images/cave/oldman1.png").convert_alpha(), pygame.image.load("images/cave/oldman2.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman3.png").convert_alpha(), pygame.image.load("images/cave/oldman3,5.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman4.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman5.png").convert_alpha(), pygame.image.load("images/cave/oldman6.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman7.png").convert_alpha(), pygame.image.load("images/cave/oldman8.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman9.png").convert_alpha()]
oldman_animation2 = [pygame.image.load("images/cave/oldman2_1.png").convert_alpha(), pygame.image.load("images/cave/oldman9.png").convert_alpha()]

oldman_animation3 = [pygame.image.load("images/cave/oldman3_1.png").convert_alpha(), pygame.image.load("images/cave/oldman3_2.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman3_3.png").convert_alpha(), pygame.image.load("images/cave/oldman3_3,5.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman3_4.png").convert_alpha(), pygame.image.load("images/cave/oldman3_5.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman3_6.png").convert_alpha(), pygame.image.load("images/cave/oldman7.png").convert_alpha(),
                     pygame.image.load("images/cave/oldman8.png").convert_alpha(), pygame.image.load("images/cave/oldman9.png").convert_alpha()]

oldman_animations = [oldman_animation1, oldman_animation2, oldman_animation3]
oldman = cl.MultiAnimatedAsset(screen, oldman_animations, 0, 1, 0, True, 0, 0)
cave_bkg = cl.UI(screen, "images/cave/cave_background.bmp", 0, 0)
sword = cl.UI(screen, "images/cave/sword.bmp", 0, 120)
cb = cl.Rectangle(screen, (255, 255, 255), 800, 50, 0, 388)
oldman_solo_animation1 = [pygame.image.load("images/cave/old_man.bmp").convert_alpha(), pygame.image.load("images/cave/old_man.bmp").convert_alpha()]
oldman_solo_animation2 = [pygame.image.load("images/cave/oldman2.bmp").convert_alpha(), pygame.image.load("images/cave/old_man.bmp").convert_alpha()]
oldman_solo_animations = [oldman_solo_animation1, oldman_solo_animation2]
oldman_solo = cl.MultiAnimatedAsset(screen, oldman_solo_animations, 0, 0.3, 0, True, 360, 385)


# Run
while running:
    enter_cave()
    lk.sword_weapon.draw()
    if lk.attacking:
        lk.sword_weapon.rect.centerx = lk.link.rect.centerx
        lk.sword_weapon.rect.centery = lk.link.rect.centery
    else:
        lk.sword_weapon.rect.centerx = 1000
    if pause_state > 0:
        lk.link.animation_speed = 0
        lk.link.speed = 0
        ip.input.stop = True
        oldman.animation_speed = 0
    else:
        lk.link.animation_speed = lk.link_animation_speed
        lk.link.speed = lk.link_speed
        ip.input.stop = False
        oldman.animation_speed = 0.1
    ui.pause_menu.animate()
    if ui.allow_start:
        pause()
        un_pause()
    if ui.topUI.sprite == 2:
        lk.wooden_sword = True
    if ip.input.a and not lk.attacking and lk.wooden_sword:
        lk.attacking = True
        lk.link.sprite = 0
        ip.input.a = False
    if lk.attacking:
        lk.attack(lk.sword)
    if lk.link.sprite >= len(lk.link.animation) - 1:
        lk.attacking = False
        lk.link.speed = lk.link_speed
        lk.link.animation_speed = lk.link_animation_speed
    if state == 0:
        ui.pause_menu.draw()
        ui.topUI.draw()
        pygame.display.flip()
        screen.fill(bg_color)
        ip.input.check()
        ui.cave_entrance.draw()
        ui.background.draw()
        if not ui.allow_start:
            if not in_cave:
                ui.move_courtins(ui.courtin, 1)
                ui.move_courtins_r(ui.courtin2, 1)
                ui.courtin.draw()
                ui.courtin2.draw()
        if lk.link.inside:
            lk.link.draw()
            lk.link.rect.centerx = 211
            ui.flore.draw()
            ip.input.stop = True
            lk.link.animation = lk.link.animations[0]
            lk.link.animate()
            if lk.link.rect.bottom > ui.cave_entrance.rect.bottom and leaving_cave == 0:
                ui.flore.rect.centerx = 384
                lk.link.rect.centery -= 1
            else:
                ip.input.stop = False
                ui.sound.play()
                ui.allow_start = True
                lk.link.inside = False
                ui.flore.rect.centerx = 1500
        if ui.allow_start:
            if not lk.link.inside:
                if pause_state == 0:
                    lk.link.draw()
            ui.background.draw()
            lk.move(lk.link)
            lk.check_collision(lk.link)
    elif state == 1:
        ui.pause_menu.draw()
        ui.topUI.draw()
        animate_text()
        lk.link.inside = True
        clock.tick(60)
        current_time = pygame.time.get_ticks()
        lk.check_collision(lk.link)
        cl.load_text(screen, sentence, font, 110, text1_Y)
        cl.load_text(screen, sentence2, font, 155, text2_y)
        scene()
        run_second_oldman_animation()
        pygame.display.flip()
        screen.fill(bg_color)
        if cave_entered:
            ip.input.check()
        cave_bkg.draw()
        lk.move(lk.link)
        leave_cave()
        if oldman.sprite >= 8:
            draw_sword = True
        elif oldman.sprite < 8 and oldman.animation == oldman.animations[0]:
            draw_sword = False
        if draw_sword:
            if pause_state == 0:
                oldman_solo.draw()
                sword.draw()
        get_sword()
        if pause_state == 0:
            lk.link.draw()
