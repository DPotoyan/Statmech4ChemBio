# Oirignal code by David Ji 
# Modified by Davit Potoyan

from tkinter import *
import numpy as np
from numpy.random import choice, uniform
import random
import copy
import scipy.special
import math

class Ball:

    def __init__(self, speed, col): #random initialization

        self.x = random.randint(50,350) + choice((0,400))
        self.y = random.randint(50,550)
        phase1 = uniform(30,55)/180.0
        phase = (choice((1,2,3,4))/2.0 + phase1)*math.pi
        self.dx = math.cos(phase)*speed
        self.dy = math.sin(phase)*speed
        self.radius = 10 
        self.color = col

def drawSplashScreen(): #draws the splash screen with four boxes

    inc=cd.boxSize*2/3
    canvas.create_text(cd.width/2,cd.border,text="MAXWELL'S DEMON",
                       font="Helvetica 24",)
    canvas.create_oval(cd.border,cd.border,cd.border*2,cd.border*2,fill="red"
                       ,width=0)
    canvas.create_oval(cd.width-cd.border,cd.border,cd.width-cd.border*2,
                       cd.border*2,fill="blue", width=0)
    leftX=cd.width/2-cd.boxSize
    rightX=cd.width/2+cd.boxSize
    topY=cd.boxSize/2
    botY=cd.boxSize
    for incNum in np.arange(cd.menus): #creates the rectangles for the splashscreen
        canvas.create_rectangle(leftX, topY+inc*incNum,rightX,botY+inc*incNum,
                                fill= "gray")
    canvas.create_text(cd.width/2,cd.boxSize*.75,text="Information",
                       font="Helvetica 24")
    canvas.create_text(cd.width/2,cd.boxSize*.75+inc,text="Sandbox",
                       font="Helvetica 24")
    canvas.create_text(cd.width/2,cd.boxSize*.75+inc*2,text="Play",
                       font="Helvetica 24")
    canvas.create_text(cd.width/2,cd.boxSize*.75+inc*cd.lastMenu, text="Demo",
                       font="Helvetica 24")

def mousePressed(event):#mouse only works for the splash screen sets the
    #game mode for clicking on the respective box
    inc=cd.boxSize*2/3
    leftX=cd.width/2-cd.boxSize
    rightX=cd.width/2+cd.boxSize
    topY=cd.boxSize/2
    botY=cd.boxSize
    if cd.isSplashScreen:
        if event.x>leftX and event.x<rightX:
            if event.y<botY and event.y>topY:
                cd.gameMode="info"
                cd.isSplashScreen=False
            elif event.y<botY+inc and event.y>topY+inc:
                cd.gameMode="sandbox"
                cd.isSplashScreen=False
            elif event.y<botY+inc*2 and event.y>topY+inc*2:
                startGameNorm()
                cd.gameMode="normal"
                cd.isSplashScreen=False
                cd.gameTime=cd.gameTimeDef
            elif event.y<botY+inc*cd.lastMenu and event.y>topY+inc*cd.lastMenu:
                startGameDemo()
                cd.gameMode="demo"
                cd.isSplashScreen=False
                cd.gameTime=cd.gameTimeDef
    
def drawInformation():#Information on Maxwell's Demon/the project in general
    canvas.create_text(cd.width/2,cd.border,text="MAXWELL'S DEMON",
                       font="Helvetica 24",)
    canvas.create_oval(cd.border,cd.border,cd.border*2,cd.border*2,fill="red"
                       ,width=0)
    canvas.create_oval(cd.width-cd.border,cd.border,cd.width-cd.border*2,
                       cd.border*2,fill="blue", width=0)
    mes="Maxwell's Demon is a physics thought experiment about the second " \
         +"law of \nthermodynamics demonstrating how it could hypothetically"\
         +" be violated.\nThis program includes three game modes: Sandbox, "\
         +" Play, and Demo.\n"\
         +" \nPress 'Esc' to return to the main menu."\
         +" \n\nSandbox:\nPress 'a' to"\
         +" add a pair of balls,"\
         +" 'b' to remove a pair of balls, or the 'space bar'\nto open/close "\
         +"the door."\
         +"\n \nPlay: \nThe goal of the game will be for you to try to get"\
         +" all of the balls of each \ncolor on their respective sides with"\
         +" the door closed. Press the 'space bar' \nto open/close the door."\
         +"\n\nDemo: "\
         +"\nThe game is played by computer using AI algorithm."
    canvas.create_text(cd.width/2,cd.height/2,text=mes,
                       font="Arial 24")
    
