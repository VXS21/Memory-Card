from pygame import *

from random import *

win_width=700
win_height = 500  
window = display.set_mode((win_width, win_height))#создай окно игры

clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial', 40)
win = font.render('ТЫ ВЫИГРАЛ !' , True , (0, 255, 0))
lose = font.render('ТЫ ПРОИГРАЛ!' , True , (255, 0, 0))

speed = 15

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

mixer.init()
fire = mixer.Sound('fire.ogg')
mixer.music.load('space.ogg') 
mixer.music.play()

game = True

check = 0 

display.set_caption('Шутер') 

win_heigth, win_width = 500, 700

lost = 0
check = 0 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sizeX, sizeY, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizeX,sizeY))
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
                self.rect.x += self.speed
    def fire(self):
        keys_pressed = key.get_pressed()
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15,20,-15)
        bullets.add()
                
class Enemy(GameSprite):
    direction = "down"
    def update(self):
        self.rect.y += self.speed 
        global lost 
        if self.rect.y >= win_height:   
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost +1

class Bullet(GameSprite):
    direction = "up"
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y < 0:
            self.kill()
        if keys_pressed[Q] and self.rect.x > 5:
            self.rect.x -= self.speed

enemy_list = {}

for enemy in enemy_list:
    enemy.update()

bullets = sprite.Group()
monsters = sprite.Group()

corable = Player('rocket.png', 450, 400, 65, 86, 15) 

for i in range(1, 6):
    randomSizeEq=randint(80,120)
    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, randomSizeEq*0.8, randomSizeEq*0.5, randint(1, 5))
    monsters.add(monster) 



while game :

    info = font.render("Счёт"+str(check),True, (224, 255, 255))
    info1 = font.render("пропущено:"+str(lost), True, (224, 255, 255))

    window.blit(background,(0, 0))

    corable.reset()
    corable.move()

    for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    fire.play()
                    corable.fire()

    monsters.draw(window)
    monsters.update()
    

    bullets.draw(window)
    bullets.update()

    window.blit(info,(10, 10))
    window.blit(info1,(10, 30))


    
    display.update()
    clock.tick(FPS)