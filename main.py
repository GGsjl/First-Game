import pygame
import time 
import random

def main():
    width = 480 #宽
    length = 320 #长
    gap = 130
    y_gap = 100
    

    def up_tuble_size():
        return random.randint(80, 300)

    class TupleU():
        def __init__(self, i):
            self.i = i
            self.rc = (0, 0, 0)#管道颜色
            self.rp = (length+self.i*gap, 0)#管道物理位置
            self.y = up_tuble_size()
            self.rs = (15, self.y)#管道大小

    class TupleD():
        def __init__(self, y, i):
            self.y = y
            self.i = i
            self.rc = (0, 0, 0)#管道颜色
            self.rp = (length+self.i*gap, y_gap+self.y)#管道物理位置
            self.rs = (15, width)#管道大小


    pygame.init() #初始化界面
    screen = pygame.display.set_mode((length, width), 0, 32) #初始化荧幕
    pygame.display.set_caption('Bird') #明明对话框名字
    bg_color = (100, 255, 255) #背景颜色
    x = 100; y = 200 #小鸟的初始位置



    def check(tuble, x, y):
        k = 0
        for t in tuble:
            if k % 2 == 0:
                if x+25 > t.rp[0] and x+25 < t.rp[0]+15:
                    if y < t.rs[1] or y+32 > t.rs[1]+y_gap:
                        return False
                elif x > t.rp[0] and x < t.rp[0]+15:
                    if y < t.rs[1] or y+32 > t.rs[1]+y_gap:
                        return False
            k += 1
        return True

    def creat_tuble():
        tuble = []
        tu1 = TupleU(0)#创建管道
        td1 = TupleD(tu1.y, tu1.i)
        tu2 = TupleU(1)
        td2 = TupleD(tu2.y, tu2.i)
        tu3 = TupleU(2)
        td3 = TupleD(tu3.y, tu3.i)
        tuble.append(tu1);tuble.append(td1);tuble.append(tu2);tuble.append(td2);tuble.append(tu3);tuble.append(td3)
        return tuble
        
    tuble = creat_tuble()#存放管道的列表总共存6个

    socer = 0; flag = False
    while True: #0.5秒刷新一次屏幕
        
        if flag == True:#游戏运行阶段
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:#每次按空格键，跳跃20个像素点
                        y -= 20
                    elif event.key == pygame.K_q:#按q键退出
                        pygame.quit()
                        quit()


            screen.fill(bg_color)#刷新屏幕，以便后续绘制

            rc = (66, 66, 66)#小鸟颜色
            rp = (x, y)#小鸟物理位置
            rs = (40, 40)#小鸟大小
            pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))#更新小鸟位置
            

            for t in tuble:#绘制管道
                pygame.draw.rect(screen, t.rc, pygame.Rect(t.rp, t.rs))
                t.rp = (t.rp[0]-20, t.rp[1])

            for i in range(len(tuble)):#更新管道信息和得分信息
                if tuble[i].rp[0] < 0:
                    ty = up_tuble_size()
                    tuble[i].rp = (240+gap, 0);   tuble[i+1].rp = (240+gap, ty+y_gap)#更新位置
                    tuble[i].rs = (15, ty);  tuble[i+1].rs = (15, width)#更新大小
                    i += 1
                if tuble[i].rp[0] < x and tuble[i].rp[0]+30 > x:#得分
                    socer += 1
                
            
            pygame.font.init()#加载分数
            myfont = pygame.font.SysFont('Comic Sans MS', 25)
            textsurface = myfont.render(str(int(socer/2)), False, (0, 0, 0))
            screen.blit(textsurface,(0,0))


            pygame.display.update()    # 刷新画面
            time.sleep(0.5)#设置时间间隔为0.5s
            flag = check(tuble, x, y)
            y += 15#每次刷新下降15个像素点
        

        else:#游戏暂停阶段
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:#每次按空格键，跳跃20个像素点
                        flag = True
                        socer = 0
                        tuble = creat_tuble()
                    elif event.key == pygame.K_q:
                        return
            
            screen.fill(bg_color)
            myfont = pygame.font.SysFont('SimHei', 50)
            textsurface = myfont.render('Fly Bird', False, (0, 0, 0))
            screen.blit(textsurface,(60, 50))
            myfont = pygame.font.SysFont('SimHei', 25)
            textsurface = myfont.render('按R键开始游戏！', False, (0, 0, 0))
            screen.blit(textsurface,(68, 200))
            textsurface = myfont.render(' 按空格键控制', False, (0, 0, 0))
            screen.blit(textsurface,(68, 250))
            textsurface = myfont.render('按Q键退出游戏！', False, (0, 0, 0))
            screen.blit(textsurface,(68, 300))
            textsurface = myfont.render('得分:'+str(int(socer/2)), False, (0, 0, 0))
            screen.blit(textsurface,(110, 350))

            pygame.display.update()    # 刷新画面


main()
