#作者：30708洪庭安、30931胡瑀真
#禮從天降
'''
遊戲規則:
1.在禮物移到字母位置時按下鍵盤
2.一個禮物5分、沒按到-1、按錯-2
3.超過通關分數可到下一關，禮物移動最大速度+1、最多禮物同時出現數+1、新增禮物頻率-5、通關分數+5、禮物移動最小速度每兩關+1
4.不確定到幾關以後會變得不合理，我們只玩到第九關
'''
import pygame, random, sys, time            #引用函式庫 
from pygame.locals import *                 #引用函式庫 
 
#------------------------------設定常數------------------------------ 
 
WINDOWWIDTH = 1311                           #設定視窗寬度 
WINDOWHEIGHT = 756                          #設定視窗高度 
TEXTCOLOR = (255, 0, 0)                     #文字顏色為紅色 
BACKGROUNDCOLOR = (255, 255, 255)           #背景顏色為白色 
FPS = 100                                   #程式畫面更新速度 
 
ARTICLESIZE = 50  #物件尺寸
ARTICLEMINSPEED = 1  #物件移動最小速度
ARTICLEMAXSPEED = 3  #物件移動最大速度
ADDNEWARTICLERATE = 120  #新增物件的頻率

NAH=1
NAL=1


#10排
width=(WINDOWWIDTH-ARTICLESIZE)/10
L1=50
L2=190
L3=320
L4=450
L5=565
L6=680
L7=810
L8=928
L9=1045
L10=1185
line=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10]
q=0
w=0
e=0
r=0
t=0
y=0
u=0
i=0
o=0
p=0

#得分區域
ptop=WINDOWHEIGHT-(ARTICLESIZE)*3
pbottom=WINDOWHEIGHT+ARTICLESIZE

getpiont=5
losepoint=2
holdtime=80

Game= 1
score = 50
passpoint=45
 
#------------------------------定義函式------------------------------ 
 
def terminate():                            #結束程式 
    pygame.quit() 
    sys.exit() 
 
def waitForPlayerToPressKey():              #暫停遊戲等待玩家按鍵 
    while True: 
        for event in pygame.event.get():    #偵測事件發生 
            if event.type == QUIT:          #關閉視窗則程式結束 
                terminate() 
            if event.type == KEYDOWN:       #如果有按下按鍵 
                if event.key == K_ESCAPE:   #按下 ESC 鍵則程式結束 
                    terminate() 
                elif event.key == K_SPACE:  #按下空白鍵則繼續遊戲 
                    print("Space key pressed")
                    return 
 
def drawText(text, font, surface, x, y):    #繪製文字 
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect() 
    textrect.topleft = (x, y) 
    surface.blit(textobj, textrect) 
 
#-------------------------初始化 pygame 和設定視窗------------------------- 
 
pygame.init()                               #pygame 初始化 
mainClock = pygame.time.Clock()             #設定調整程式執行速度之物件 
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) 
pygame.display.set_caption('喜從天降')      #設定視窗標題 
 
#------------------------------設定字型物件------------------------------ 
 
font = pygame.font.SysFont(None, 32)        #設定字型
f=pygame.font.SysFont(None, 50)
 
#------------------------------設定音效物件------------------------------ 
 
pygame.mixer.music.load('background.mp3')               #設定背景音樂 
getBananaSound = pygame.mixer.Sound('money.wav')        #設定接到香蕉音效 
gameSuccessSound = pygame.mixer.Sound('success.wav')    #設定遊戲成功音效 
gameOverSound = pygame.mixer.Sound('gameover.wav')      #設定遊戲失敗音效 
 
#------------------------------設定影像物件------------------------------ 
 
bananaImage = pygame.image.load('banana.png')
backgroundImage = pygame.image.load('woods.png')        #設定背景圖像 
 
#------------------------------顯示起始畫面------------------------------ 
 
