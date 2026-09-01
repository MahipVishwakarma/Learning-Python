from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creat_car()
    car_manager.move_car()

    if player.ycor() > 280:
        player.advance()
        scoreboard.increase_score()
        car_manager.speed_up()

    if scoreboard.score > 5:
        scoreboard.win()
        game_is_on = False

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
