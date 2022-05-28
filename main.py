from turtle import Screen
from food import Food
from scoreBoard import Score
import time
from snake import Snake

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True


while game_is_on:

    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect food collection
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # detect walll touch
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.ended()

    # head touched
    for segment in snake.statement[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.ended()

screen.exitonclick()
