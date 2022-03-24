from turtle import Screen
from paddle import Paddle

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)

left_paddle = Paddle(-(SCREEN_WIDTH / 2 - 50))
right_paddle = Paddle(SCREEN_WIDTH / 2 - 50)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
  screen.update()

screen.exitonclick()