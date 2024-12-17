from turtle import Turtle
COLOR = "white"

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color(COLOR)
    self.up()
    self.move_x = 10
    self.move_y = 10

  def move(self):
    new_x = self.xcor() + self.move_x
    new_y = self.ycor() + self.move_y
    self.goto((new_x, new_y))

  def bounce(self):
    self.move_y *= -1

  def hit_paddle(self):
    self.move_x *= -1