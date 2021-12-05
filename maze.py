import turtle
screen = turtle.Screen()
screen.setup(400,400)

t=turtle.Turtle()
turtle.title("maze")
turtle.shape("turtle")
turtle.bgcolor("white")

turtle.done()

X=0
Y=1
cubesize=20

maze=[
    [1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,1],
    [1,1,0,1,1,0,0,0,1,1],
    [1,1,0,1,1,1,1,0,1,1],
    [1,1,0,1,1,1,1,0,1,1],
    [1,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,0,0,1,1],
    [1,0,0,0,0,0,0,1,1,1],
    [1,0,1,0,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,1,1],
    [1,0,1,1,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,0,1,1],
    [1,1,1,1,1,1,1,0,1,1]]
mazelen = len(maze)


def getx(x):
    global cubesize
    global mazelen
    return (x-mazelen/2)*cubesize

def gety(y):
    global cubesize
    global mazelen
    return -(y-mazelen/2)*cubesize

def draw_wall(x,y):
    x=getx(x)
    y=gety(y)
    t.penup()
    t.goto(x,y)

def draw_maze(maze):
    t.penup()
    t.goto(getx(0),gety(0))
    t.pendown()

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if(maze[y][x]==1):
                draw_wall(X,Y)

def isWin(x,y):
    print("x",x,"y",y)
    if(x==8):
        if(y==9):
            t.write("you win")

def turn_right():
    global maze
    global X
    global Y
    if(X<9):
        if(maze[Y][X+1]==0):
            X=X+1
            t.seth(0)
            t.goto(getx(X),gety(Y))
            isWin(X,Y)

def turn_left():
    global maze
    global X
    global Y
    if(X>0):
        if(maze[Y][X-1]==0):
            X=X-1
            t.seth(180)
            t.goto(getx(X),gety(Y))
            isWin(X,Y)
