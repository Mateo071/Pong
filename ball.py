from turtle import Turtle
from math import sin, cos, radians
from random import randint, choice
COLOR = "white"
C = 16

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color(COLOR)
    self.up()
    self.move_x = 10
    self.move_y = 10
    self.move_speed = 0.1

  def move(self):
    new_x = self.xcor() + self.move_x
    new_y = self.ycor() + self.move_y
    self.goto((new_x, new_y))

  def bounce(self):
    self.move_y *= -1

  def hit_paddle(self):
    self.move_x *= -1
    self.move_speed *= 0.9

  def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.randomize_direction()

  def randomize_direction(self):
    random_angle = randint(30, 60)
    neutral_x = int(16*cos(radians(random_angle)))
    neutral_y = int(16*sin(radians(random_angle)))

    if self.move_x > 0:
      self.move_x = int(neutral_x * -1)
    else:
      self.move_x = int(neutral_x)


    self.move_y = int(neutral_y * choice([-1, 1]))
