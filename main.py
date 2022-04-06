from scoreboard import Scoreboard
import difficult
from turtle import Screen
from snake import Snake
from food import Food
import time

# SCREEN SETTINGS
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('ALEXANDER ZHARYUK SNAKE GAME')
screen.tracer(0)
DIFFICULT = difficult.choose_difficulty()
difficult.ready_count()


snake = Snake()
food = Food()
score = Scoreboard()

# KEY BINDINGS
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(screen.bye, 'Escape')


# SNAKE MOVING
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(DIFFICULT)
    snake.move()

#     Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
#     Detect collision with wall
    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
        score.reset()
        snake.reset()

#     Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()

# END THE PROGRAM
screen.exitonclick()
