from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(10)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def move_upward(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_downward(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
