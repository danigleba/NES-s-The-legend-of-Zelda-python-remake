import pygame
import tlozInputs as ip
import tlozClasses as cl


# Variables
running = True
pygame.init()
screen_select = pygame.display.set_mode((768, 720))
pygame.display.set_caption("The legend of Zelda")
bg_color = (0, 0, 0)
icon = pygame.image.load("images/triforce_icon.bmp")
pygame.display.set_icon(icon)
pygame.mixer.music.stop()
clock = pygame.time.Clock()
state = 0
create = False
delete = False
allow_space = False
stop_shift = False
name_saved = False
name2_saved = False
name3_saved = False
name = "         "
name2 = "         "
name3 = "         "
subname = "   0"
name_square_stop = False
char = 0


# Keyboard
font = pygame.font.Font("nes_zelda_font.ttf", 24)
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "-", ".", ",", "!", "'", "&", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8",
              "9", " "]


# Functions
def write_name():
    """Writes the letters"""
    global name_square_stop
    global name
    global name2
    global name3
    global char
    if ip.input.a or ip.input.b:
        if not name_square_stop:
            if heart.pos == 0:
                if ip.input.a:
                    new_name = name[:char] + characters[int(keyboard_square.pos + keyboard_square.posy)] + name[char + 1:]
                elif ip.input.b:
                    new_name = name[:char] + " " + name[char + 1:]
                name = new_name
            if heart.pos == 1:
                if ip.input.a:
                    new_name = name2[:char] + characters[int(keyboard_square.pos + keyboard_square.posy)] + name2[char + 1:]
                elif ip.input.b:
                    new_name = name2[:char] + " " + name2[char + 1:]
                name2 = new_name
            if heart.pos == 2:
                if ip.input.a:
                    new_name = name3[:char] + characters[int(keyboard_square.pos + keyboard_square.posy)] + name3[char + 1:]
                elif ip.input.b:
                    new_name = name3[:char] + " " + name3[char + 1:]
                name3 = new_name
            name_square_stop = True
            if heart.pos < 3:
                pygame.mixer.Sound("menu_letter_sound_efect.mp3.").play()
                if char < 7:
                    name_square.rect.centerx += 24
                    char += 1
                else:
                    name_square.rect.centerx -= 168
                    char = 0
    else:
        name_square_stop = False


def move(heart):
    """Moves the heart between the 4 options"""
    vertical_pos_dict = {0: 360, 1: 435, 2: 510, 3: 576}
    i = 0
    for i in vertical_pos_dict:
        if heart.pos == i:
            if i == 3:
                heart.rect.centery = vertical_pos_dict[i]
                name_square.rect.centery += 2000
            else:
                name_square.rect.centery = vertical_pos_dict[i]
                heart.rect.centery = vertical_pos_dict[i]
            i += 1
    if ip.input.shift:
        global char
        if not heart.stop:
            sound = pygame.mixer.Sound("menu_sound.mp3")
            sound.play()
            sound.set_volume(0.4)
            char = 0
            name_square.rect.centerx = 384
            if heart.pos == 0:
                if name2_saved:
                    heart.pos = 2
                    if name3_saved:
                        heart.pos = 3
                else:
                    heart.pos = 1
            elif heart.pos == 1:
                if name3_saved:
                    heart.pos = 3
                else:
                    heart.pos = 2
            elif heart.pos == 2:
                heart.pos += 1
            elif heart.pos == 3:
                if name_saved:
                    heart.pos = 1
                    if name2_saved:
                        heart.pos = 2
                        if name3_saved:
                            heart.pos = 3
                else:
                    heart.pos = 0
            heart.stop = True
    else:
        heart.stop = False


