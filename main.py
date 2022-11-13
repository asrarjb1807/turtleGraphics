from turtle import Turtle, Screen


t = Turtle()
#                             METHOD 1(mine)
# for i in range(3):
#     t.fd(100), t.right(120)
# for i in range(4):
#     t.fd(100), t.right(90)
# for i in range(5):
#     t.fd(100), t.right(72)
# for i in range(6):
#     t.fd(100), t.right(60)
# for i in range(7):
#     t.fd(100), t.right(51.43)
# #     135, 140, 144
# for i in range(8):
#     t.fd(100), t.right(45)
# for i in range(9):
#     t.fd(100), t.right(40)
# for i in range(10):
#     t.fd(100), t.right(36)
# t.fd(100)
# for i in range(360):
#     t.fd(1), t.right(1)

#                         METHOD 2
def make_shape(sides) :
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100), t.left(angle)
for i in range(3, 11):
    make_shape(i)


screen = Screen()
screen.exitonclick()
