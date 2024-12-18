from turtle import Turtle
L_STARTING_SCORE = 0
R_STARTING_SCORE = 0
ALIGNMENT = "center"
SCORE_FONT = ("Arial", 64, "bold")
END_FONT = ("Arial", 64, "bold")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.up()
    self.goto(0, 200)
    self.l_score = L_STARTING_SCORE
    self.r_score = R_STARTING_SCORE
    self.update_score(L_STARTING_SCORE, R_STARTING_SCORE)

  def update_score(self, l_new, r_new):
    self.clear()
    self.l_score += l_new
    self.r_score += r_new
    self.write(f"{self.l_score} : {self.r_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)