windowSurface.fill(BACKGROUNDCOLOR)         #畫出背景和顯示文字 
drawText('Catch The Gifts', font, windowSurface, (WINDOWWIDTH/2 )-90, (WINDOWHEIGHT /3))
drawText('Level 1', f, windowSurface, (WINDOWWIDTH/2 )-70, (WINDOWHEIGHT /3)+50)
drawText('get '+str(passpoint)+' point to win', font, windowSurface, (WINDOWWIDTH/2 )-100, (WINDOWHEIGHT /3)+100)
drawText('Press "SPACE" key to start.', font, windowSurface, (WINDOWWIDTH /2)-140, (WINDOWHEIGHT /2)+50 )
drawText('(please switch witch to English input)', font, windowSurface, (WINDOWWIDTH /2)-180, (WINDOWHEIGHT /2)+80 )
drawText('click the letter on your keyboard  ', font, windowSurface, (WINDOWWIDTH /2)-500, (WINDOWHEIGHT /2)+160 )
drawText('when gifts touch the letter on the screen  ', font, windowSurface, (WINDOWWIDTH /2)-500, (WINDOWHEIGHT /2)+190 )
drawText('*one gift = 5 points ', font, windowSurface, (WINDOWWIDTH /2)-500, (WINDOWHEIGHT /2)+220 )
drawText('*miss = -2 points ', font, windowSurface, (WINDOWWIDTH /2)-500, (WINDOWHEIGHT /2)+250 )
drawText('*click on wrong time = -3 points ', font, windowSurface, (WINDOWWIDTH /2)-500, (WINDOWHEIGHT /2)+280 )
pygame.display.update()                     #更新畫面 
waitForPlayerToPressKey()                   #暫停遊戲等待玩家按鍵 
 
#------------------------------主程式開始------------------------------ 

