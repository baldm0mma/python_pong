from turtle import Turtle


class Ball:
    def __init__(self):
        self.ball = self.create_ball()

    def create_ball(self):
        ball = Turtle("circle")
        ball.color("white")
        ball.penup()
        return ball

    def move(self):
        self.ball.goto(self.ball.xcor() + 10, self.ball.ycor() + 10)
