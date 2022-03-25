from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_x_position):
        super().__init__()
        self.starting_x_position = starting_x_position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.starting_x_position, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
