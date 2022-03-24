from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

def go_up():
  paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def go_down():
  paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.exitonclick()