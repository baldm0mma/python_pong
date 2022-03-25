from turtle import Turtle

# Constants
STARTING_SCORE = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = STARTING_SCORE
        self.right_score = STARTING_SCORE
        self.paint_to_screen()

    def paint_to_screen(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center",
                   font=("Ariel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center",
                   font=("Ariel", 60, "normal"))

    def update_score(self, side=None):
        if side == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.paint_to_screen()
