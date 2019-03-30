import pygame
import random

class Game_Object:
    x = 0
    y = 0
    speed_x = 1
    speed_y = 1
    image = ""
    image_width = 100
    image_height = 100

    def __init__(self, screen_height, screen_width, image_name):
        self.x = random.randint(10, screen_width)
        self.y = random.randint(10, screen_height)
        self.image = pygame.image.load(image_name).convert()
        self.image = pygame.transform.scale(self.image, (self.image_width,
                                                         self.image_height))

    def move_bounce(self, screen):

        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.collision_screen_x(screen.get_width()):
            self.speed_x *= -1

        if self.collision_screen_y(screen.get_height()):
            self.speed_y *= -1
            
    def update(self, screen):
        self.move_bounce(screen)
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse):
        bound_left = self.x
        bound_right = self.x + self.image_width
        bound_top = self.y
        bound_bottom = self.y + self.image_height

        mouse_x, mouse_y = mouse.get_pos()

        if (mouse_x >= bound_left and mouse_x <= bound_right) and (mouse_y >= bound_top and mouse_y <= bound_bottom):
               return True

        return False

    def collision_screen_x(self, screen_width):
        bound_left = self.x
        bound_right = self.x + self.image_width

        if bound_left <= 0 or bound_right >= screen_width:
            return True

        return False

    def collision_screen_y(self, screen_height):
        bound_top = self.y
        bound_bottom = self.y + self.image_height

        if bound_top <= 0 or bound_bottom >= screen_height:
            return True

        return False
        

        
