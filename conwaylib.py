from random import randint

class conway:
  def __init__(self,row,col,state):
    self.store = []
    self.row = row
    self.col = col
    if state == 'zeros':
      for i in range(0,row):
        self.store.append([0]*col)
    elif state == 'random':
      for i in range(0,row):
        newrow = []
        for j in range(0,col):
          newrow = newrow + [randint(0,1)]
        self.store.append(newrow)
        
  def getDisp(self):
    #converting the above list to a string
    accum = ""
    for i in range(0,len(self.store),1):
      for j in range(0,len(self.store[i]),1):
        if self.store[i][j] == 0:
          accum = accum + " "
        elif self.store[i][j] == 1:
          accum = accum + "*"
        if j == len(self.store[i])-1:
          accum = accum + "\n"
    return accum
    
  def printDisp(self):
    #printing the string, which represents the game board
    try:
      print self.getDisp()
      return True
    except:
      return False
  
  def setPos(self,row,col,val):
    if val == 0 or val == 1:
      self.store[row][col] = val
      return True
    else:
      return False
  
  def getNeighbours(self,row,col):
    neighbours = []
    if row == 0:
      top = self.row - 1
      bottom = row + 1
      if col == 0:
        left = self.col - 1
        right = col + 1
      elif col = self.col - 1:
        left = col - 1
        right = 0
      else:
        left = col - 1
        right = col + 1
    elif row == self.row - 1:
      top = row - 1
      bottom = 0
      if col == 0:
        left = self.col - 1
        right = col + 1
      elif col == self.col - 1:
        left = col - 1
        right = 0
      else:
        left = col - 1
        right = col + 1
    else:
      top = row - 1
      bottom = row + 1
      if col == 0:
        left = self.col - 1
        right = col + 1
      elif col == self.col - 1:
        left = col - 1
        right = 0
      else:
        left = col - 1
        right = col + 1
    return [self.store[top][left],self.store[top][col],self.store[top][right],
            self.store[row][left],self.store[row][right],self.store[bottom][left],
            self.store[bottom][col],self.store[bottom][right]]
  
  def evolve(self,rule):
    nextstate = []
    r = self.row
    c = self.c
    for i in range(0,r):
      next.append([0]*c)
    for i in range(0,r):
      for j in range(0,c):
        next[i][j] = rule(self.store[i][j],self.getNeighbours(i,j))
    for i in range(0,r):
      for j in range(0,c):
        self.setPos(i,j,next[i][j])
    return True
