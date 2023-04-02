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
r7 = Road(8,8,8,500,485, 5, 200)
r8 = Road(8,8,8,320,425, 5, 320)

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
    display.update()