def move_select(asset):
    vertical_pos_dict = {0: 120, 1: 192, 2: 262, 3: 357, 4: 405}
    i = 0
    for i in vertical_pos_dict:
        if asset.pos == i:
            asset.rect.centery = vertical_pos_dict[i]
            i += 1

    if ip.input.shift:
        if not asset.stop:
            sound = pygame.mixer.Sound("menu_sound.mp3")
            sound.play()
            sound.set_volume(0.4)
            if asset.pos == 0:
                if name2_saved:
                    asset.pos = 1
                elif name3_saved:
                    asset.pos = 2
                else:
                    asset.pos = 3
            elif asset.pos == 1:
                if name3_saved:
                    asset.pos = 2
                else:
                    asset.pos = 3
            elif asset.pos == 2:
                if not name_saved or not name2_saved:
                    asset.pos = 3
                else:
                    asset.pos = 4
            elif asset.pos == 3:
                if name_saved or name2_saved or name3_saved:
                    asset.pos = 4
                else:
                    sound.set_volume(0)
            else:
                if name_saved:
                    asset.pos = 0
                elif name2_saved:
                    asset.pos = 1
                elif name3_saved:
                    asset.pos = 2
                else:
                    asset.pos = 3

            asset.stop = True
    else:
        asset.stop = False


def move_heart_d(heart):
    """Moves the heart in the delete screen"""
    vertical_pos_dict = {0: 360, 1: 435, 2: 510, 3: 576}
    i = 0
    for i in vertical_pos_dict:
        if heart.pos == i:
            heart.rect.centery = vertical_pos_dict[i]
            i += 1

    if ip.input.shift:
        if not heart.stop:
            sound = pygame.mixer.Sound("menu_sound.mp3")
            sound.play()
            sound.set_volume(0.4)
            if heart.pos == 0:
                if name2_saved:
                    heart.pos = 1
                elif name3_saved:
                        heart.pos = 2
                else:
                    heart.pos = 3
            elif heart.pos == 1:
                if name3_saved:
                    heart.pos = 2
                else:
                    heart.pos = 3
            elif heart.pos == 2:
                heart.pos += 1
            elif heart.pos == 3:
                if name_saved:
                    heart.pos = 0
                elif name2_saved:
                    heart.pos = 1
                elif name3_saved:
                    heart.pos = 2
                else:
                    heart.pos = 3
            heart.stop = True
    else:
        heart.stop = False


# Sprites & Animations
delete_bgk = cl.UI(screen_select, "images/select/delete_background.bmp", 0, 0)
heart_d = cl.UI(screen_select, "images/select/delete_heart.bmp", 0, 0)
heart_d.pos = 3
name_square_animation = [pygame.image.load("images/select/name_square1.bmp"),
                         pygame.image.load("images/select/name_square2.bmp")]
keyboard_square_animation = [pygame.image.load("images/select/rojo_teclado.bmp"),
                             pygame.image.load("images/select/rojo_teclado2.bmp")]
create_bkg = cl.UI(screen_select, "images/select/fondo_teclado.bmp", 0, 0)
keyboard_square = cl.AnimatedAsset(screen_select, keyboard_square_animation, 0.05, 0, 0, 0)
keyboard_square.r_stop = False
keyboard_square.l_stop = False
keyboard_square.u_stop = False
keyboard_square.d_stop = False
keyboard_square.pos = 0
keyboard_square.posy = 0
name_square = cl.AnimatedAsset(screen_select, name_square_animation, 0.05, 0, 0, 0)
heart = cl.UI(screen_select, "images/select/corazon_teclado.bmp", 0, 0)
heart.stop = False
heart.pos = 0
heart_animation = [pygame.image.load("images/select/files_heart1.bmp"),
                   pygame.image.load("images/select/files_heart2.bmp")]
files_bkg = cl.UI(screen_select, "images/select/select1.png", 0, 0)
heart_f = cl.AnimatedAsset(screen_select, heart_animation, 0, 0, 0, -3)
heart_f.pos = 3
heart_f.stop = False
lives_name = cl.UI(screen_select, "images/select/lives_name.png", 0, 0)
lives_name2 = cl.UI(screen_select, "images/select/lives_name2.png", 0, 0)
lives_name3 = cl.UI(screen_select, "images/select/lives_name3.png", 0, 0)


