from turtle import Turtle
COLOR = "white"

class Ball(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("circle")
    self.color(COLOR)
    self.up()
    self.goto(position)
    self.setheading(45)

  def move(self):
    self.forward(10)
    if self.hit_wall():
      prev_heading = self.heading()
      new_heading = prev_heading + 90
      self.setheading(new_heading)

  def hit_wall(self):
    x_cor = self.xcor()
    y_cor = self.ycor()

    if x_cor >= 440:
      return True
    elif x_cor <= -440:
      return True
    elif y_cor >= 290:
      return True
    elif y_cor <= -290:
      return True