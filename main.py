import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

player_right = Paddle(350, 0)
player_left = Paddle(-350, 0)
ball = Ball(0, 0)
score = Scoreboard()

screen.listen()
screen.onkey(player_right.move_up, "Up")
screen.onkey(player_right.move_down, "Down")

screen.onkey(player_left.move_up, "w")
screen.onkey(player_left.move_down, "s")

game_is_on = True
start_speed = 0.1
while game_is_on:
    screen.update()
    time.sleep(start_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_right) < 50 and ball.xcor() > 320 or ball.distance(player_left) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_score()
        start_speed *= 0.9
        print(start_speed)

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_score()
        start_speed *= 0.9
        print(start_speed)
    if score.score_right > 9 or score.score_left > 9:
        game_is_on = False

screen.exitonclick()
