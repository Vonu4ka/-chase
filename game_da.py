from pygame import *

display.set_caption('фе')

win_windth = 800
win_height = 700
background = transform.scale(image.load('fon1.jpg'), (win_windth, win_height))
window = display.set_mode((win_windth, win_height))

clock = time.Clock()
FPS = 60

class Road(sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, height, windth):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.windth = windth
        self.height = height
        self.image = Surface((self.windth, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_road(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

r1 = Road(8,8,8,100,20, 250, 5)
r2 = Road(8,8,8,160,20, 200, 5)
r3 = Road(8,8,8,100,270, 5, 540)
r4 = Road(8,8,8,160,220, 5, 540)
r5 = Road(8,8,8,700,220, 270, 5)
r6 = Road(8,8,8,640,270, 160, 5)
r7 = Road(8,8,8,400,485, 5, 300)
r8 = Road(8,8,8,320,425, 5, 320)
r8 = Road(8,8,8,320,425, 5, 320)
r9 = Road(8,8,8,320,425, 150, 5)
r10 = Road(8,8,8,400,490, 155, 5)
r11 = Road(8,8,8,50,640, 5, 355)
r12 = Road(8,8,8,50,570, 5, 270)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, windth, height, speed):
        self.image = transform.scale(image.load(player_image), (windth, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

goal = GameSprite('cel.png', 50, 580, 50, 50, 0)

game = True
finish = False
while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        r1.draw_road()
        r2.draw_road()
        r3.draw_road()
        r4.draw_road()
        r5.draw_road()
        r6.draw_road()
        r7.draw_road()
        r8.draw_road()
        r9.draw_road()
        r10.draw_road()
        r11.draw_road()
        r12.draw_road()
        goal.reset()
    clock.tick(60)
    display.update()
