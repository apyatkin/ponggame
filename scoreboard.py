from turtle import Turtle
FONT = ('arial', 20, 'bold')
ALIGMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Left: {self.score_left}  Right: {self.score_right}", move=False, align=ALIGMENT, font=FONT)

    def right_score(self):
        self.score_right += 1
        self.clear()
        self.update_score()

    def left_score(self):
        self.score_left += 1
        self.clear()
        self.update_score()

