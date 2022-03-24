from turtle import Turtle

# CONSTANTS
STARTING_PADDLE_LOCATION = {"x": 350, "y": 0}


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.paddle = self.create_paddle()

    def create_paddle(self):
        paddle = Turtle("square")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.color("white")
        paddle.penup()
        paddle_position = "-" if self.position == "left" else ""
        paddle.goto(int(f"{paddle_position}350"), 0)
        return paddle

    def move_up(self):

    def move_down(self):
