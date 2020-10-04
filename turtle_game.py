# The Turtle game
# By Lilian Boinard
from ion import *
from time import *
from turtle import *
from random import *
from kandinsky import *

# DON'T Touch ->
lvl = 0
vitesse = 0
# DON'T Touch ->

# MAP pixel construction ->
def constructMap():
  fill_rect(0,20,51,3,(0,0,0))
  fill_rect(0,20,3,240,(0,0,0))
  fill_rect(50,0,4,23,(0,0,0))
  fill_rect(0,220,320,3,(0,0,0))
  fill_rect(50,0,270,3,(0,0,0))
  fill_rect(317,0,3,240,(0,0,0))
# MAP pixel construction ->

# Control for forward ->
def control():
    showturtle()
    if keydown(KEY_RIGHT):
      setheading(0)
      forward(5)
      hideturtle()
# Control for forward ->

def mapReload():
  global lvl
  if keydown(KEY_BACKSPACE):
      lvl = 0
      theMap()

# Initialization of turtle ->    
def iniTurtle():
  penup()
  hideturtle()
  speed(10)
  goto(-140,1)
# Initialization of turtle ->

# Verification of position ->
# if the turtle is in the water
def over():
  if position() == (-80.0,1.0):
    if get_pixel(75,105) == (8,168,208):
      while 1:
        fill_rect(0,0,320,240,(125,24,24))
        constructMap()
        while 1:
          draw_string("lvl:x",0,0)
          draw_string("Game over", 116,100)
          mapReload()
  elif position() == (-10.0,1.0):
    if get_pixel(75,105) == (8,168,208):
      while 1:
        fill_rect(0,0,320,240,(125,24,24))
        constructMap()
        while 1:
          draw_string("lvl:x",0,0)
          draw_string("Game over", 116,100)
          mapReload()
  elif position() == (60.0,1.0):
    if get_pixel(75,105) == (8,168,208):
      while 1:
        fill_rect(0,0,320,240,(125,24,24))
        constructMap()
        while 1:
          draw_string("lvl:x",0,0)
          draw_string("Game over", 116,100)
          mapReload()
  elif position() == (85.0,1.0):
    theMap()
# Verification of position ->

# Main function ->
def theMap():
  global lvl
  lvl += 1
  p=0
  iniTurtle()
  fill_rect(0,0,320,240,(10,80,15))
  fill_rect(70,0,20,240,(15,170,210))
  fill_rect(140,0,20,240,(15,170,210))
  fill_rect(210,0,20,240,(15,170,210))
  constructMap()
  fill_rect(240,105,10,10,(0,0,0))
  
  fill_rect(0,230,320,30,(0,0,0))
  if lvl == 1:
    vitesse = 0.012 # editable
    draw_string("lvl:1",0,0)
  elif lvl == 2:
    vitesse = 0.010 # editable
    draw_string("lvl:2",0,0)
  elif lvl == 3:
    vitesse = 0.001 # editable
    draw_string("lvl:3",0,0)
  elif lvl == 4:
    while 1:
        fill_rect(0,0,320,240,(225,225,255))
        constructMap()
        while 1:
          draw_string("lvl:x",0,0)
          draw_string("Win !", 116,100)
  
  while 1:
    while p<240:
      control()
      over()
      p=p+10
      control()
      over()
      fill_rect(75,p,10,60,(80,70,25))
      fill_rect(145,p,10,60,(80,70,25))
      fill_rect(215,p,10,60,(80,70,25))
      control()
      over()
      sleep(vitesse)
      control()
      over()
      fill_rect(75,p,10,10,(15,170,210))
      fill_rect(145,p,10,10,(15,170,210))
      fill_rect(215,p,10,10,(15,170,210))
    p=0
# Main function ->

theMap() #go
  
