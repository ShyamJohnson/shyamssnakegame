from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import score
import time
snake = Snake()

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.listen()
fo = Food()
sc = score()
screen.onkey(snake.Up,'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left,'Left')
screen.onkey(snake.Right,'Right')
on = True
while on:
    screen.update()

    time.sleep(0.08)
    snake.move()
    if snake.head.distance(fo)<15:
        fo.refresh()
        snake.ext()
        sc.re()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        on = False
        sc.re()
        snake.reset()

    for i in snake.seg:
        if i == snake.head:
            pass
        elif snake.head.distance(i) < 10:
            on = False
            sc.re()
            snake.reset()


screen.exitonclick()