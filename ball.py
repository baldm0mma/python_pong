from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
      super().__init__()
      self.ball = self.create_ball()

  def create_ball(self):
    ball = Turtle("circle")
    ball.color("white")
    return ball