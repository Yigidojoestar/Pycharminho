import turtle

#İnteraktif Çizme

tahta=turtle.Screen()
tahta.bgcolor("Black")
tahta.title("İnteraktif Çiziminho Oyunu")

interaktif=turtle.Turtle()
interaktif.pencolor("white")

def ileri():
    interaktif.forward(100)
def sol():
    interaktif.left(90)
def sağ():
    interaktif.right(90)
def sil():
    interaktif.clear()
def çağır():
    interaktif.home()
def çiz():
    interaktif.pendown()
def bırak():
    interaktif.penup()

tahta.listen()
tahta.onkey(fun=ileri,key="space")
tahta.onkey(fun=sol,key="Left")
tahta.onkey(fun=sağ,key="Right")
tahta.onkey(fun=sil,key="Escape")
tahta.onkey(fun=çağır,key="e")
tahta.onkey(fun=çiz,key="Tab")
tahta.onkey(fun=bırak,key="m")


turtle.mainloop()
