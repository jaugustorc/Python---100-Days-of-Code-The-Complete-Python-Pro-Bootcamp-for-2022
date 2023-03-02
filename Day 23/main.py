import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
scoreboard= Scoreboard()

# definindo os atalhos
screen.listen()
screen.onkey(player.go, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # cria carros aleatoriamente
    cars.creat_car()
    cars.go()

    #Detectar colisões
    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on=False

    # Detectar o fim
    if player.is_at_finish_line():
        player.go_to_start()
        cars.move_up()
        scoreboard.increase_level()



screen.exitonclick()