import turtle
screen = turtle.Screen()
screen.setup(400,400)

t=turtle.Turtle()
turtle.shape("turtle")
turtle.bgcolor("white")

x=0
y=1
cubesize= ?

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
