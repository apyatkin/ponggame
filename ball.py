from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x = x_cor
        self.y = y_cor
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(self.x, self.y)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

