import pygame
import time

pygame.display.init()
screen = pygame.display.set_mode((800, 600))
back = pygame.image.load("ThisIsFine.png")



screen.blit(back, (0, 0, 800, 600))
pygame.display.flip()

run = True
while (run):
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			run = False
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_F4 and (e.mod and pygame.KMOD_ALT):
				run = False
				
pygame.display.quit()