while True:                                 #主程式是個無窮迴圈
    while score>=passpoint:
        passpoint+=5
        GameTime = 2000                         #設定遊戲時間(在 FPS 為 100 的情形下約 20 秒) 
        score = 0                               #分數初始為 0 
         
        bananas = []                            #宣告新香蕉字典物件的串列 
     
        bananaAddCounter = 0                    #香蕉計數器初始為 0 

        pygame.mixer.music.play(-1, 0.0)        #重頭播放背景音樂且為循環播放 
         
    #------------------------------遊戲計時開始------------------------------ 
         
        while GameTime > 0:                     #當遊戲時間未歸零的情形下遊戲進行 
            GameTime -= 1                       #遊戲時間遞減 
             
            for event in pygame.event.get():    #偵測事件發生 
                if event.type == QUIT:          #關閉視窗則程式結束 
                    terminate()
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    waitForPlayerToPressKey()
                    
             
    #-------------------------新增香蕉,移動香蕉,碰撞偵測------------------------- 
             
            bananaAddCounter += 1                           #香蕉計數累加 
            if bananaAddCounter == ADDNEWARTICLERATE:       #當達到預設之新增物件的頻率時 
                bananaAddCounter = 0                        #累加計數歸 0

                for j in range (random.randint(NAL, NAH)):
                    j+=1
                    newBanana = {'rect': pygame.Rect(line[random.randint(0,9)], 0 - ARTICLESIZE, ARTICLESIZE, ARTICLESIZE), 
                                 'speed': random.randint(ARTICLEMINSPEED, ARTICLEMAXSPEED)} 
                    bananas.append(newBanana)                   #新增新香蕉字典物件並放到串列中 

             
            for b in bananas: 
                b['rect'].move_ip(0, b['speed'])            #將香蕉從天而降 
             
            for b in bananas: 
            
                #按到
                if pygame.key.get_pressed(): #當有按下按鍵
                    if pygame.key.get_pressed()[K_q]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L1 and b['rect'].right<=L2:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:                                           #按鍵按著會一直偵測到，扣分太快，因此變成用按錯時間計算扣分
                            q+=1                                        #官網有相關功能，可以將長按計成一次，但我們用了沒效(不確定怎麼用)
                            if q>holdtime:
                                q=0
                                score -= losepoint
                                
                    if pygame.key.get_pressed()[K_w]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L2 and b['rect'].right<=L3:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            w+=1
                            if w>holdtime:
                                w=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_e]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L3 and b['rect'].right<=L4:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            e+=1
                            if w>holdtime:
                                w=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_r]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L4 and b['rect'].right<=L5:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            r+=1
                            if r>holdtime:
                                r=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_t]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L5 and b['rect'].right<=L6:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            t+=1
                            if t>holdtime:
                                t=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_y]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L6 and b['rect'].right<=L7:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            y+=1
                            if y>holdtime:
                                y=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_u]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L7 and b['rect'].right<=L8:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            u+=1
                            if u>holdtime:
                                u=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_i]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L8 and b['rect'].right<=L9:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            i+=1
                            if i>holdtime:
                                i=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_o]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L9 and b['rect'].right<=L10:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            o+=1
                            if o>holdtime:
                                o=0
                                score -= losepoint

                    if pygame.key.get_pressed()[K_p]:
                        if b['rect'].top>=ptop and b['rect'].bottom<=pbottom:
                            if b['rect'].left>=L10 and b['rect'].right<=WINDOWWIDTH:
                                getBananaSound.play()                   #播放接到香蕉音效 
                                score += getpiont
                                bananas.remove(b)
                        else:
                            p+=1
                            if p>holdtime:
                                p=0
                                score -= losepoint

                if b['rect'].top > WINDOWHEIGHT+ARTICLESIZE: #當香蕉落地
                    score -= 1
                    bananas.remove(b) 

    #------------------------------繪製視窗------------------------------ 
             
            windowSurface.blit(backgroundImage, (0, 0))     #畫出背景圖 
             
            drawText('Time: %s' % (GameTime/100), font, windowSurface, 10, 0) 
            drawText('Score: %s' % (score), font, windowSurface, 1200, 0)    #繪製文字 
             
            for b in bananas:                               #畫出每 1 串香蕉 
                windowSurface.blit(bananaImage, b['rect']) 

             
            pygame.display.update()                         #更新畫面 
            mainClock.tick(FPS)                             #設定程式執行速度 
             
    #-------------------------遊戲計時結束,顯示遊戲結果------------------------- 
         
        pygame.mixer.music.stop()               #停止背景音樂
         
        if score >= passpoint:                         #時間到後若分數達 70 以上為過關
            
            NAH+=1
            Game+=1
            
            if Game%2==0 :
                ARTICLEMINSPEED+=1
        
            ARTICLEMAXSPEED+=1
            ADDNEWARTICLERATE-=5
            gameSuccessSound.play()             #播放成功音效與顯示文字 
            drawText('Success!!', font, windowSurface, (WINDOWWIDTH/2 )-70, (WINDOWHEIGHT /3))
            drawText('Next Level : '+str(Game), f, windowSurface, (WINDOWWIDTH/2 )-110, (WINDOWHEIGHT /3)+50)
            drawText('get '+str(passpoint)+' point to win', font, windowSurface, (WINDOWWIDTH/2 )-100, (WINDOWHEIGHT /3)+100)
            drawText('Press "SPACE" key to continue.', font, windowSurface, (WINDOWWIDTH /2)-150, (WINDOWHEIGHT /2)+50)

            pygame.display.update()                 #更新畫面 
            waitForPlayerToPressKey()               #等待玩家按鍵繼續 
            gameSuccessSound.stop()                 #關閉音效 
            gameOverSound.stop()                    #關閉音效 

                                       
    gameOverSound.play()                #播放失敗音效與顯示文字
    passpoint=50
    NAH=1
    NAL=1
    Game+= 1
    ARTICLEMINSPEED = 1  #物件移動最小速度
    ARTICLEMAXSPEED = 3  #物件移動最大速度
    ADDNEWARTICLERATE = 120  #新增物件的頻率
    score=50
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH/2 )-70, (WINDOWHEIGHT / 3))
    drawText('You got it to level '+str(Game)+'!', font, windowSurface, (WINDOWWIDTH/2 )-90, (WINDOWHEIGHT / 3)+50)

    drawText('Press "SPACE" key to continue.', font, windowSurface, (WINDOWWIDTH /2)-150, (WINDOWHEIGHT /2)+100) 
    pygame.display.update()                 #更新畫面 
    waitForPlayerToPressKey()               #等待玩家按鍵繼續 
    gameSuccessSound.stop()                 #關閉音效 
    gameOverSound.stop()                    #關閉音效 
         
    #------------------------------主程式結束------------------------------ 
