from turtle import Turtle


class Writing(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(180)
        self.penup()
        self.color('black')
        self.hideturtle()

    def scores(self, level):
        self.goto(x=-150, y=250)
        self.write(f'Level: {level}', align='center', font=('Comic Sans MS', 16, 'normal'))

    def loser(self, score):
        self.goto(x=0, y=0)
        self.write(f'You lose! Your score is {score}', align='center', font=('Comic Sans MS', 24, 'normal'))


class Liners(Turtle):
    def __init__(self):
        super().__init__()
        self.seth(180)
        self.penup()
        self.color('black')
        self.hideturtle()

    def lines(self):
        for _ in range(-11, 11):
            self.goto(x=350, y=_*20+10)
            self.pendown()
            self.fd(800)
            self.penup()

