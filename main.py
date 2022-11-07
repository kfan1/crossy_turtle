import time
from turtle import Screen

import cars
from turtles import Timmy
from cars import *
from score_and_lines import Writing, Liners

screen = Screen()
screen.setup(height=600, width=600)
screen.title('Crossy Turtle')
screen.tracer(0)
timmy = Timmy()
car = []
writing = Writing()
liners = Liners()
liners.lines()
screen.onkey(timmy.movement, 'Up')

score = 1
i = 0
game_on = True
while game_on:
    writing.clear()
    writing.scores(score)
    screen.listen()
    screen.update()
    time.sleep(0.1)
    if i%10 == 0:
        car.append(Cars())
    for _ in range(len(car)):
        car[_].drive()
        token = timmy.crashing(car[_])
        if not token:
            game_on = False
    i += 1
    if timmy.winning() == 1:
        score += 1
        cars.SPEED *= 1.1

writing.loser(score)


screen.exitonclick()
