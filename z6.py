#
# from turtle import *
# k = 30
# tracer(0)
# pendown()
# for i in range(24):
#     forward(3*k)
#     left(60)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x*k, y*k)
#         dot(2)
# done()

# from turtle import *
# k = 100
# tracer(0)
# pendown()
# begin_fill()
# for i in range(6):
#     forward(3*k)
#     left (60)
# end_fill()
# penup()
# count = 0
# canvas = getcanvas()
# for x in range(-15, 15):
#     for y in range(-15, 15):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k ,) == (5 ,):
#             count += 1
# print(count)
# done()

# from turtle import *
# k = 20
# left(90)
# tracer(0)
# screensize( 3090,  2000)
# pendown()
# for i in range(9):
#     forward(7 * k)
#     right(90)
#     forward(42 * k)
#     right(90)
# penup()
# backward(10*k)
# left(90)
# backward(16*k)
# pendown()
# for i in range(9):
#     forward(42*k)
#     right(90)
#     forward(16*k)
#     right(90)
# penup()
# for x in range(-10,100):
#     for y in range(-10,100):
#         setpos(x*k,y*k)
#         dot()
# done()

from math import *
from turtle import *
k=50


tracer(0)
screensize(1000,2000)
pendown()
right(60)
forward(4*k)
right(120)
for i in range(4):
    forward(3*k)
    right(240)
    forward(3*k)
    right(120)
forward(4*k)
right(90)
forward((8*sqrt(3))*k)
right(90)
forward(8*k)
penup()

for x in range(-100,100):
    for y in range(-100,100):
        setpos(x*k,y*k)
        dot(3)
done()