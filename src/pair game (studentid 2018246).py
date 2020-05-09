import pygame, random, sys,time
from pygame.locals import*
windowwidth= 800
windowheight= 490
boxsize= 150
gap= 10
xbox= 10
ybox= 10
g=160 #box+gap
left= 10
top= 10
#cursorx= 0
#cursory= 0
clickoneicon=[]
iconlist= []
coverlist= []
uncoverd= []
#clickedbox= []
#clicked= []
matched=[]
uncovered=[]
#uncoverdonceormore= []
runtime=0
limeleftend=0

black= [000,000,000]
green= [000,225,000]
red=   [235,000,000]
grey=  [100,100,100]

#resourses
square= pygame.image.load('square.png')
trangle= pygame.image.load('trangle.png')
hexagon= pygame.image.load('hexagon.png')
cover= pygame.image.load('cover.png')

iconlist.append(square) #you can use iconlist.extend(square,circle,hexagon)
iconlist.append(trangle)
iconlist.append(hexagon)
coverlist.append(cover)

#pairs
iconlist *=4
coverlist *=12
def makeicongrid(screen,iconlist,xbox,ybox,g):
    random.shuffle(iconlist)
    j=0
    for i in range (4):
        screen.blit(iconlist[j],(xbox,ybox,boxsize,boxsize))
        j+=1
        xbox+=g
    for i in range (5,9):
        screen.blit(iconlist[j],(xbox-(g*4),ybox+g,boxsize,boxsize))
        j+=1
        xbox+=g
    for i in range (10,14):
        screen.blit(iconlist[j],(xbox-(g*8),ybox+g*2,boxsize,boxsize))
        j+=1
        xbox+=g
    pygame.display.flip()
    return(iconlist)
def makecovergrid(screen,coverlist,xbox,ybox,g):
    k=0
    for i in range(4):
        screen.blit(coverlist[k], (xbox,ybox,boxsize,boxsize))
        xbox+=g
    for i in range(5,9):
        screen.blit(coverlist[k], (xbox-(g*4),ybox+g,boxsize,boxsize))
        xbox+=g
    for i in range(9,13):
        screen.blit(coverlist[k], (xbox-(g*8),ybox+g*2,boxsize,boxsize))
        xbox+=g
    pygame.display.flip()

def clicktobox(screen,left,top,cursorx,cursory,clickoneicon,uncoverd,uncovered):
    if cursorx <= g and cursory <= g:
        left=10
        top=10
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
            
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=0
    elif cursorx <= g*2 and cursory <= g:
        left+=g 
        top=10
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=1
    elif cursorx <= g*3 and cursory <= g:
        left+=g*2
        top=10
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=2
    elif cursorx <= g*4 and cursory <= g:
        left+=g*3
        top=10
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=3
    elif cursorx <= g and cursory <= g*2:
        left=10
        top=170
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=4
    elif cursorx <= g*2 and cursory <= g*2:
        left+=g
        top=170
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=5
    elif cursorx <= g*3 and cursory <= g*2:
        left+=g*2
        top=170
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=6
    elif cursorx <= g*4 and cursory <= g*2:
        left+=g*3
        top=170
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=7
    elif cursorx <= g and cursory <= g*3:
        left=10
        top=330
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=8
    elif cursorx <= g*2 and cursory <= g*3:
        left+=g
        top=330
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=9
    elif cursorx <= g*3 and cursory <= g*3:
        left+=g*2
        top=330
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=10
    elif cursorx <= g*4 and cursory <= g*3:
        left+=g*3
        top=330
        if (left,top,boxsize,boxsize) in uncovered:
            uncoverd=[]
            clickoneicon=[]
            print('ftt')
        elif (left,top,boxsize,boxsize) not in uncoverd:
            uncoverd.append((left,top,boxsize,boxsize))
        t=11
    #if (left,top,boxsize,boxsize) not in uncoverdonceormore:
    #    uncoverdonceormore.append((left,top,boxsize,boxsize))
    #    print(uncoverdonceormore)
    
    areabox= pygame.Rect(left,top,boxsize,boxsize)    
    if areabox.collidepoint(cursorx,cursory):
        screen.fill(grey,(left,top,boxsize,boxsize))
        screen.blit(iconlist[t],(left,top))
        clickoneicon.append(t)
        pygame.display.flip()
        return(left,top,boxsize,boxsize,clickoneicon) # get clicked area from mouse click
def textin(screen,tp,lt,textt,size):
    font=pygame.font.Font('freesansbold.ttf',size)
    text = font.render(textt,1,grey,black)
    textRect = text.get_rect()
    textRect.center = (tp,lt)
    screen.blit(text, textRect)
    pygame.display.flip()
