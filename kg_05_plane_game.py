from kg_04_plane_sprites import *
import pygame


class PlaneGame(object):

    # 初始化方法
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有化精灵类
        self.__creatSprites()
        # 定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)

        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    # 创建精灵组
    def __creatSprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.background_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 事件监听
    def __event_handler(self):
        user_action = pygame.event.get()
        for action in user_action:
            if action.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif action.type == CREATE_ENEMY_EVENT:
                enemy1 = Enemy()
                self.enemy_group.add(enemy1)
            elif action.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif action.type == pygame.KEYDOWN and action.key == pygame.K_RIGHT:

            # elif action.type == pygame.KEYDOWN and action.key == pygame.K_LEFT:
        self.hero.update()

    # 碰撞检测
    def __check_collide(self):
        if pygame.sprite.groupcollide(self.enemy_group, self.hero.bullets, True, True):
            global SCORE
            SCORE += 1

        enemise = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemise) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    # 更新绘制精灵组
    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 游戏结束
    @staticmethod
    def __game_over():
        print("游戏结束")
        # 卸载PyGame模块，释放资源
        pygame.quit()
        # 退出系统
        exit()

    def startGame(self):
        print("游戏开始")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __del__(self):
        print("最终得分：%d" % SCORE)


if __name__ == '__main__':
    planegame = PlaneGame()

    planegame.startGame()
