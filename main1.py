import pygame
import math
from Game_Object import *
from pygame.locals import *
from sys import exit

pygame.init()

screen_height = 600
screen_width = 480
screen = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('Click Pikachu!')

pika = Game_Object(screen_height, screen_width, "pika.jpeg")

clock = pygame.time.Clock()
score = 0
timeleft = 30000 
407
def handle_mouse():
        global score
        pos_x, pos_y = pygame.mouse.get_pos()
        if pika.is_clicked(pygame.mouse):
                score += pika.get_value()
        else:
                score -= pika.get_value()

def display(message):
        font = pygame.font.Font(None,36)
        text = font.render(message, 1, (10, 10, 10))
        screen.blit(text, (0,0))
        
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			handle_mouse()

	screen.fill((255,255,255))
	pika.update(screen)
	timeleft = int((30000 - pygame.time.get_ticks()) / 1000)
	display("Score: " + str(score) + " Time Left: " + str(timeleft))
	pygame.display.update()
	clock.tick(120)

	if timeleft <= 0:
                break

