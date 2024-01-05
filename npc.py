import pygame
import random
import time

# screen settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AI - NPC")
    
# AI - setting 
class NPC:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x * 50, self.y * 50, 50, 50))


    def ai_move(self, player):
        dx = player.x - self.x
        dy = player.y - self.y

        if abs(dx) > abs(dy):
            self.x += 1 if dx > 0 else -1
        else:
            self.y += 1 if dy > 0 else -1
# startup
npc = NPC(3, 3)

# controller 
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x * 50, self.y * 50, 50, 50))

player = Player(1, 1)

# wake up - ckeck
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    npc.ai_move(player)

    screen.fill((255, 255, 255))
    npc.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    time.sleep(0.5)