def textbutt(screen,tp,lt,textt,size,bt,rt):
    pygame.draw.rect(screen,black,(tp,lt,bt,rt))
    font=pygame.font.Font('freesansbold.ttf',size)
    text = font.render(textt,1,grey,black)
    screen.blit(text,(tp+5,lt+5))
    pygame.display.flip()                
def showtimer(screen,playtime,timl,timt,runtime,limeleftend):
    timeleft=((runtime+playtime)-pygame.time.get_ticks())//1000
    font = pygame.font.Font('freesansbold.ttf', 25)
    texttime = font.render('Time: ' + str(timeleft),1,grey, black)
    texttimeRect = texttime.get_rect()
    texttimeRect.center = (timl,timt)
    screen.blit(texttime, texttimeRect)
    pygame.display.flip()
    return(timeleft)
def lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered):
    score=0
    playtime=63000
    matched=[]
    missed=[]
    uncovered=[]
    #uncoverdonceormore=[]
    textin(screen,705,30,'Score: ' + str(score),25)
    pygame.draw.rect(screen,black,(650,78,102,32))
    font=pygame.font.Font('freesansbold.ttf',25)
    text = font.render('level 1',1,green,black)
    screen.blit(text,(650+5,78+5))
    pygame.draw.rect(screen,black,(650,115,102,32))
    textbutt(screen,650,115,'level 2',25,68,32)
    textbutt(screen,650,152,'quit',25,68,32)
    pygame.display.set_caption('memory game')
    firstclick=None
    makeicongrid(screen,iconlist,xbox,ybox,g)
    #pygame.time.wait(800)
    makecovergrid(screen,coverlist,xbox,ybox,g)
    while True:
        mouseClicked= False
        for event in pygame.event.get():
            if event.type==QUIT or (event.type== KEYUP and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEMOTION:
                cursorx, cursory= event.pos
            elif event.type== MOUSEBUTTONDOWN:
                cursorx, cursory= event.pos
                mouseClicked= True
                clicktobox(screen,left,top,cursorx,cursory,clickoneicon,uncoverd,uncovered)
             
                if 650<cursorx<728 and 78<cursory<103:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 650<cursorx<728 and 115<cursory<140:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvltwo(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 650<cursorx<728 and 152<cursory<177:
                    pygame.quit()
                    quit()
                    sys.exit()

        showtimer(screen,playtime,700,60,runtime,limeleftend)
        timeleft=((runtime+playtime-pygame.time.get_ticks())//1000)
        if timeleft<=0:
            loss(screen,playtime)
            
        if len(clickoneicon)==2:
            if iconlist[clickoneicon[0]]== iconlist[clickoneicon[1]]:
                matched.append(iconlist[clickoneicon[0]])
                matched.append(iconlist[clickoneicon[1]])
                uncovered.append(uncoverd[0])
                uncovered.append(uncoverd[1])
                score+=20
                textin(screen,705,30,'Score: ' + str(score),25)
                pygame.display.flip()
                if len(matched)==12:
                    won(screen,score,playtime,timeleft)
                    uncoverd=[]
                    uncovered=[]
                    clickoneicon=[]
                    break
                else:
                    uncoverd=[]
                    clickoneicon=[]

            else:
                pygame.time.wait(200)
                missed.append(iconlist[clickoneicon[0]])
                missed.append(iconlist[clickoneicon[1]])
                if uncoverd[0] not in uncovered:
                    screen.blit(cover,(uncoverd[0]))
                if uncoverd[1] not in uncovered:
                    screen.blit(cover,(uncoverd[1]))
                uncoverd=[]
                clickoneicon=[]
def lvltwo(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered):
    score=0
    playtime=63000
    matched=[]
    uncovered=[]
    #uncoverdonceormore=[]
    missed=[]
    textin(screen,705,30,'Score: ' + str(score),25)
    pygame.draw.rect(screen,black,(650,78,102,32))
    textbutt(screen,650,78,'level 1',25,68,32)
    pygame.draw.rect(screen,black,(650,115,102,32))
    font=pygame.font.Font('freesansbold.ttf',25)
    text = font.render('level 2',1,green,black)
    screen.blit(text,(650+5,115+5))
    textbutt(screen,650,152,'quit',25,68,32)
    pygame.display.set_caption('memory game')
    firstclick=None
    makeicongrid(screen,iconlist,xbox,ybox,g)
    pygame.time.wait(800)
    makecovergrid(screen,coverlist,xbox,ybox,g)
    while True:
        mouseClicked= False
        for event in pygame.event.get():
            if event.type==QUIT or (event.type== KEYUP and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEMOTION:
                cursorx, cursory= event.pos
            elif event.type== MOUSEBUTTONDOWN:
                cursorx, cursory= event.pos
                mouseClicked= True
                clicktobox(screen,left,top,cursorx,cursory,clickoneicon,uncoverd,uncovered)
             
                if 650<cursorx<728 and 78<cursory<103:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 650<cursorx<728 and 115<cursory<140:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvltwo(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 650<cursorx<728 and 152<cursory<177:
                    pygame.quit()
                    quit()
                    sys.exit()

        showtimer(screen,playtime,700,60,runtime,limeleftend)
        timeleft=((runtime+playtime-pygame.time.get_ticks())//1000)
        if timeleft<=0:
            loss(screen,playtime)
        if len(clickoneicon)==2:
            if iconlist[clickoneicon[0]]== iconlist[clickoneicon[1]]:
                matched.append(iconlist[clickoneicon[0]])
                matched.append(iconlist[clickoneicon[1]])
                uncovered.append(uncoverd[0])
                uncovered.append(uncoverd[1])
                score+=20
                textin(screen,705,30,'Score: ' + str(score),25)
                pygame.display.flip()
                if len(matched)==12:
                    won(screen,score,playtime,timeleft)
                    uncoverd=[]
                    uncovered=[]
                    clickoneicon=[]
                    break
                else:
                    uncoverd=[]
                    clickoneicon=[]

            else:
                pygame.time.wait(200)
                missed.append(clickoneicon[0])
                missed.append(clickoneicon[1])
                if uncoverd[0] not in uncovered:
                    screen.blit(cover,(uncoverd[0]))
                if uncoverd[1] not in uncovered:
                    screen.blit(cover,(uncoverd[1]))
                uncoverd=[]
                clickoneicon=[]
def loss(screen,playtime):
    screen.fill(red)
    textin(screen,400,190,' You Lost',115)
    textbutt(screen,80,360,'playagain',50,250,70)
    textbutt(screen,500,360,' quit',50,150,70)
    while True:
        mouseClicked= False
        for event in pygame.event.get():
            if event.type==QUIT or (event.type== KEYUP and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEMOTION:
                cursorx, cursory= event.pos
            elif event.type== MOUSEBUTTONDOWN:
                cursorx, cursory= event.pos
                mouseClicked= True
                if 147<cursorx<297 and 369<cursory<447:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 503<cursorx<653 and 369<cursory<447:
                    pygame.quit()
                    quit()
                    sys.exit()
    pygame.display.flip()
def won(screen,score,playtime,timeleft):
    limeleftend=timeleft
    runtime=(60-limeleftend)
    timeleft=(runtime+playtime-pygame.time.get_ticks())//1000
    score+=(60-runtime)
    screen.fill(green)
    textin(screen,400,290,'Score: ' + str(score),25)
    textin(screen,400,320,'time: ' + str(runtime),25)
    textin(screen,400,190,'You Won',115)
    textbutt(screen,80,360,'playagain',50,250,70)
    textbutt(screen,500,360,' quit',50,150,70)
    while True:
        mouseClicked= False
        for event in pygame.event.get():
            if event.type==QUIT or (event.type== KEYUP and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEMOTION:
                cursorx, cursory= event.pos
            elif event.type== MOUSEBUTTONDOWN:
                cursorx, cursory= event.pos
                mouseClicked= True
                if 147<cursorx<297 and 369<cursory<447:
                    timeleft=(playtime-pygame.time.get_ticks())//1000
                    limeleftend=timeleft
                    runtime=(60-limeleftend)*1000
                    screen.fill(grey)
                    lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 503<cursorx<653 and 369<cursory<447:
                    pygame.quit()
                    quit()
                    sys.exit()              

    pygame.display.flip()
    pygame.time.wait(1000)
    timeleft+=runtime
def start():
    pygame.init()
    screen= pygame.display.set_mode((windowwidth, windowheight))
    screen.fill(grey)
    uncovered=[]
    textin(screen,400,190,'Pair Game',115)
    textbutt(screen,147,369,'play',70,150,78)
    textbutt(screen,503,369,'quit',70,150,78)    
    pygame.display.flip()
    while True:
        mouseClicked= False
        for event in pygame.event.get():
            if event.type==QUIT or (event.type== KEYUP and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEMOTION:
                cursorx, cursory= event.pos
            elif event.type== MOUSEBUTTONDOWN:
                cursorx, cursory= event.pos
                mouseClicked= True
                if 147<cursorx<297 and 369<cursory<447:
                    screen.fill(grey)
                    lvlone(screen,clickoneicon,uncoverd,runtime,limeleftend,uncovered)
                elif 503<cursorx<653 and 369<cursory<447:
                    pygame.quit()
                    quit()
                    sys.exit()
start()