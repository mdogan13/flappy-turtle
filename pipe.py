import turtle


class Pipe:

    pipe = None
    isdown = None

    def __init__(self, isdown, offset, size):
        self.pipe = turtle.Turtle()
        self.size = size
        self.pipe.speed(0)
        self.pipe.shape("square")
        self.pipe.color("green")
        self.pipe.shapesize(stretch_wid=self.size, stretch_len=1)
        self.pipe.penup()

        self.isdown = isdown

        if isdown:
            self.pipe.goto(800+300*offset, -300 + (self.size * 20) / 2)
        else:
            self.pipe.goto(800+300*offset, 300 - (self.size * 20) / 2)

    def movePipe(self):
        x = self.pipe.xcor()
        x -= 2
        self.pipe.setx(x)


    def getTopY(self):
        if self.isdown:
            return self.size * 20 - 300
        else:
            return 300 - self.size * 20