from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]
Moved = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.seg = []
        self.createsnake()
        self.head = self.seg[0]


    def createsnake(self):
        for i in pos:
            tim = Turtle()

            tim.color('white')
            tim.shape('square')
            tim.penup()
            a = tim.goto(i)
            self.seg.append(tim)

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            x = self.seg[i - 1].xcor()
            y = self.seg[i - 1].ycor()
            self.seg[i].goto(x, y)
        self.head.forward(Moved)

    def addseg(self):
        for i in pos:
            tim = Turtle()

            tim.color('white')
            tim.shape('square')
            tim.penup()
            a = tim.goto(i)
            self.seg.append(tim)

    def reset(self):
        for i in self.seg:
            i.goto(1000,1000)
        self.seg.clear()
        self.createsnake()
        self.head = self.seg[0]


    def ext(self):
        self.addseg()


    def Up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def Down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def Left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def Right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
