import pygame
from data import *

pygame.init()

class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, color = (120, 150, 100), image = None, speed = 5):
        super().__init__(x,y,width, height)
        self.COLOR = color
        self.SPEED = speed
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.IMAGE_NOW = self.IMAGE
    
    def move_image(self):
        self.IMAGE_COUNT += 1
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10 - 1:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT % 10 == 0:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]

class Hero(Sprite):
    def __init__(self, x, y, width, height, color = (120, 150, 100), image = None, speed = 5):
        super().__init__(x, y, width, height, color, image, speed)
        self.MOVE = {'UP':False, 'DOWN': False, 'LEFT': False, 'RIGHT': False}
        self.DIRECTION = False

    def move(self, window):
        if self.MOVE['UP'] and self.y > 0:
            self.y -= self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y += self.SPEED
        elif self.MOVE['DOWN'] and self.y < setting_win['HEIGHT'] - self.height:
            self.y += self.SPEED
            if self.collidelist(wall_list) != -1:
                self.y -= self.SPEED
        elif self.MOVE['LEFT'] and self.x > 0:
            self.x -= self.SPEED
            self.DIRECTION = True
            if self.collidelist(wall_list) != -1:
                self.x += self.SPEED
        elif self.MOVE['RIGHT'] and self.x < setting_win['WIDTH'] - self.width:
            self.x += self.SPEED
            self.DIRECTION = False
            if self.collidelist(wall_list) != -1:
                self.x -= self.SPEED
        
        if self.MOVE['UP'] or self.MOVE['DOWN'] or self.MOVE['LEFT'] or self.MOVE['RIGHT']:
            self.move_image()
        else:
            self.IMAGE_NOW = self.IMAGE_LIST[0]
        
        if self.DIRECTION:
            self.IMAGE_NOW = pygame.transform.flip(self.IMAGE, True, False)
        else:
            self.IMAGE_NOW = self.IMAGE
        
        window.blit(self.IMAGE_NOW, (self.x, self.y))

class Bot(Sprite):
    def __init__(self, x, y, width, height, color = (120, 150, 100), image = None, speed = 5, vertical = None, horizontal = None):
        super().__init__(x, y, width, height, color, image, speed)
        self.vertical = vertical
        self.horizontal = horizontal
        self.BULLET = pygame.Rect(self.x, self.y + self.height // 2, 20, 10)

    def move(self, window):
        if self.horizontal:
            self.x += self.SPEED
            if (self.collidelist(wall_list) != -1) or (self.x > 0) or (self.x + self.width > setting_win['WIDTH']):
                self.SPEED *= -1
        elif self.vertical:
            self.y += self.SPEED
            if self.collidelist(wall_list) != -1 or self.y < 0 or self.y + self.height > setting_win['HEIGHT']:
                self.SPEED *= -1
        self.move_image()
        window.blit(self.IMAGE, (self.x, self.y))
    
    def shoot(self, window, hero):
        self.BULLET.x -= self.SPEED
        if self.BULLET.collidelist(wall_list) != -1 or self.BULLET.x < 0 or self.BULLET.colliderect(hero):
            self.BULLET.x = self.x
        pygame.draw.rect(window, (255, 255, 0), self.BULLET)
        self.move_image()
        window.blit(self.IMAGE, (self.x, self.y))
        
def create_wall(key):
    x, y = 0, 0
    width = 20
    index_x, index_y =0, 0
    for string in maps[key]:
        for symb in string:
            if symb == '1':
                for index in range(index_y, len(maps[key])):
                    if maps[key][index][index_x] == '2':
                        wall_list.append(pygame.Rect(x, y, width, (index - index_y) * 20 + width))
                        break
            if symb == '3':
                for index in range(index_x, len(string)):
                    if maps[key][index_y][index] == '2':
                        wall_list.append(pygame.Rect(x, y, (index - index_x) * 20 + width, width))
                        break
            x += width
            index_x += 1
        index_x = 0
        index_y += 1
        x = 0
        y += width

create_wall('MAP1')