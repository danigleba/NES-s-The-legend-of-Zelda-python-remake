import pygame
import tlozInputs as ip
import time

pygame.init()
screen = pygame.display.set_mode((768, 720))

# Variables
stop = False
current_time = 0
move_time = 0


# Objects
class Rectangle:
    def __init__(self, screen, color, x, y, X, Y):
        """Creates the collision boxes"""
        self.screen = screen
        self.color = color
        self.activated = True
        self.rect = pygame.Rect(0, 0, x, y)
        self.rect.centerx = self.rect.centerx + X
        self.rect.centery = self.rect.centery + Y

    def draw(self):
        """Draws the collision boxes on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def deactivate(self):
        self.activated = False


class UI:
    def __init__(self, screen, sprite, x, y):
        """Creates the UI"""
        self.screen = screen
        self.sprite = sprite
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.sprite)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx + x
        self.rect.centery = self.screen_rect.centery + y

    def draw(self):
        """Draws the UI on the screen"""
        self.screen.blit(self.image, self.rect)


class AnimatedAsset:
    def __init__(self, screen, animation, animation_speed, speed, x, y):
        """Creates an animated asset"""
        self.screen = screen
        self.animation = animation
        self.animation_speed = animation_speed
        self.speed = speed
        self.x = x
        self.y = y
        self.sprite = 0
        for sprite in self.animation:
            self.rect = sprite.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + x
        self.rect.top = self.screen_rect.top + y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def animate(self):
        """Creates the animation"""
        self.sprite += self.animation_speed
        if self.sprite >= len(self.animation):
            self.sprite = 0
        self.image = pygame.transform.scale(self.animation[int(self.sprite)], (768, 720))

    def draw(self):
        """Draws the animated asset on the screen"""
        self.screen.blit(self.animation[int(self.sprite)], self.rect)


class MultiAnimatedAsset:
    def __init__(self, screen, animations, default_animation, animation_speed, speed, loop, x, y):
        """Creates an asset with multiples animations"""
        self.screen = screen
        self.animations = animations
        self.default_animation = default_animation
        self.animation_speed = animation_speed
        self.speed = speed
        self.loop = loop
        self.x = x
        self.y = y
        self.sprite = 0
        for animation in self.animations:
            for sprite in animation:
                self.rect = sprite.get_rect()
        self.screen_rect = screen.get_rect()
        self.animation = self.animations[self.default_animation]
        self.rect.left = self.screen_rect.left + x
        self.rect.top = self.screen_rect.top + y

    def animate(self):
        """Animates the asset"""
        if self.loop:
            self.sprite += self.animation_speed
            if self.sprite >= len(self.animation):
                self.sprite = 0
        else:
            if self.sprite < len(self.animation) -1:
                self.sprite += self.animation_speed
        self.image = pygame.transform.scale(self.animation[int(self.sprite)], (768, 720))

    def draw(self):
        """Draws the asset on the screen"""
        self.screen.blit(self.animation[int(self.sprite)], self.rect)


# Functions
def load_text(screen, script, font, x, y):
    """Loads text onto screen"""
    text = font.render(script, 1, (255, 255, 255))
    screen.blit(text, (x, y))


def move_keyb_square(square):
    """Moves the square inside the screen's keyboard"""
    global stop
    global current_time
    global move_time
    movement_inputs_dict = {ip.input.right: [48, 0, 1, 0, square.pos < 10],
                            ip.input.left: [-48, 0, -1, 0, square.pos > 0],
                            ip.input.up: [0, -48, 0, -11, square.posy > 0],
                            ip.input.down: [0, 48, 0, 11, square.posy < 33]}
    position_dict = {ip.input.right and square.pos > 9 and square.posy < 33: [-480, 48, -10, 11],
                     ip.input.left and square.pos < 1 and square.posy > 0: [480, -48, 10, -11]}
    for move in movement_inputs_dict:
        if move and not stop:
            move_time = pygame.time.get_ticks()
            if movement_inputs_dict[move][4]:
                sound = pygame.mixer.Sound("menu_sound.mp3")
                sound.play()
                sound.set_volume(0.4)
                square.rect.centerx += movement_inputs_dict[move][0]
                square.rect.centery += movement_inputs_dict[move][1]
                square.pos += movement_inputs_dict[move][2]
                square.posy += movement_inputs_dict[move][3]
            else:
                for position in position_dict:
                    if position:
                        square.rect.centerx += position_dict[position][0]
                        square.rect.centery += position_dict[position][1]
                        square.pos += position_dict[position][2]
                        square.posy += position_dict[position][3]
            stop = True
        if current_time - move_time > 200:
            stop = False
