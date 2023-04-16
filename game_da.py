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
tr1 = GameSprite('bbe.jpg', 90, 200, 30 , 50, 0)
tr2 = GameSprite('bbe.jpg', 200, 200, 50 , 30, 0)
tr3 = GameSprite('bbe.jpg', 320, 265, 50 , 30, 0)
tr4 = GameSprite('bbe.jpg', 600, 200, 50 , 30, 0)
tr5 = GameSprite('bbe.jpg', 630, 330, 30 , 50, 0)
tr6 = GameSprite('bbe.jpg', 630, 475, 50 , 30, 0)
tr7 = GameSprite('bbe.jpg', 470, 410, 50 , 30, 0)
tr8 = GameSprite('bbe.jpg', 310, 460, 30 , 50, 0)
tr9 = GameSprite('bbe.jpg', 300, 620, 50 , 30, 0)
energ = GameSprite('energ.png', 260, 230, 50 , 50, 0)
energ2 = GameSprite('energ.png', 260, 570, 50 , 50, 0)

class Player(GameSprite):
    def update_player(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 40:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_windth - 40:
            self.rect.x += self.speed

    def update_enemy(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 40:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_windth - 40:
            self.rect.x += self.speed

player = Player('player.png', 120, 60, 30, 30, 5)
player2 = Player('rab_stol.png', 120, 20, 30, 30, 5)

font.init()
font1 = font.SysFont('Arial', 70)
lose = font1.render('хахаха', True, (180,0,0))
win = font1.render('ПОБЕДА!!!', True, (190,0,0))

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
        player.reset()
        player.update_player()
        player2.reset()
        player2.update_enemy()
        tr1.reset()
        tr2.reset()
        tr3.reset()
        tr4.reset()
        tr5.reset()
        tr6.reset()
        tr7.reset()
        tr8.reset()
        tr9.reset()
        energ.reset()
        energ2.reset()

    if sprite.collide_rect(player, goal):
        finish = True
        window.blit(win, (350, 300))
    if sprite.collide_rect(player, player2):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r1):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r2):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r3):
        finish = True
        window.blit(lose, (300, 300)) 
    if sprite.collide_rect(player, r4):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r5):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r6):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r7):
        finish = True
        window.blit(lose, (300, 300))  
    if sprite.collide_rect(player, r8):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r9):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r10):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r11):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player, r12):
        finish = True
        window.blit(lose, (300, 300))
    if sprite.collide_rect(player2, r1):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r2):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r3):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r4):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r5):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r6):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r7):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r8):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r9):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r10):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r11):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player2, r12):
        finish = True
        window.blit(win, (300, 300))
    if sprite.collide_rect(player, tr1):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr2):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr3):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr4):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr5):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr6):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr7):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr8):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player, tr9):
        finish = True
        window.blit(lose,(300,300))
    if sprite.collide_rect(player2, tr1):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr2):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr3):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr4):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr5):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr6):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr7):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr8):
        finish = True
        window.blit(win,(300,300))
    if sprite.collide_rect(player2, tr9):
        finish = True
        window.blit(win,(300,300))

    if sprite.collide_rect(player, energ):
        player.speed *= 1.007
    if sprite.collide_rect(player, energ2):
        player.speed *= 1.007    
        











    clock.tick(60)
    display.update()
