from turtle import Turtle
COLOR = "white"

class Midfield(Turtle):
  def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
    super().__init__(shape, undobuffersize, visible)
    self.hideturtle()
    self.pencolor(COLOR)
    self.width(5)
    self.create_midfield()

  def create_midfield(self):

    self.up()
    self.goto(0, -300)
    self.down()
    self.setheading(90)
    while self.ycor() < 300:
      self.forward(10)
      self.up()
      self.forward(10)
      self.down()