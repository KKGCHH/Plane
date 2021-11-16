import random
import pygame

SCREEN_RECT = pygame.rect.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_SPEND = 2
HERO_FIRE_EVENT = pygame.USEREVENT + 1
SCORE = 0


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, spend=1):
        # 初始化父类
        super().__init__()
        # 使用精灵类加载图像
        self.image = pygame.image.load(image_name)
        # 加载图像初始位置
        self.rect = self.image.get_rect()
        # 定义移动速度
        self.spend = spend

    def update(self):
        # y轴向下移动速度
        self.rect.y += self.spend


class BackGround(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        # 判断是否移出屏幕，if = T 将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.y


# 敌机类
class Enemy(GameSprite):
    def __init__(self):
        # 调用父类方法，创建敌机精灵，指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度
        self.spend = random.randint(1, 10)
        # 指定敌机的初始随机位置
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        # 调用父类方法，保持垂直飞行
        super().update()
        # 判断敌机是否飞出屏幕。如果是则删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        pass
        # print("X: %d Y: %d" % (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += HERO_SPEND
        elif keys_pressed[pygame.K_LEFT]:
            self.rect.x -= HERO_SPEND
        elif keys_pressed[pygame.K_UP]:
            self.rect.y -= HERO_SPEND
        elif keys_pressed[pygame.K_DOWN]:
            self.rect.y += HERO_SPEND

        if self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        elif self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
        elif self.rect.y <= 0:
            self.rect.y = 0
        '''while True:
            print("X: %d Y: %d" % (self.rect.x, self.rect.y))'''

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            #bullet1 = Bullet()
            #bullet2 = Bullet()
            bullet.rect.y = self.rect.y - i * 20
            bullet.rect.x = self.rect.centerx
            #bullet1.rect.y = self.rect.y - i * 20
            #bullet1.rect.x = self.rect.centerx - 20
            #bullet2.rect.y = self.rect.y - i * 20
            #bullet2.rect.x = self.rect.centerx + 20
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)
        # self.rect.centerx = SCREEN_RECT.centerx
        # self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):
        super().update()
        if self.rect.y <= 0:
            self.kill()
