from turtle import Screen, Turtle
import time
from food import Food
from Snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


x_axis = [0, -20, -40]
segment = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.mark_score()

    # detect collision with wall

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:

        scoreboard.reset()
        snake.reset()

    # detect collision with wall
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    # if head collides with any tail
    # trigger game_over










screen.exitonclick()