# 初始化 
import pygame
import warnings
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("判断硫酸根离子")

# 图片导入
jd = pygame.image.load("胶头滴管.png")
jd = pygame.transform.scale(jd, (100, 100))
sb = pygame.image.load("烧杯图标.png")
sb = pygame.transform.scale(sb, (200, 200))
sg = pygame.image.load("试管.png")
sg = pygame.transform.scale(sg, (120, 200))
sd = pygame.image.load("5816beaeb8253_610_爱奇艺.jpg")
sd = pygame.transform.scale(sd, (3, 3))
js = pygame.image.load("Gameover.png")
js = pygame.transform.scale(js, (100, 100))
ks = pygame.image.load("start开始.png")
ks = pygame.transform.scale(ks, (100, 100))
bj = pygame.image.load("jjj.jpg")
bj = pygame.transform.scale(bj, (1000, 500))
bz = pygame.image.load("OPYUKOP.jpg")
bz = pygame.transform.scale(bz, (100, 50))
bj2 = pygame.image.load("t01529c468e869dc5c0.jpg")
bj2 = pygame.transform.scale(bj2, (1000, 500))
tc = pygame.image.load("按钮.png")
tc = pygame.transform.scale(tc, (100, 50))
bj3 = pygame.image.load("timg.jpg")
bj3 = pygame.transform.scale(bj3, (1000, 500))
zd = pygame.image.load("u=304846130,2092500079&fm=15&gp=0.jpg")
zd = pygame.transform.scale(zd, (100, 50))
bjzd = pygame.image.load("untitled.png")
bjzd = pygame.transform.scale(bjzd, (1000, 500))
bzd = pygame.image.load("u=2014661807,975063841&fm=26&gp=0.jpg")
bzd = pygame.transform.scale(bzd, (100, 50))
zd1 = pygame.image.load("wgfijs.jpg")
zd1 = pygame.transform.scale(zd1, (1000, 500))
qd = pygame.image.load("123123213.jpg")
qd = pygame.transform.scale(qd, (100, 50))
zq = pygame.image.load("FERGEGE.gif")
zq = pygame.transform.scale(zq, (1000, 500))
bqd = pygame.image.load("u=4276337747,279935642&fm=115&gp=0.jpg")
bqd = pygame.transform.scale(bqd, (1000, 500))
bqdd = pygame.image.load("u=2582108432,574239236&fm=26&gp=0.jpg")
bqdd = pygame.transform.scale(bqdd, (100, 50))

# 文字与提示
myfont = pygame.font.Font("simkai.ttf", 30)
chemical_formula = pygame.font.Font("consola.ttf", 30)
so = chemical_formula.render("SO₄²¯", True, [0, 0, 0])
white_so = chemical_formula.render("SO₄²¯", True, [100, 100, 100])
bacl2 = chemical_formula.render("BaCl₂", True, [255, 255, 255])
solution = myfont.render("溶液", True, [255, 255, 255])
black_bacl2 = chemical_formula.render("BaCl₂", True, [0, 0, 0])
hno3 = myfont.render("HCl溶液", True, [255, 255, 255])
ff1 = myfont.render("A", True, [255, 255, 255])
ff2 = myfont.render("B", True, [255, 255, 255])
ff3 = myfont.render("C", True, [255, 255, 255])
ff4 = myfont.render("硫酸根离子的检验", True, [0, 0, 0])
ff5 = myfont.render("EXIT", True, [255, 255, 255])
ff = myfont.render("1:检验     应先加入HCl溶液看是否有气体生成,", True, [0, 0, 0])
ff_ = myfont.render("若没有，再加入      溶液,看是否有沉淀生成，若有，则为    ", True, [0, 0, 0])
ff6 = myfont.render("2:检验     也可加入      溶液看是否有沉淀生成", True, [0, 0, 0])
ff7 = myfont.render("若有，再加入HCl溶液,看是否有气泡生成，若有，则为碳酸根离子", True, [0, 0, 0])
ff8 = myfont.render("最后点击gameoverh回答哪个试管有      （记住用大写字母A,B,C）", True, [100, 100, 100])
ff9 = myfont.render("若回答正确则会退出，回答错误则会回到开始界面", True, [100, 100, 100])

