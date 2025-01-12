from turtle import Turtle
Align = 'center'
Font = ('courier',20,'normal')
f = ('courier',30,'normal')
fF = ('courier',30,'normal')


class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        with open('data.txt') as f:
            self.highscore = int(f.read())
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}   HIGH SCORE : {self.highscore}",align=Align,font=Font)
    def incsco(self):
        self.score +=1

        self.write(f"Score : {self.score}",align=Align,font=Font)

    def re(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()


    '''def gameover(self):
        self.goto(0,0)
        self.write('Game Over',align=Align,font=f)
        self.goto(0,-50)
        self.write(f"Final score : {self.score}",align=Align,font=f)'''
