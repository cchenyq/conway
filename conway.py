from conwaylib import *
from random import randint
from time import sleep
from rule import rule
import os

row = 40  #board can be set to an arbitrary size
col = 30
c = conway(row,col,'zeros')

c.setPos(10,10,1)
c.setPos(9,10,1)
c.setPos(12,10,1)
c.setPos(10,9,1)
c.setPos(11,9,1)
c.setPos(10,11,1)
c.setPos(11,11,1)

c.setPos(10,20,1)
c.setPos(11,21,1)
c.setPos(12,19,1)
c.setPos(12,20,1)
c.setPos(12,21,1)

n = 0
while True:
  c.evolve(rule)
  os.system('clear')
  c.printDisp()
  print "Step: ",n
  sleep(0.1)  #change the size of the argument to speed up/slow down the simulation
  n = n+1
