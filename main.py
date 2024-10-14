
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.segments[0].distance(food)<20:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        score.game_over()
        game_is_on=False

    for segment in snake.segments:
        if snake.segments[0].distance(segment)<5:
            game_is_on= False;
            score.game_over()







screen.exitonclick()

