import turtle
from turtle import*
from random import randint

#Screen Design 

sc = turtle.Screen()
sc.title("Turtle Race Project")

###########################
speed(10)
penup()
goto(-140,140)

#Map Design

for step in range(16):
    write(step , align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

#Turtle Design Red

leo = Turtle()
leo.color("red")
leo.shape("turtle")
    
leo.penup()
leo.goto(-160,100)
leo.pendown()

#Turtle Design Pink


sam = Turtle()
sam.color("pink")
sam.shape("turtle")
    
sam.penup()
sam.goto(-160,70)
sam.pendown()

#Turtle Design Purple

alysa = Turtle()
alysa.color("purple")
alysa.shape("turtle")
    
alysa.penup()
alysa.goto(-160,40)
alysa.pendown()

#Turtle Design Blue

bob = Turtle()
bob.color("blue")
bob.shape("turtle")
    
bob.penup()
bob.goto(-160,10)
bob.pendown()


#Turtle Speed

for turn in range(100):
    leo.forward(randint(1,5))
    sam.forward(randint(1,5))
    alysa.forward(randint(1,5))
    bob.forward(randint(1,5))
