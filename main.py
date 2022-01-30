from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong Game")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(key="Up", fun=r_paddle.move_upward)
s.onkey(key="Down", fun=r_paddle.move_downward)

s.onkey(key="w", fun=l_paddle.move_upward)
s.onkey(key="s", fun=l_paddle.move_downward)


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    s.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_with_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() < 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_with_paddle()

    if ball.xcor() > 370:
        ball.refresh_ball()
        score.l_point()

    if ball.xcor() < -370:
        ball.refresh_ball()
        score.r_point()


s.exitonclick()
