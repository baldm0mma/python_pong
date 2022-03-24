from turtle import Turtle


class Paddle:
    def __init__(self, starting_x_position):
        self.starting_x_position = starting_x_position
        self.paddle = self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color("white")
        paddle.penup()
        paddle.goto(self.starting_x_position, 0)
        return paddle

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
