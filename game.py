import turtle
import random
import pipe

wn = turtle.Screen()
wn.title("Flappy Turtle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
num_of_pipe_pairs = 50
score = 0
high_score = 0
pipes = []

# Bird
bird = turtle.Turtle("turtle")
bird.speed(0)
bird.color("white")
bird.penup()
bird.goto(0, 0)
# Pen to keep track of the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



def flap():
    y = bird.ycor()
    for i in range(1, 20):
        y += 3
        bird.sety(y)

def createPipePair(offset):
    mingap= 4
    maxgap=10
    gap = random.randint(mingap, maxgap)
    remainingspace=30-gap
    upsize = random.randint(1, remainingspace)
    downsize = remainingspace -upsize

    up = pipe.Pipe(False,offset,upsize)
    down = pipe.Pipe(True,offset,downsize)
    return [up, down]

def initPipes(num_of_pipe_pairs):
    for _ in range(0,num_of_pipe_pairs):
        pipes.append(createPipePair(_))

def movePipes():
    for pair in pipes:
        pair[0].movePipe()
        pair[1].movePipe()

def is_collided_with(b, pipepair):

    if b.ycor() > pipepair[0].getTopY() or b.ycor() < pipepair[1].getTopY():

        if abs(b.xcor()-pipepair[0].pipe.xcor()) < 20:

            return True
        else:
            return False
    else:
        return False

def checkCollision():

    counter = 0
    for i in range(len(pipes)):
        if is_collided_with(bird, pipes[i]):
            counter += 1
    if counter != 0:
        return True
    else:
        return False

def isPassedAPipe(b, pipepair):
    if abs(b.xcor()-pipepair[0].pipe.xcor())==0:
        return True
    else:
        return False

def increaseScore(pen):
    global score
    global high_score
    for i in range(len(pipes)):
        if isPassedAPipe(bird, pipes[i]):
           score += 10
           if score > high_score:
                high_score += 10
           pen.clear()
           pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def resetGame():
    bird.sety(0)
    bird.setx(0)
    global score
    score = 0
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



wn.listen()
wn.onkey(flap, "space")
initPipes(num_of_pipe_pairs)
collision_counter = 0

while True:
    wn.update()

    if checkCollision():
        collision_counter += 1
        if collision_counter > 1:
            resetGame()
    if bird.ycor() < -290: # collision check for ground
        resetGame()
    if bird.ycor() > 300: # collision check for ceiling
        bird.sety(bird.ycor()-20)
    else:
        y = bird.ycor()
        y -= 3
        bird.sety(y)

    increaseScore(pen)
    movePipes()