def addBallPair():#adds a pair of balls(different colors) to the board
    cd.ballList.append(Ball(10.0,"red"))
    cd.ballList.append(Ball(9.0,"blue"))

def removeBallPair():#removes a pair of balls (last ones added) from the board
    #(only available in sandbox mode
    if len(cd.ballList)==0:
        print("Ball list is empty")
    else:
        cd.ballList.pop()
        cd.ballList.pop()

def keyPressed(event):#keys only work during a game
    if event.keysym=="Escape":
        cd.isSplashScreen=True
        cd.ballList=[]
    elif not cd.isSplashScreen:
        if cd.gameMode=="sandbox":
            if event.char=="a":
                addBallPair()
            elif event.char=="b":
                removeBallPair()
            elif event.keysym=="space":
                cd.doorIsOpen= not cd.doorIsOpen
        elif cd.gameMode=="normal":
            #print "Normal Mode"
            if event.keysym=="space" and not cd.gameWon:
                cd.doorIsOpen= not cd.doorIsOpen
    redrawAll()

def timerFired():
    redrawAll()
    cd.gameTime-=cd.delay*2
    canvas.after(cd.delay, timerFired) # pause, then call timerFired again

def redrawAll():#draws the necessary 
    canvas.delete(ALL)
    if cd.isSplashScreen:
        drawSplashScreen()
    else:
        if cd.gameMode=="info":
            drawInformation()
        elif cd.gameMode=="sandbox":
            drawBoard()
            drawBalls()
        elif cd.gameMode=="normal":
            drawBoard()
            drawBalls()
            drawTimer()
            displayEntropy()
            if cd.gameWon:
                drawWinner()
            elif cd.gameTime<0:
                drawLoser()
        elif cd.gameMode=="demo":
            WantdoorOpen = useAI()
            if cd.doorIsOpen == True:
                if WantdoorOpen == True:
                    cd.doordelay -= 1
                elif cd.doordelay > 0:
                    cd.doordelay -= 1
                else:
                    cd.doorIsOpen = False
                    cd.doordelay = 5 
                    
            if cd.doorIsOpen == False:
                if WantdoorOpen == False:
                    cd.doordelay -= 1
                elif cd.doordelay > 0:
                    cd.doordelay -= 1
                else:
                    cd.doorIsOpen = True
                    cd.doordelay = 5 
                
            drawBoard()
            drawBalls()
            drawTimer()
            displayEntropy()
            if cd.gameWon:
                drawWinner()
            elif cd.gameTime<0:
                drawLoser()
    
def drawTimer():#draws the timer if the time is greater than 0
    if cd.gameTime>0:
        minutes=int(cd.gameTime/1000/60)
        seconds=int(cd.gameTime/1000%60)
        if seconds>9:
            canvas.create_text(cd.width/3,cd.border,text="Time Remaining: "\
                               +str(minutes)+":"+str(seconds),
                               font="Arial 24")
        else:
            canvas.create_text(cd.width/3,cd.border,text="Time Remaining: "\
                               +str(minutes)+":0"+str(seconds),
                               font="Arial 24")
            
def displayEntropy():#display the entropy number
    if cd.gameTime>0:
        #entropy = 0.0
        canvas.create_text(2*cd.width/3,cd.border,text="Entropy = "\
                               + "%.2f" % round(cd.entropy,2) + " bit",
                               font="Arial 24")
            
