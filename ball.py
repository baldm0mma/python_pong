from turtle import Turtle

# CONSTANTS
BALL_MOVEMENT = 5

class Ball(Turtle):
    def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("white")
      self.penup()
      self.x_move = BALL_MOVEMENT
      self.y_move = BALL_MOVEMENT

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
      self.y_move *= -1