from turtle import Screen
from midfield import Midfield
from paddle import User, User2, Opponent
import time

is_game_on = True

screen = Screen()
screen.setup(900, 600, 2500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

midfield = Midfield()

player1_paddle = User()

# player2_paddle = User2()

cpu_paddle = Opponent()

screen.listen()
screen.onkey(player1_paddle.move_up, "w")
screen.onkey(player1_paddle.move_down, "s")
# screen.onkey(player2_paddle.move_up, "Up")
# screen.onkey(player2_paddle.move_down, "Down")

while is_game_on:
  screen.update()
  time.sleep(0.1)


screen.exitonclick()