def drawLoser():#draws losing screen
    canvas.create_rectangle(cd.width/4,cd.height/4,cd.width*3/4,cd.height*3/4,
                            fill= "white")
    canvas.create_text(cd.width/2,cd.height/2, text="Sorry You Lose!"+
                       "\nPress Esc to go to the menu",
                       font="Helvetica 24")

def drawWinner():#draws winning screen
    canvas.create_rectangle(cd.width/4,cd.height/4,cd.width*3/4,cd.height*3/4,
                            fill= "white")
    canvas.create_text(cd.width/2,cd.height/2, text="Congratulations You Win!"+
                       "\nPress Esc to go to the menu",
                       font="Helvetica 24")

def startGameDemo():#Creates game with a demo amount of balls
    cd.ballList=[]
    for numPairs in np.arange(cd.demo):
        addBallPair()

def startGameNorm():#Creates game with a normal amount of balls
    cd.ballList=[]
    for numPairs in np.arange(cd.norm):
        addBallPair()

#draws the board
def drawBoard():
    canvas.create_rectangle(0, 0, cd.wall, cd.height, fill="red", width=0)
    canvas.create_rectangle(cd.width-cd.wall, 0, cd.width, cd.height,
                            fill="blue", width=0)
    canvas.create_rectangle(0, 0, cd.width/2, cd.wall, fill="red", width=0)
    canvas.create_rectangle(0, cd.height-cd.wall, cd.width/2, cd.height,
                            fill="red", width=0)
    canvas.create_rectangle(cd.width/2,0,cd.width,cd.wall,fill="blue", width=0)
    canvas.create_rectangle(cd.width/2,cd.height-cd.wall,cd.width,cd.height,
                            fill="blue", width=0)
    canvas.create_rectangle((cd.width-cd.wall)/2, 0, (cd.width+cd.wall)/2,
                            200, fill="red", width=0)
    canvas.create_rectangle((cd.width-cd.wall)/2, 400, (cd.width+cd.wall)/2,
                            cd.height, fill="blue", width=0)
    if cd.doorIsOpen == False:
        canvas.create_rectangle((cd.width-cd.wall)/2, 200,
                                (cd.width+cd.wall)/2, 400, fill="lightblue")

def drawBalls():

    count=0.#count of balls that are in the right spot
    for ball in cd.ballList:
        if cd.doorIsOpen: redisplayBall_opendoor(ball)
        else: redisplayBall_closedoor(ball)

    red_left = 0
    red_right = 0
    blue_left = 0
    blue_right = 0
    for ball in cd.ballList:
        if ball.color=="red":
            if ball.x<= cd.width/2:
                red_left+=1
            else:
                red_right+=1
        else:
            if ball.x<= cd.width/2:
                blue_left+=1
            else:
                blue_right+=1  
    red_total = scipy.special.binom(red_left+red_right,red_left)
    blue_total = scipy.special.binom(blue_left+blue_right,blue_left)
    cd.entropy = math.log(red_total,2) + math.log(blue_total,2)
    
    if cd.gameMode=="normal" or cd.gameMode=="demo":
        if cd.doorIsOpen==False:
            won=True
            for ball in cd.ballList:
                if not isInRightSpot(ball):
                    won=False
            cd.gameWon=won

