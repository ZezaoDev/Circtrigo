from turtle import *
import math

# === Configurações do Turtle ===

color("black", "lightgreen")
shape("turtle")
bgcolor("white")


# === CIRCUNFERÊNCIA TRIGONOMÉTRICA ===


def circulo(raio):
    color("black")
    pensize(3.5)
    rt(90)
    pu()
    fd(raio)
    lt(90)
    pd()
    circle(raio)
    pu()
    home()
    pd()


def eixos(raio):
    color("darkblue")
    pensize(3)
    pu()
    bk(raio)
    pd()
    fd(raio*2)
    bk(raio)
    rt(90)
    pu()
    bk(raio)
    pd()
    fd(raio*2)
    bk(raio)
    lt(90)


def angulo(angulo, raio):
    lt(angulo)
    fd(raio)
    if angulo == 30:
        color("gray")
        pensize(0.5)
        lt(150)
        fd(r*math.sqrt(3))
        lt(90)
        fd(r)
        lt(90)
        fd(r*math.sqrt(3))
        lt(90)
        fd(r)
        color("red")
        pensize(1.5)
    if angulo == 45:
        color("gray")
        pensize(0.5)
        lt(135)
        fd(r*math.sqrt(2))
        lt(90)
        fd(r*math.sqrt(2))
        lt(90)
        fd(r*math.sqrt(2))
        lt(90)
        fd(r*math.sqrt(2))
        color("red")
        pensize(1.5)
    if angulo == 60:
        color("gray")
        pensize(0.5)
        lt(120)
        fd(r)
        lt(90)
        fd(r*math.sqrt(3))
        lt(90)
        fd(r)
        lt(90)
        fd(r*math.sqrt(3))
        color("red")
        pensize(1.5)
    home()


def angulos(raio):
    color("red")
    pensize(1.5)
    angulo(30, raio)
    angulo(45, raio)
    angulo(60, raio)
    angulo(90, raio)
    angulo(120, raio)
    angulo(135, raio)
    angulo(150, raio)
    angulo(180, raio)
    angulo(210, raio)
    angulo(225, raio)
    angulo(240, raio)
    angulo(270, raio)
    angulo(300, raio)
    angulo(315, raio)
    angulo(330, raio)
    angulo(360, raio)

def fim(raio):
    pu()
    fd(raio)
    rt(90)
    fd(raio)
    rt(180)
    color("black", "lightgreen")

# =====================================


r = float(300) #!!! coloque o valor do raio aqui !!!

circulo(r)
eixos(r)
angulos(r)
fim(r)
input('')
