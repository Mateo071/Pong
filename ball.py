from turtle import Turtle
COLOR = "white"

class Ball(Turtle):
  def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
    super().__init__(shape, undobuffersize, visible)
    self.color(COLOR)

  def move(self):
    pass