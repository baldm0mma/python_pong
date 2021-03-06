from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_SLEEP_INTERVAL = 0.05

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)

scoreboard = Scoreboard()

left_paddle = Paddle(-(SCREEN_WIDTH / 2 - 50))
right_paddle = Paddle(SCREEN_WIDTH / 2 - 50)

ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

sleep_interval = STARTING_SLEEP_INTERVAL

while game_is_on:
    time.sleep(sleep_interval)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > SCREEN_HEIGHT / 2 - 20 or ball.ycor() < -(SCREEN_HEIGHT / 2 - 20):
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(left_paddle) < 60 and ball.xcor() < -(SCREEN_WIDTH / 2 - 75) or ball.distance(right_paddle) < 60 and ball.xcor() > SCREEN_WIDTH / 2 - 75:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.reset_ball()
        scoreboard.update_score("left")
        sleep_interval /= 1.25

    # Detect left paddle miss
    if ball.xcor() < -(SCREEN_WIDTH / 2):
        ball.reset_ball()
        scoreboard.update_score("right")
        sleep_interval /= 1.25

screen.exitonclick()
