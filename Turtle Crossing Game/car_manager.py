from turtle import Turtle
import random

COLOURS = ["red", "blue", "orange", "yellow", "green", "purple"]


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_speed = 5

    def creat_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            new_car.goto(300, random.randint(-230, 230))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.starting_speed)
            
    def speed_up(self):
        self.starting_speed += 10


    