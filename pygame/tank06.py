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
""""
新增功能
   绘制我方坦克
"""
import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR = pygame.Color(255,255,0)
class MainGame():
    window=None
    my_tank = None
    def __init__(self):
        pass

    #   开始游戏
    def startGame(self):
        #   加载主窗口
        pygame.display.init()
        #   设置窗口长宽高
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #   初始化我方坦克
        MainGame.my_tank = Tank(350,250)
        #   设置窗口标题
        pygame.display.set_caption("坦克大战1.02")
        while True:
            #   设置填充颜色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            MainGame.window.blit(self.getTextSuface('ENEMY TANKS %d'%6),(10,10))
            #   调用坦克显示的方法
            MainGame.my_tank.displayTank()
        #   保持事件一直再获取状态
            pygame.display.update()

    def endGame(self):
        print("THANKS PLAYING")
        exit()

    def getTextSuface(self,text=None):
        #   初始化字体模块
        pygame.font.init()
        #   获取字体font对象
        font = pygame.font.SysFont('kaiti',18)
        #   绘制文字信息
        textSurface = font.render(text,True,TEXT_COLOR)
        return textSurface

    def getEvent(self):
    #   获取所有事件
        eventList = pygame.event.get()
    #   遍历事件
        for event in eventList:
            #   判断按下的按键是关闭还是键盘按下
             if event.type == pygame.QUIT:
                 self.endGame()
             if event.type == pygame.KEYDOWN:
            #   判断按下的按钮
                 if event.key == pygame.K_LEFT:
                    print("TANK TO THE LEFT")
                 elif event.key == pygame.K_RIGHT:
                    print ("TANKE TO THE RIGHT")
                 elif event.key == pygame.K_UP:
                    print("TANK TO THE UP")
                 elif event.key == pygame.K_DOWN:
                    print(("TANK TO THE DOWN"))

class Tank():
    #   添加距离左边left 上边top
    def __init__(self,left,top):
        self.images = {'U':pygame.image.load('img/p1tankU.gif'),
                      'D': pygame.image.load('img/p1tankD.gif'),
                      'L': pygame.image.load('img/p1tankL.gif'),
                      'R': pygame.image.load('img/p1tankR.gif'),
                      }
        self.direction = 'D'

        self.image = self.images[self.direction]

        #   根据图片获取区域
        self.rect = self.image.get_rect()
        #   设置区域的left和top
        self.rect.left = left
        self.rect.top = top

    def move(self):
        pass

    def shot(self):
        pass

    def displayTank(self):
        #   获取展示的对象
        self.image = self.images[self.direction]

        MainGame.window.blit(self.image,self.rect)

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
    MainGame().getTextSuface()
