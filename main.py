from turtle import Screen
from midfield import Midfield
from paddle import Paddle
from ball import Ball
import time

is_game_on = True

screen = Screen()
screen.setup(900, 600, 2500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

midfield = Midfield()
r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while is_game_on:
  screen.update()
  ball.move()
  if ball.ycor() >= 290 or ball.ycor() <= -290:
    ball.bounce()
  if ball.distance(r_paddle.position()) <= 10 or ball.distance(l_paddle.position()) <= 10:
    ball.hit_paddle()
  time.sleep(0.1)


screen.exitonclick()