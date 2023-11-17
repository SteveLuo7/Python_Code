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
   优化子弹效果
   子弹碰到墙壁就消失
   最多可以发射3发子弹 不允许一直发射
   
"""
import pygame, time, random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 255, 0)


class MainGame():
    window = None
    my_tank = None
    #   存储敌方坦克的列表
    enemyTankList = []
    enemyTankCount = 5
    #   存储我方子弹的列表
    myBulletList = []

    def __init__(self):
        pass

    #   开始游戏
    def startGame(self):
        #   加载主窗口
        pygame.display.init()
        #   设置窗口长宽高
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        #   初始化我方坦克
        MainGame.my_tank = Tank(350, 250)
        #   初始化敌方坦克，并将敌方坦克添加到列表中
        self.createEnemyTank()
        #   设置窗口标题
        pygame.display.set_caption("坦克大战1.13")
        while True:
            #   让坦克移动速度变慢
            time.sleep(0.05)
            #   设置填充颜色
            MainGame.window.fill(BG_COLOR)
            self.getEvent()
            MainGame.window.blit(self.getTextSuface('ENEMY TANKS %d' % len(MainGame.enemyTankList)), (10, 10))
            #   调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #   循环遍历，展示敌方坦克
            self.blitEnemyTank()
            #   循环遍历显示我方坦克子弹
            self.blitMyBullet()
            #   调用移动方法
            #   坦克开关开启才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            #   保持事件一直再获取状态
            pygame.display.update()

    def createEnemyTank(self):
        top = 100
        #   循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left = random.randint(0,600)
            speed = random.randint(1, 4)
            enemy = enemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)

    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            enemyTank.displayTank()
            enemyTank.randMove()

    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            #   加上当前子弹是否为活着的状态的判断
            if myBullet.live:
                myBullet.displayBullet()
                myBullet.move()
            else:
                MainGame.myBulletList.remove(myBullet)


    def endGame(self):
        print("THANKS PLAYING")
        exit()

    def getTextSuface(self, text=None):
        #   初始化字体模块
        pygame.font.init()
        #   获取字体font对象
        font = pygame.font.SysFont('kaiti', 18)
        #   绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
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
                    #  切换方向
                    MainGame.my_tank.direction = 'L'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                    print("TANK TO THE LEFT")
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                    print("TANK TO THE RIGHT")
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                    print("TANK TO THE UP")
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    MainGame.my_tank.stop = False
                    MainGame.my_tank.move()
                    print(("TANK TO THE DOWN"))
                elif event.key == pygame.K_SPACE:
                    print("SHOOTING BULLETS")
                    #   创建子弹
                    #   如果挡墙我方子弹列表小于3 才可以创建子弹
                    if len(MainGame.myBulletList) <= 3:
                        myBullet = Bullet(MainGame.my_tank)
                        MainGame.myBulletList.append(myBullet)




            if event.type == pygame.KEYUP:
                #   判断松开的按键是上、下、左、右才停止坦克移动
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    MainGame.my_tank.stop = True


class Tank():
    #   添加距离左边left 上边top
    def __init__(self, left, top):
        self.images = {'U': pygame.image.load('img/p1tankU.gif'),
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
        #   速度 决定移动素的快慢
        self.speed = 10
        #   坦克移动速度的开关
        self.stop = True

    def move(self):
        #   判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < SCREEN_WIDTH:
                self.rect.left += self.speed

    def shot(self):
        pass

    def displayTank(self):
        #   获取展示的对象
        self.image = self.images[self.direction]

        MainGame.window.blit(self.image, self.rect)


class myTank(Tank):
    def __init__(self):
        pass


class enemyTank(Tank):
    def __init__(self, left, top, speed):
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif'),
        }
        #   方向 随机生成敌方坦克的方向
        self.direction = self.randDirection()
        #   根据方向 获取不同方向的图片
        self.image = self.images[self.direction]
        #   区域
        self.rect = self.image.get_rect()
        #   对left和top进行赋值
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.flag = True
        #   新增步数变量
        self.step = 20

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return "L"
        elif num == 4:
            return "R"

    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 60
        else:
            self.move()
            self.step -= 1

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
    def __init__(self,tank):
        #   加载子弹图片的属性
        self.image = pygame.image.load('img/enemymissile.gif')
        #   子弹的方向随着坦克的方向 要在属性中加入tank参数
        self.direction = tank.direction
        #   获取区域
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + self.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        self.speed = 7
        #   子弹的效果是否碰撞墙壁，如果碰到墙壁，修改此状态
        self.live = True


    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False


    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)


if __name__ == '__main__':
    MainGame().startGame()
    MainGame().getTextSuface()
