from turtle import Screen
from time import sleep
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.new_segment()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        snake.reset()

    #detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.game_over()
            snake.reset()






screen.exitonclick()