import turtle
import math

class circtrigo:

    def __init__(self):
        self.raio = 0
        self.grau = 0
        self.seno = 0
        self.cosseno = 0
        self.tangente = 0
        self.quadrante = 0
        self.tema = ''
        
    def seta(self):
        # DESENHA UMA SETA
        turtle.left(90)
        turtle.forward(5)
        turtle.right(120)
        turtle.forward(10)
        turtle.right(120)
        turtle.forward(10)
        turtle.right(120)
        turtle.forward(5)
        turtle.right(90)

    def linha(self, pxls):
        # DESENHA UMA LINHA PONTILHADA
        pixels = int(pxls//1)
        if pixels % 2 == 0:
            pixels = pixels + 1
        for x in range(0, pixels//10):
            turtle.pendown()
            turtle.forward(5)
            turtle.penup()
            turtle.forward(5)
            turtle.pendown()
        turtle.forward(pixels%10)            
    
    def reset(self):
        # RETORNA PRA POSIÇÃO INICIAL
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.speed(6)
        turtle.pensize(2)
        if self.tema == 'dark':
            self.dark()
        else:
            self.light()
        
    def light(self):
        if self.tema != "light":
            turtle.bgcolor("white")
            turtle.pencolor("black")
        
    def dark(self):
        if self.tema != "dark":
            turtle.bgcolor("black")
            turtle.pencolor("white")
    
    def circulo(self, raio):
        # DESENHA O CIRCULO
        self.raio = raio
        turtle.right(90)
        turtle.penup()
        turtle.forward(self.raio)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(self.raio)
        self.reset()

    def eixos(self):
        # EIXO X
        turtle.penup()
        turtle.backward(self.raio + 50)
        turtle.pendown()
        self.linha((self.raio*2)+100)
        self.seta()
        self.reset()
        # EIXO Y
        turtle.left(90)
        turtle.penup()
        turtle.backward(self.raio + 50)
        turtle.pendown()
        self.linha((self.raio * 2) + 100)
        self.seta()
        self.reset()

    def angulo(self, grau):
        # DESENHA O ANGULO
        self.grau = grau
        turtle.left(self.grau)
        turtle.forward(self.raio)
        self.reset()
        # DEFINE O VALOR DO SENO, COSSENO E TANGENTE.
        self.seno = math.sin(math.radians(self.grau))
        self.cosseno = math.cos(math.radians(self.grau))
        self.tangente = math.tan(math.radians(self.grau))
        # DEFINE O QUADRANTE DO ÂNGULO
        vquad = self.grau % 360
        if 0 < vquad < 90:
            self.quadrante = 1
        elif 90 < vquad < 180:
            self.quadrante = 2
        elif 180 < vquad < 270:
            self.quadrante = 3
        elif 270 < vquad < 360:
            self.quadrante = 4
    
    def sen(self):
        # DESENHA O SENO
        turtle.left(self.grau)
        turtle.forward(self.raio)
        turtle.pencolor("red")
        turtle.left(180 - self.grau)
        self.linha(self.cosseno * self.raio)
        turtle.left(90)
        turtle.forward(self.seno * self.raio)
        self.reset()
    
    def csen(self):
        # DESENHA O COSSENO
        turtle.left(self.grau)
        turtle.forward(self.raio)
        turtle.pencolor("green")
        turtle.right(self.grau + 90)
        self.linha(self.seno * self.raio)
        turtle.right(90)
        turtle.forward(self.cosseno * self.raio)
        self.reset()
    
    def tan(self):
        # DESENHA A TANGENTE
        turtle.left(self.grau)
        turtle.penup()
        turtle.forward(self.raio)
        turtle.pencolor("blue")
        turtle.pendown
        self.linha(math.sqrt(((self.tangente*self.raio)**2) + (self.raio**2)) - self.raio)
        turtle.right(90 + self.grau)
        turtle.forward(self.tangente * self.raio)
        self.reset()
    

    
