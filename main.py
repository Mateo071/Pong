from turtle import Screen
from midfield import Midfield

screen = Screen()
screen.setup(900, 600, 2500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

midfield = Midfield()


screen.exitonclick()