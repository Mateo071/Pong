from turtle import Turtle
COLOR = "white"
MOVE_DISTANCE = 20
P2_STARTING_COORDINATES = (-400, 0)
STARTING_COORDINATES = (400, 0)
UPPER_BOUND = 260
LOWER_BOUND = -260

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.color(COLOR)
    self.shape("square")
    self.up()
    self.setheading(90)
    self.shapesize(stretch_wid=0.8, stretch_len=4, outline=None)
    self.goto(position)

  def create_paddle(self):
    pass

  def move_up(self):
    if self.ycor() < UPPER_BOUND:
      self.forward(MOVE_DISTANCE)

  def move_down(self):
    if self.ycor() > LOWER_BOUND:
      self.back(MOVE_DISTANCE)