def redisplayBall_opendoor(ball):#checks if the ball is hitting the wall
    #and bounces it back if so
    if (ball.x) < (cd.width/2-cd.wall/2-ball.radius) and \
    (ball.x + ball.dx) > (cd.width/2-cd.wall/2-ball.radius) and \
    ((ball.y+ball.dy) < (200+cd.wall/2+ball.radius) or (ball.y+ball.dy) > \
    (400-ball.radius-cd.wall/2)): ball.dx = -ball.dx
    if (ball.x) > (cd.width/2+cd.wall/2+ball.radius) and \
    (ball.x + ball.dx) < (cd.width/2+cd.wall/2+ball.radius) and \
    ((ball.y+ball.dy) < (200+ball.radius+cd.wall/2) or (ball.y+ball.dy) > \
     (400-ball.radius-cd.wall/2)): ball.dx = -ball.dx
    elif (ball.x + ball.dx) < cd.wall+ball.radius: ball.dx = -ball.dx
    elif (ball.x + ball.dx) > (cd.width-cd.wall-ball.radius):ball.dx = -ball.dx
    elif (ball.y + ball.dy) > cd.height-cd.wall-ball.radius: ball.dy = -ball.dy
    elif (ball.y + ball.dy) < cd.wall+ball.radius: ball.dy = -ball.dy
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                            ball.x + ball.radius, ball.y + ball.radius,
                            fill = ball.color, width=0)

def redisplayBall_closedoor(ball):#checks if the ball is hitting the door or
    #the wall and bounces it back if so
    if (ball.x) < (cd.width/2-cd.wall/2-ball.radius) and \
    (ball.x + ball.dx) > (cd.width/2-cd.wall/2-ball.radius):
        ball.dx = -ball.dx
    elif (ball.x) > (cd.width/2+cd.wall/2+ball.radius) and \
    (ball.x + ball.dx) < (cd.width/2+cd.wall/2+ball.radius):
        ball.dx = -ball.dx  
    elif (ball.x + ball.dx) < cd.wall+ball.radius:
        ball.dx = -ball.dx
    elif (ball.x + ball.dx) > (cd.width-cd.wall-ball.radius):
        ball.dx = -ball.dx
    elif (ball.y + ball.dy) > cd.height-cd.wall-ball.radius:
        ball.dy = -ball.dy  
    elif (ball.y + ball.dy) < cd.wall+ball.radius:
        ball.dy = -ball.dy
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                       ball.x + ball.radius, ball.y + ball.radius,
                       fill = ball.color,width=0)
    
def isInRightSpot(ball):#checks if the ball is in the correct position

    if ball.color=="red":
        if ball.x<=(cd.width-cd.wall)/2:
            return True
        else:
            return False
    else:
        if ball.x>=(cd.width-cd.wall)/2:
            return True
        else:
            return False

def init():#initializes cd variables

    cd=canvas.data
    cd.width=800
    cd.height = 600
    cd.border=50
    cd.wall=10
    cd.doorIsOpen=True
    cd.ballList=[]
    cd.isSplashScreen=True
    cd.boxSize=175
    cd.gameMode=""
    cd.delay=20
    cd.delayDef=20
    cd.gameWon=False
    cd.norm=4
    cd.demo=8
    cd.menus=4
    cd.lastMenu=3
    cd.gameTime=120000
    cd.gameTimeDef=120000
    cd.tSize=100
    cd.doordelay=5

def useAI():
    ahead = 2
    decision = 0
    # print "use AI"
    for ball in cd.ballList:
        count = 0
        if (ball.x) < (cd.width/2-cd.wall/2-ball.radius) and \
        (ball.x + ball.dx) > (cd.width/2-cd.wall/2-ball.radius) and \
        ((ball.y+ball.dy) > (200+cd.wall/2+ball.radius) and (ball.y+ball.dy) < \
        (400-ball.radius-cd.wall/2)): 
            if ball.color=="red":
                count = -1
            else:
                count = 1
        if (ball.x) > (cd.width/2+cd.wall/2+ball.radius) and \
        (ball.x + ball.dx) < (cd.width/2+cd.wall/2+ball.radius) and \
        ((ball.y+ball.dy) > (200+ball.radius+cd.wall/2) and (ball.y+ball.dy) < \
        (400-ball.radius-cd.wall/2)): 
            if ball.color=="red":
                count = 1
            else:
                count = -1
        decision += count
    
    if decision > 0: X = True
    else: X = False   
    return X      
            
def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    # Set up canvas data and call init
    global cd
    class Struct: pass
    canvas.data = Struct()
    cd=canvas.data
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close
    #the window!)

run()
