from turtle import Turtle
COLOR = 'green'


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.shape('turtle')
        self.goto(x=0, y=-250)
        self.seth(90)

    def movement(self):
        self.fd(20)

    def winning(self):
        if self.ycor() > 240:
            self.goto(x=0, y=-250)
            return 1
        else:
            return 0

    def crashing(self, car):
        if self.distance(car) < 30:
            return False
        else:
            return True