from turtle import Screen, Turtle, color
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

lives = 3
game = True
screen = Screen()
screen.bgcolor("#191825")
screen.setup(width=880, height=600)
screen.title("Breakout game")
screen.tracer(0)
turtle = Turtle()

ball = Ball()

paddle = Paddle((0,-250))
bricks = Bricks()
score = Scoreboard()

bricks.create_bricks()

screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

while game:
    
    turtle.clear()
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.color("white")
    turtle.write(f"Lives: {lives}", move=False, align="center", font=("Courier", 14, "normal"))
    
    time.sleep(0.06)
    screen.update()
    ball.move()
   
    if ball.ycor() > 280 or ball.distance(paddle) < 50:
        ball.bounce_y()
        
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.bounce_x()   
    
    for brick in bricks.bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            bricks.bricks.remove(brick)
            brick.hideturtle()
            actual_score = score.point()
            if actual_score == 24:
                turtle.color("white")
                turtle.write("Winner", move=False, align="center", font=("Roboto Condensed", 54, "bold")) 
                game = False   
    
    if ball.ycor() < -280:
       ball.reset_position()
       paddle.reset_paddle((0,-250))
       lives -= 1
       if lives == 0:
            turtle.clear()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.color("white")
            turtle.write("Game Over", move=False, align="center", font=("Roboto Condensed", 54, "bold"))
            game = False

    if paddle.xcor() > 400:
        paddle.goto(400, paddle.ycor())
    elif paddle.xcor() < -400:
        paddle.goto(-400, paddle.ycor())
          
        
screen.exitonclick()