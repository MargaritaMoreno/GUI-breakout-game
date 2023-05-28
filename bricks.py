from turtle import Turtle

class Bricks:
    def __init__(self):
        self.bricks = []  
    

    def create_bricks(self):
        y_coordinate = 150  

        for _ in range(4):
            x_coordinate = -370  

            for _ in range(7):
                brick = Turtle()
                brick.shape("square")
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.color("#FFA3FD")
                brick.penup()
                brick.goto(x_coordinate, y_coordinate)  
                x_coordinate += 150  
                self.bricks.append(brick)  

            y_coordinate -= 50  