def w():
    jl3=j=h=jl1=jl=a=m=n=0
    s=3
    x30=y30=0
    x11=430
    x70=y70=0
    yq1=yq2=yq3=yq=408
    y1=10
    y2=10
    x3=20
    y3=20
    jd_move=False
    y6=y5=60
    y7=y4=350
    x=10000
    y=10000
    xshui1=xshui=10000
    yshui1=yshui=10000
    jd_jiaoshao1=60
    jd_jiaoshao2=60
    sd_jiaoshao1=20
    sd_jiaoshao2=20
    xsd=10000
    ysd=10000
    sd_move=False
    jd_shui1=jd_shui=0
    diluo2=False
    sd_shui1=sd_shui=False
    qf2=qf=cd=cd1=False
    sc2=sc1=False
    rj=False
    k=False
    qp=True
    z=False

    
    #界面判断
    running=True
    running1=True
    running2=False
    running3=False
    running4=False
    running5=False
    running6=False
    running7=False
    running8=False
    #程序执行
    while running:
        #开始界面，判断（帮助界面或主程序）
        if running1==True:
            screen.fill((255, 255, 255))
            screen.blit(bj, (0, 0))
            screen.blit(ks, (850, 50))
            screen.blit(ff4, (717, 26))
            screen.blit(bz, (850, 120))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x30,y30=pygame.mouse.get_pos()
                        if 850<x30<950 and 50<y30<120:
                            running1=False
                            running2=True
                        elif 850<x30<951 and 121<y30<169:
                            running3=True
                            running2=False
                            running1=False
            pygame.display.update()
   
        #帮助
        if running3==True:
            screen.blit(bj2, (0, 0))
            screen.blit(so, (110, 114))
            screen.blit(ff, (16, 114))
            screen.blit(ff_, (16, 144))
            screen.blit(black_bacl2, (230, 144))
            screen.blit(so, (810, 144))
            screen.blit(ff6, (16, 184))
            screen.blit(so, (110, 184))
            screen.blit(black_bacl2, (310, 184))
            screen.blit(ff7, (16, 214))
            screen.blit(tc, (20, 20))
            screen.blit(ff5, (40, 30))
            screen.blit(ff8, (20, 250))
            screen.blit(white_so, (500, 250))
            screen.blit(ff9, (20, 280))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x50, y50 = pygame.mouse.get_pos()
                        if 20 < x50 < 100 and 20 < y50 < 70:
                            running3 = False
                            running1 = True
            pygame.display.update()

        # 彩蛋
        if running4==True:
            screen.blit(bj3, (0,0))
            screen.blit(zd, (63,44))
            screen.blit(bzd, (800,44))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x70,y70=pygame.mouse.get_pos()
                        if 63<x70<163 and 44<y70<94:
                            running4=False
                            running5=True
                        if 800<x70<900 and 44<y70<94:
                            running4=False
                            running3=True
                pygame.display.update()
        if running5==True:
            screen.blit(bjzd, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        running5=False
                        w()
                pygame.display.update()
        if running6==True:
            screen.blit(zd1, (0,0))
            screen.blit(qd, (20,20))
            screen.blit(bqdd,(800,20))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x80,y80=pygame.mouse.get_pos()
                        if 20<x80<120 and 20<x80<70:
                            running6=False
                            running7=True
                        if 800<x80<900 and 20<y80<70:
                            running6=False
                            running8=True
            pygame.display.update()
        if running7==True:
            screen.blit(zq, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        running=False
            pygame.display.update()
        if running8==True:
            screen.blit(bqd,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        running8=False
                        w()
            pygame.display.update()
                    
        #主程序   
        if running2==True:   
            screen.fill((150, 150, 150))
            screen.blit(bacl2, (99, 426))
            screen.blit(solution, (190, 426))
            screen.blit(hno3, (811, 426))
            screen.blit(ff1, (387, 439))
            screen.blit(ff2, (490, 439))
            screen.blit(ff3, (590, 439))
            screen.blit(js, (850, 120))
            screen.blit(tc, (850, 50))
            screen.blit(ff5, (873, 60))
            screen.blit(jd, (x3, y3))
            #试管里的原水柱
            if m==0:
                pygame.draw.rect(screen, [0,128,255], [390,326,17,84], 0)
            pygame.draw.rect(screen, [0,128,255], [590,326,17,84], 0)
            if n==0:
                pygame.draw.rect(screen, [0,128,255],[490,326,17,84], 0)
            #bacl2水滴落下与沉淀生成
            if diluo2==True and jd_shui>=4 and jd_jiaoshao1-50<x10<jd_jiaoshao1+50 and jd_jiaoshao2-50<y10<jd_jiaoshao2+50:
                ysd+=1
                # xsd=int(xsd)
                # ysd=int(ysd)
                screen.blit(sd, (xsd,ysd))
                if ysd>=330:
                    jd_shui-=4
                    ysd=330
                    diluo2=False
                if ysd>=315 and 489<jd_jiaoshao1<508:
                    jl1=ysd-315
                    k=True
                if ysd>=315 and 390<jd_jiaoshao1<407:
                    jl=ysd-315
                    z=True
            if ysd==330:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x1480,y1480=pygame.mouse.get_pos()
                        ysd=y1480
                    
            if 390<jd_jiaoshao1<407 and rj==False and z==True and  jd_shui>=4:
                pygame.draw.rect(screen, [0,128,255],[390,326+jl,17,84-jl], 0)
                pygame.draw.rect(screen, [255,255,255], [390,396-jl,17,14+jl],0)
                s=1
                m=1
            if 390<jd_jiaoshao1<407 and rj==True:
                s=3
            if s==1:
                pygame.draw.rect(screen, [0,128,255],[390,326+jl,17,84-jl], 0)
                pygame.draw.rect(screen, [255,255,255], [390,396-jl,17,14+jl],0)
            if s==3:
                pygame.draw.rect(screen, [0,128,255], [390,326+jl+18,17,84-jl-18], 0)   
            if ysd>=315 and k==True and jd_shui>=4:
                pygame.draw.rect(screen, [0,128,255],[490,326+jl1,17,84-jl1], 0)
                pygame.draw.rect(screen, [255,255,255], [490,395-jl1,17,14+jl1],0)
                n=1
            if n==1:
                pygame.draw.rect(screen, [0,128,255],[490,326+jl1,17,84-jl1], 0)
                pygame.draw.rect(screen, [255,255,255], [490,395-jl1,17,14+jl1],0)   
            #HCl溶液的液滴与气泡，沉淀溶解    
            if diluo2==True and jd_shui1>=4 and jd_jiaoshao1-50<x10<jd_jiaoshao1+50 and jd_jiaoshao2-50<y10<jd_jiaoshao2+50:
                ysd+=1.5
                # xsd=int(xsd)
                # ysd=int(ysd)
                screen.blit(sd, (xsd,ysd))
                if ysd>=335:
                    jd_shui1-=4
                    ysd=335
                    diluo2=False
                if ysd>=320 and 390<jd_jiaoshao1<407 and diluo2==False:
                    jl3=ysd-330
            if ysd==335:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x140,y140=pygame.mouse.get_pos()
                        ysd=y140
            if 390<jd_jiaoshao1<407 and qp==True and jd_shui1>=4 and ysd==335:
                m=3
                h=1
                rj=True
                s=0
            if m==3:
                pygame.draw.rect(screen, [0,128,255], [390,326+jl3+15,17,84-jl3-15], 0)
            if h==1:
                pygame.draw.circle(screen,[0,230,230] , [395,yq], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [399,yq1+10], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [400,yq2+15], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [398,yq3-10], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [393,yq1], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [396,yq+7], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [396,yq3+17], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [403,yq2-12], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [401,yq1+17], 3, 0)
                pygame.draw.circle(screen,[0,230,230] , [403,yq3-12], 3, 0)
                yq-=1
                yq1-=2
                yq2-=3
                yq3-=4
            # 气泡：天蓝色0,128,255 位置395,408
            # 沉淀：白色 位置 382,409,26,12
            #胶头滴管中的液体增多与消减
            if jd_move:
                if jd_shui>0 and sd_shui==True:
                    pygame.draw.line(screen, (95,158,160), (x,y+25), (x,y+25-jd_shui-7), 6)
                    #pygame.draw.rect(screen, (95,158,160), (x-3,y+25,6,-jd_shui-7),0)
                if jd_shui1>0 and sd_shui1==True:
                    pygame.draw.line(screen, (0,191,255), (x,y+25), (x,y+25-jd_shui1-7), 6)
                    #pygame.draw.rect(screen, (0,191,255), (x-3,y+25,6,-jd_shui1-7),0)
            elif jd_move==False:
                if jd_shui>0 and sd_shui==False:
                    pygame.draw.line(screen, (95,158,160), (jd_jiaoshao1,jd_jiaoshao2+25), (jd_jiaoshao1,jd_jiaoshao2+25-jd_shui-7), 6)
                    #pygame.draw.rect(screen, (95,158,160), (jd_jiaoshao1-3,jd_jiaoshao2+25,6,-jd_shui-7),0)
                if jd_shui1>0 and sd_shui1==False:
                    pygame.draw.line(screen, (0,191,255), (jd_jiaoshao1,jd_jiaoshao2+25), (jd_jiaoshao1,jd_jiaoshao2+25-jd_shui1-7), 6)
                    #pygame.draw.rect(screen, (0,191,255), (jd_jiaoshao1-3,jd_jiaoshao2+25,6,-jd_shui1-7),0)
                    
            #判断事件类型
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=0
                #胶头滴管移动
                elif event.type == pygame.MOUSEBUTTONUP:
                    jd_move=False
                    if jd_shui>0:
                        sd_shui=False
                    if jd_shui1>0:
                        sd_shui1=False
                elif event.type == pygame.MOUSEMOTION:
                    if jd_move:
                        if pygame.mouse.get_pressed()[0]:
                            x2,y2=pygame.mouse.get_pos()
                            jd_jiaoshao1=x2
                            jd_jiaoshao2=y2
                            x3=x2-50
                            y3=y2-50
                            
                #水滴移动,胶头滴管水增多,上端粗口间距9，下端粗口间距从下到上为5，7        
                    if jd_move and jd_shui>=1:
                        sd_move=True
                        if sd_move:
                            xsd,ysd=pygame.mouse.get_pos()
                            sd_jiaoshao1=xsd
                            sd_jiaoshao2=ysd
                            xsd=xsd-1.5
                            ysd=ysd-1.5
                    if jd_move and jd_shui1>=1:
                        sd_move=True
                        if sd_move:
                            xsd,ysd=pygame.mouse.get_pos()
                            sd_jiaoshao1=xsd
                            sd_jiaoshao2=ysd
                            xsd=xsd-1.5
                            ysd=ysd-1.5
    
                #水减少,胶头滴管移动条件满足，jd_move=True sd_move=True
                if jd_shui<36:
                    if 83<jd_jiaoshao1<201 and y4<jd_jiaoshao2+30<420 and jd_shui1<=4:
                        y5=y5-3
                        y4=y4+3
                        jd_shui+=4
                        sd_shui=True
                if jd_shui1<36:        
                    if 792<jd_jiaoshao1<792+122 and y7<jd_jiaoshao2+30<420 and jd_shui<=4:
                        y6=y6-3
                        y7=y7+3
                        jd_shui1+=4
                        sd_shui1=True
                if jd_shui>=36:
                    jd_shui=36
                if jd_shui1>=36:
                    jd_shui1=36
                if y5<=0:
                    y5=0
                if y6<=0:
                    y6=0
                    
                #水滴移动条件判断，胶头滴管移动条件判断
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x10,y10=pygame.mouse.get_pos()
                        if jd_jiaoshao1-50<x10<jd_jiaoshao1+50 and jd_jiaoshao2-50<y10<jd_jiaoshao2+50: 
                            jd_move=True
                        if jd_shui>0:
                            sd_shui=True
                        if jd_shui1>0:
                            sd_shui1=True
                        
                #结束判断A,B,C试管中哪个含硫酸根离子，判断回到哪个界面
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x100,y100=pygame.mouse.get_pos()
                        if 850<x100<950 and  120<y100<220:
                            a=input("请判断A,B,C试管中哪个含硫酸根离子：")
                            if a=="B":
                                print("回答正确")
                                running2=False
                                running6=True
                            elif a!="B":
                                print("回答错误")
                                running4=True
                                running2=False
                        elif 850<x100<950 and 50<y100<100:# 退出按钮
                            w()
                if event.type == pygame.MOUSEMOTION:
                    x,y=pygame.mouse.get_pos()
                #水滴下落的条件
                if 390<jd_jiaoshao1<407 or 489<jd_jiaoshao1<508 or 589<jd_jiaoshao1<609:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                diluo2=True
            
            # 试管
            screen.blit(sg, (339, 230))
            screen.blit(sg, (439, 230))
            screen.blit(sg, (539, 230))
            
            # 烧杯水柱
            pygame.draw.rect(screen, [95, 158, 160], [86, y4, 116, y5], 0)
            pygame.draw.rect(screen, [0, 191, 255], [797, y7, 116, y6], 0)
            # 烧杯
            screen.blit(sb, (34, 230))
            screen.blit(sb, (745, 230))
            pygame.display.update()
#调用函数            
w()
warnings.filterwarnings("ignore")
pygame.quit()
