from turtle import Turtle, position
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars=[]
        self.speed=STARTING_MOVE_DISTANCE

    def creat_car(self):
        chance=random.randint(1,6)
        if chance==6:
            car=Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            # determina o tamanho, é um elemento so
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            position_y=random.randint(-250,250)
            car.goto(x=300,y=position_y)
            self.all_cars.append(car)

    def go(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def move_up(self):
        self.speed+=MOVE_INCREMENT