import turtle

#İç içe geçen kareler

birsürükare=turtle.Screen()
birsürükare.bgcolor("Orange")

kareler = turtle.Turtle()
kareler.speed(400)

def içiçekare(size):
    for i in range(4):
        kareler.forward(size)
        kareler.left(90)
        size = size - 1

içiçekare(150)
içiçekare(140)
içiçekare(130)
içiçekare(120)
içiçekare(110)
içiçekare(100)
içiçekare(90)
içiçekare(80)
içiçekare(70)
içiçekare(60)
içiçekare(50)
içiçekare(40)
içiçekare(30)
içiçekare(20)
içiçekare(10)
içiçekare(5)


turtle.done()

