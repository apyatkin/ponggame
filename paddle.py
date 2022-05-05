from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x = x_cor
        self.y = y_cor
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, self.y)

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.x, self.ycor() + 30)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.x, self.ycor() - 30)