# Run
while running:
    clock.tick(60)
    cl.current_time = pygame.time.get_ticks()
    if state == 0:
        pygame.display.flip()
        screen_select.fill(bg_color)
        ip.input.check()
        files_bkg.draw()
        heart_f.draw()
        move_select(heart_f)
        if name_saved:
            lives_name.draw()
            cl.load_text(screen_select, name, font, 215, 264)
            cl.load_text(screen_select, subname, font, 215, 290)
        if name2_saved:
            lives_name2.draw()
            cl.load_text(screen_select, name2, font, 215, 335)
            cl.load_text(screen_select, subname, font, 215, 361)
        if name3_saved:
            lives_name3.draw()
            cl.load_text(screen_select, name3, font, 215, 406)
            cl.load_text(screen_select, subname, font, 215, 432)
        if heart_f.pos == 3 and ip.input.enter and allow_space:
            if not name_saved:
                heart.pos = 0
            elif not name2_saved:
                heart.pos = 1
            elif not name3_saved:
                heart.pos = 2
            else:
                heart.pos = 4
            state = 1
            allow_space = False
        if heart_f.pos == 0 and name_saved and allow_space:
            if ip.input.enter:
                from theLegendOfZelda import screen
        elif heart_f.pos == 1 and name2_saved and allow_space:
            if ip.input.enter:
                from theLegendOfZelda import screen
        elif heart_f.pos == 2 and name3_saved and allow_space:
            if ip.input.enter:
                from theLegendOfZelda import screen
        if heart_f.pos == 4:
            if ip.input.enter and allow_space:
                if name_saved:
                    heart_d.pos = 0
                elif name2_saved:
                    heart_d.pos = 1
                elif name3_saved:
                    heart_d.pos = 2
                else:
                    heart_d.pos = 4
                allow_space = False
                state = 2
    elif state == 1:
        move(heart)
        cl.load_text(screen_select, name, font, 336, 144)
        cl.load_text(screen_select, name2, font, 336, 219)
        cl.load_text(screen_select, name3, font, 336, 294)
        pygame.display.flip()

        screen_select.fill(bg_color)
        ip.input.check()

        keyboard_square.draw()
        keyboard_square.animate()
        cl.move_keyb_square(keyboard_square)
        create_bkg.draw()
        name_square.draw()
        name_square.animate()
        write_name()
        heart.draw()
        if heart.pos == 3:
            if ip.input.enter and allow_space:
                if name != "         ":
                    name_saved = True
                if name2 != "         ":
                    name2_saved = True
                if name3 != "         ":
                    name3_saved = True
                keyboard_square.pos = 0
                keyboard_square.rect.centerx = 384
                keyboard_square.posy = 0
                keyboard_square.rect.centery = 360
                if name_saved:
                    heart_f.pos = 0
                elif name2_saved:
                    heart_f.pos = 1
                elif name3_saved:
                    heart_f.pos = 2
                elif name3_saved and name2_saved and name_saved:
                    heart_f.pos = 4
                else:
                    heart_f.pos = 3
                state = 0
                allow_space = False
    elif state == 2:
        pygame.display.flip()
        screen_select.fill(bg_color)
        ip.input.check()
        delete_bgk.draw()
        heart_d.draw()
        move_heart_d(heart_d)
        cl.load_text(screen_select, name, font, 336, 144)
        cl.load_text(screen_select, name2, font, 336, 219)
        cl.load_text(screen_select, name3, font, 336, 294)
        if ip.input.enter:
            if heart_d.pos == 3 and allow_space:
                if name_saved:
                    heart_f.pos = 0
                elif name2_saved:
                    heart_f.pos = 1
                elif name3_saved:
                    heart_f.pos = 2
                elif name3_saved and name2_saved and name_saved:
                    heart_f.pos = 4
                else:
                    heart_f.pos = 3
                state = 0
                allow_space = False
            elif heart_d.pos == 0 and allow_space:
                name = "         "
                name_saved = False
            elif heart_d.pos == 1 and allow_space:
                name2 = "         "
                name2_saved = False
            elif heart_d.pos == 2 and allow_space:
                name3 = "         "
                name3_saved = False
    if not ip.input.enter:
        allow_space = True
    else:
        allow_space = False
