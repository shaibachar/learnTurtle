from turtle import *
import turtle

print("position:", turtle.position())

turtle.forward(25)
print("position:", turtle.position())

turtle.forward(-75)
print("position:", turtle.position())

turtle.backward(-75)
print("position:", turtle.position())

turtle.backward(25)
print("position:", turtle.position())

print("heading:", turtle.heading()) # 0.0

turtle.left(90)
print("heading:", turtle.heading()) # 90.0

turtle.left(90)
print("heading:", turtle.heading()) # 180.0

turtle.left(90)
print("heading:", turtle.heading()) # 270.0

turtle.left(90)
print("heading:", turtle.heading()) # 360.0 || 0.0

turtle.right(90)
print("heading:", turtle.heading()) # 270.0

turtle.right(90)
print("heading:", turtle.heading()) # 180.0

turtle.right(90)
print("heading:", turtle.heading()) # 90.0

turtle.right(90)
print("heading:", turtle.heading()) # 360.0 || 0.0

