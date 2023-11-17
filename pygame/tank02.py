"""
坦克大战游戏的需求
项目中有哪些类
每个类拥有哪些方法

1.坦克类
    我方坦克、敌方坦克
    射击
    移动
    显示坦克的方法
2.子弹类
    移动
    显示子弹的方法
3.墙壁类
    属性：是否可以通过
4.爆炸效果
    展示爆炸效果
5.音效
    播放音乐
6，主类
    开始游戏
    结束游戏
"""
import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)
class MainGame():
    window=None
    def __init__(self):
        pass
    #   开始游戏
    def startGame(self):
        #   加载主窗口
        pygame.display.init()
        #   设置窗口标题
        pygame.display.set_caption("坦克大战1.02")
        #   设置窗口长宽高
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        while True:
        #   设置填充颜色
            MainGame.window.fill(BG_COLOR)
            pygame.display.update()

    def endGame(self):
        pass


class Tank():
    def __init__(self):
        pass

    def move(self):
        pass

    def shot(self):
        pass

    def displayTank(self):
        pass


class myTank(Tank):
    def __init__(self):
        pass

class enemyTank(Tank):
    def __init__(self):
        pass

class Wall():
    def __init__(self):
        pass

    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass

    def displayExplode(self):
        pass

class Music():
    def __init__(self):
        pass

    def playMusic(self):
        pass

class Bullet():
    def __init__(self):
        pass

    def move(self):
        pass

    def displayBullet(self):
        pass

    
if __name__ == '__main__':
    MainGame().startGame()
