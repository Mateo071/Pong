from turtle import Turtle
import time
COLOR = "white"
STARTING_COORDINATES = (-400, 0)
P2_STARTING_COORDINATES = (400, 0)

class Paddle(Turtle):
  def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
    super().__init__(shape, undobuffersize, visible)
    self.color(COLOR)
    self.up()
    self.setheading(90)
    self.shapesize(stretch_wid=0.8, stretch_len=4, outline=None)




class User(Paddle):
  def __init__(self, shape="square", undobuffersize=1000, visible=True):
    super().__init__(shape, undobuffersize, visible)
    self.goto(STARTING_COORDINATES)

  def move_up(self):
    if self.ycor() < 260:
      self.forward(10)

  def move_down(self):
    if self.ycor() > -260:
      self.back(10)
    

class User2(Paddle):
  def __init__(self, shape="square", undobuffersize=1000, visible=True):
    super().__init__(shape, undobuffersize, visible)
    self.goto(P2_STARTING_COORDINATES)

  def move_up(self):
    if self.ycor() < 260:
      self.forward(10)

  def move_down(self):
    if self.ycor() > -260:
      self.back(10)

class Opponent(Paddle):
  def __init__(self, shape="square", undobuffersize=1000, visible=True):
    super().__init__(shape, undobuffersize, visible)
    self.goto(P2_STARTING_COORDINATES)
    # for _ in range(1, 26):
    #   if self.ycor() > -260:
    #     self.back(10)
    # while self.ycor() >= -260:
    #   self.back(10)
    #   time.sleep(0.1)
    # while self.ycor() <= 260:
    #   self.forward(10)
    #   time.sleep(0.1)