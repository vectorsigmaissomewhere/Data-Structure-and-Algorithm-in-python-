#There is my unsolved solution 
#it is already solved but I haven't tried it yet
#DRAWING A RECURSIVE SPIRAL USING TURTLE

import turtle

myTurtle=turtle.Turtle()
myWin=turtle.Screen()

def drawSpiral(myTurtle,lineLen):
    if lineLen >0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
drawSpiral(myTurtle,100)
myWin.exitonclick()


#RECURSIVELY DRAWING A TREE
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t) #this is the first recursion
        t.left(40)
        tree(branchLen-15,t) #this is the second recursion 
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()


main()
