from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PiPa")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, height, width, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            


class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed



player = Player('lala-Photoroom.png', 120, win_height - 80,50, 50, 4)
monster = Enemy('circle_rgb-Photoroom.png', win_width - 80, 280,50, 50, 2)
player2 = Player('lala-Photoroom.png', 120, win_height - 230,230, 50, 4)


game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
       if e.type == QUIT:
           game = False
  
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        monster.reset()
    display.update()
