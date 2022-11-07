import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
SPEED = 5


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.seth(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=350, y=random.randint(-10, 10)*20)

    def drive(self):
        self.fd(SPEED)
