import turtle
import random

def space(length):
    turtle.up()
    turtle.forward(length)
    turtle.down()

turtle.speed(5)

frame = int(input("Frame size: "))
grid = int(input("Complexity (smaller -> complex): "))
turtle.up()
turtle.goto(frame / -2, frame / -2)
turtle.down()

for x in range (4):
    for i in range (int(frame / grid)):
        if((x == 1 or x == 3) and (i == int(frame / grid / 2))):
            space(grid)
        else:
           turtle.forward(grid)
    turtle.left(90)
for y in range(2 * int(frame / grid)):
    if(y == frame / grid):
        space(grid)
        turtle.right(90)
    
    for i in range(int(frame / grid)):
        randomNum = random.randint(0, 9)
        if(randomNum >= 7):
            turtle.forward(grid)
        else:
            space(grid)
    if(y % 2 == 0):
        turtle.left(90)
        if(y == int(frame / grid / 2) - 1 or y == int(frame / grid / 2)):
            space(grid)
        else:
            turtle.forward(grid)
        turtle.left(90)
    else:
        turtle.right(90)
        if(y == int(frame / grid / 2) - 1 or y == int(frame / grid / 2)):
            space(grid)
        else:
            turtle.forward(grid)
        turtle.right(90)

##for x in range(1, 20):
##    turtle.circle(3 * x)
##    turtle.left(30)
    
##for x in range(4):
##    turtle.forward(80)
##    turtle.left(90)
##    for i in range(4):
##        turtle.forward(80)
##        for j in range(4):
##            turtle.forward(80)
##            turtle.left(60)
