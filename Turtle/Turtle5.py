import turtle

#Altın Oran Çizim(Galiba Altın Oran Degil)

altınoran=turtle.Screen()
turtle.bgcolor("Black")

altın=turtle.Turtle()
altın.pencolor("Yellow")
altın.speed(300)
def altıninhıo(size):
    for i in range(4):
        altın.forward(size)
        altın.left(90)

altıninhıo(150)
altıninhıo(140)
altıninhıo(130)
altıninhıo(120)
altıninhıo(110)
altıninhıo(100)
altıninhıo(90)
altıninhıo(80)
altıninhıo(70)
altıninhıo(60)
altıninhıo(50)
altıninhıo(40)
altıninhıo(30)
altıninhıo(20)
altıninhıo(10)
altıninhıo(5)

turtle.done()