import pygame
import tlozInputs as ip
import tlozClasses as cl


# Variables
running = True
pygame.init()
screen_create = pygame.display.set_mode((768, 720))
pygame.display.set_caption("The legend of Zelda")
bg_color = (0, 0, 0)
icon = pygame.image.load("images/triforce_icon.bmp")
pygame.display.set_icon(icon)
pygame.mixer.music.stop()
name = "         "
name2 = "         "
name3 = "         "
name_square_stop = False
char = 0


# Keyboard
font = pygame.font.Font("nes_zelda_font.ttf", 24)
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "-", ".", ",", "!", "'", "&", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8",
              "9", " "]


# Functions
def write_name(square):
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
    if ip.input.shift:
        global char
        if not heart.stop:
            char = 0
            name_square.rect.centerx = 384
            sound = pygame.mixer.Sound("menu_sound.mp3")
            sound.play()
            sound.set_volume(0.4)
            if heart.pos < 2:
                name_square.rect.centery += 75
                heart.rect.centery += 75
                heart.pos += 1
            elif heart.pos == 2:
                heart.rect.centery += 66
                heart.pos += 1
                name_square.rect.centerx -= 500
            else:
                name_square.rect.centery -= 150
                heart.rect.centery -= 216
                heart.pos = 0
            heart.stop = True
    else:
        heart.stop = False


def load_text(let, y):
    text = font.render(let, 1, (255, 255, 255))
    screen_create.blit(text, (336, y))


# Sprites & Animations
name_square_animation = [pygame.image.load("images/select/name_square1.bmp"),
                         pygame.image.load("images/select/name_square2.bmp")]


# Objects
create_bkg = cl.UI(screen_create, "images/select/fondo_teclado.bmp", 0, 0)
keyboard_square = cl.UI(screen_create, "images/select/rojo_teclado.bmp", 0, 0)
keyboard_square.r_stop = False
keyboard_square.l_stop = False
keyboard_square.u_stop = False
keyboard_square.d_stop = False
keyboard_square.pos = 0
keyboard_square.posy = 0
name_square = cl.AnimatedAsset(screen_create, name_square_animation, 0.05, 0, 0, 0)
heart = cl.UI(screen_create, "images/select/corazon_teclado.bmp", 0, 0)
heart.stop = False
heart.pos = 0


# Run
while running:
    load_text(name, 144)
    load_text(name2, 219)
    load_text(name3, 294)
    pygame.display.flip()
    screen_create.fill(bg_color)
    ip.input.check()
    keyboard_square.draw()
    cl.move_keyb_square(keyboard_square)
    create_bkg.draw()
    name_square.draw()
    name_square.animate()
    write_name(name_square)
    heart.draw()
    move(heart)
    if ip.input.enter:
        if heart.pos == 3:
            from tlozFiles import screen
