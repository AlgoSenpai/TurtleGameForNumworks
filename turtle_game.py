# The Turtle game
# By Lilian Boinard

##################
#  PObj VERSION  #
##################

from ion import *
from time import *
from turtle import *
from random import *
from kandinsky import *

level = 1
trunkSpeed = 0.1

trunkPosition = 0

class newMap:
        
    def outlineScreen():
        # <MAP outline construction>
        fill_rect(0,20,51,3,(0,0,0))
        fill_rect(0,20,3,240,(0,0,0))
        fill_rect(50,0,4,23,(0,0,0))
        fill_rect(0,220,320,3,(0,0,0))
        fill_rect(50,0,270,3,(0,0,0))
        fill_rect(317,0,3,240,(0,0,0))
        fill_rect(0,230,320,30,(0,0,0))
        # </MAP outline construction>
                    
    def construct():
        global level
        global trunkSpeed
        trunkSpeed -= 0.025
        # <MAP grass,water construction>
        fill_rect(0,0,320,240,(10,80,15))
        fill_rect(70,0,20,240,(15,170,210))
        fill_rect(140,0,20,240,(15,170,210))
        fill_rect(210,0,20,240,(15,170,210))      
        fill_rect(240,105,10,10,(0,0,0))
        # </MAP graas,water construction>
        
        newMap.outlineScreen()
        
        if level == 1:
            draw_string("lvl:1",0,0)
        elif level == 2:
            draw_string("lvl:2",0,0)
        elif level == 3:
            draw_string("lvl:3",0,0)
        elif level > 3:
            newMap.winScreen()
        level += 1
        
    def winScreen():
        while 1:
            fill_rect(0,0,320,240,(225,225,255))
            newMap.outlineScreen()           
            while 1:
                draw_string("lvl:x",0,0)
                draw_string("Win !", 116,100)
                newTurtle.controlReload()
                if newTurtle.controlReload():
                    break
            break
                
    def overScreen():
        while 1:
            fill_rect(0,0,320,240,(125,24,24))
            newMap.outlineScreen()
            while 1:
                draw_string("lvl:x",0,0)
                draw_string("Game over", 116,100)
                if newTurtle.controlReload():
                    break
            break
     
    def invokeTrunks(self):
        global trunkSpeed
        global trunkPosition
        trunkPosition += 10
        fill_rect(75,trunkPosition,10,60,(80,70,25))
        fill_rect(145,trunkPosition,10,60,(80,70,25))
        fill_rect(215,trunkPosition,10,60,(80,70,25))
        sleep(trunkSpeed)
        fill_rect(75,trunkPosition,10,10,(15,170,210))
        fill_rect(145,trunkPosition,10,10,(15,170,210))
        fill_rect(215,trunkPosition,10,10,(15,170,210))
            
class newTurtle:
    def __init__(self, state, position):
        self.state = state
        self.position = position
        
    def turtleState(self, state):
        if state:
            showturtle()
        else:
            hideturtle()
        
    def invokeTurtle(self, position):
        penup()
        hideturtle()
        speed(10)
        goto(position[0],position[1])
        setheading(0)        
        showturtle()
        
    def control(self):
        if keydown(KEY_RIGHT):
            forward(10)
            
    def controlReload():
        global level
        global trunkSpeed
        if keydown(KEY_BACKSPACE):
            level = 1
            trunkSpeed = 0.1
            newMap.construct()
            theTurtle.invokeTurtle([-140,1])
            return True
        else:
            return False
        
    def getPosition(self, position):
        global level
        if position == (-80.0,1.0):
            if get_pixel(75,105) == (8,168,208):
                newMap.overScreen()
        elif position == (-10.0,1.0):
            if get_pixel(75,105) == (8,168,208):
                newMap.overScreen()
        elif position == (60.0,1.0):
            if get_pixel(75,105) == (8,168,208):
                newMap.overScreen()
        elif position == (90.0,1.0):
            newMap.construct()
            self.invokeTurtle([-140,1])
            
theMap = newMap(0)
newMap.construct()

theTurtle = newTurtle(0,[])
theTurtle.invokeTurtle([-140,1])
theTurtle.turtleState(1)
while 1:
    trunkPosition = 0
    while trunkPosition != 240:
        theMap.invokeTrunks()
        theTurtle.control()
        theTurtle.getPosition(position())
