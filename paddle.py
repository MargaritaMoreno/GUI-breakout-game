from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.color("#865DFF")
        self.penup()
        self.goto(position)
        self.speed = 2
        
        
    def right(self):
        new_x = self.xcor() + 15
        self.goto(new_x,self.ycor())
     
        
    def left(self):
        new_x = self.xcor() - 15
        self.goto(new_x,self.ycor())
    
    
    def reset_paddle(self,position):
        self.goto(position)
