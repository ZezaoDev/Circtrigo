import turtle as t
import math


class circTrigo:

    def __init__(self):
        self.raio = 0
        self.grau = 0
        self.seno = 0
        self.cosseno = 0
        self.tangente = 0
        self.quadrante = 0
        self.tema = ''
        t.bgcolor("black")
        t.pencolor("white")
        
    def seta(self):
        # DESENHA UMA SETA
        t.left(90)
        t.forward(5)
        t.right(120)
        t.forward(10)
        t.right(120)
        t.forward(10)
        t.right(120)
        t.forward(5)
        t.right(90)

    def linha(self, pxls):
        # DESENHA UMA LINHA PONTILHADA
        pixels = int(pxls//1)
        if pixels % 2 == 0:
            pixels = pixels + 1
        for x in range(0, pixels//10):
            t.pendown()
            t.forward(5)
            t.penup()
            t.forward(5)
            t.pendown()
        t.forward(pixels%10)            
    
    def reset(self):
        # RETORNA PRA POSICAO INICIAL
        t.penup()
        t.home()
        t.pendown()
        t.speed(0)
        t.pensize(2)
        t.pencolor("white")

    def circulo(self, raio):
        # DESENHA O CIRCULO
        self.raio = raio
        t.right(90)
        t.penup()
        t.forward(self.raio)
        t.left(90)
        t.pendown()
        t.circle(self.raio)
        self.reset()

    def eixos(self):
        # EIXO X
        t.penup()
        t.backward(self.raio + 50)
        t.pendown()
        self.linha((self.raio*2)+100)
        self.seta()
        self.reset()
        # EIXO Y
        t.left(90)
        t.penup()
        t.backward(self.raio + 50)
        t.pendown()
        self.linha((self.raio*2)+100)
        self.seta()
        self.reset()

    def angulo(self, grau):
        # DESENHA O ANGULO
        self.grau = grau % 360
        t.left(self.grau)
        t.forward(self.raio)
        self.reset()
        # DEFINE O VALOR DO SENO, COSSENO E TANGENTE.
        self.seno = math.sin(math.radians(self.grau))
        self.cosseno = math.cos(math.radians(self.grau))
        self.tangente = math.tan(math.radians(self.grau))
        # DEFINE O QUADRANTE DO ANGULO
        vquad = self.grau
        if 0 < vquad < 90:
            self.quadrante = 1
        elif 90 < vquad < 180:
            self.quadrante = 2
        elif 180 < vquad < 270:
            self.quadrante = 3
        elif 270 < vquad < 360:
            self.quadrante = 4
        if vquad == 0 or vquad == 90 or vquad == 180 or vquad == 270 or vquad == 360:   # Quadrante 0 representa os angulos de resultados indefinidos
            self.quadrante = 0

    def sen(self):
        # DESENHA O SENO
        t.left(self.grau)
        t.forward(self.raio)
        t.pencolor("red")
        if self.quadrante == 1:
            t.left(180 - self.grau)
            self.linha(self.cosseno * self.raio)
            t.left(90)
            t.forward(self.seno * self.raio)
            print (self.seno)
        elif self.quadrante == 2:
            t.right(self.grau)
            self.linha((self.cosseno * self.raio) * -1)
            t.right(90)
            t.forward(self.seno * self.raio)
            print (self.seno)
        elif self.quadrante == 3:
            t.right(self.grau)
            self.linha(self.cosseno * self.raio * -1)
            t.left(90)
            t.forward(self.seno * self.raio * -1)
            print (self.seno)
        elif self.quadrante == 4:
            t.left(180 - self.grau)
            self.linha(self.cosseno * self.raio)
            t.left(90)
            t.forward(self.seno * self.raio)
            print (self.seno)
        else: 
            print("Erro: angulo invalido")
        self.reset()
    
    def csen(self):
        # DESENHA O COSSENO
        t.left(self.grau)
        t.forward(self.raio)
        t.pencolor("green")
        if self.quadrante == 1:
            t.right(self.grau + 90)
            self.linha(self.seno * self.raio)
            t.right(90)
            t.forward(self.cosseno * self.raio)
            print (self.cosseno)
        elif self.quadrante == 2:
            t.right(self.grau + 90)
            self.linha(self.seno * self.raio)
            t.right(90)
            t.forward(self.cosseno * self.raio)
            print (self.cosseno)
        elif self.quadrante == 3:
            t.right(self.grau - 90)
            self.linha(self.seno * self.raio * -1)
            t.right(90)
            t.forward(self.cosseno * self.raio * -1)
            print (self.cosseno)
        elif self.quadrante == 4:
            t.right(self.grau - 90)
            self.linha(self.seno * self.raio * -1)
            t.left(90)
            t.forward(self.cosseno * self.raio)
            print (self.cosseno)
        else: 
            print("Erro: angulo invalido")
        self.reset()
    
    def tan(self):
        # DESENHA A TANGENTE
        t.left(self.grau)
        t.penup()
        t.pencolor("blue")
        if self.quadrante == 1:
            t.forward(self.raio)
            t.pendown()
            self.linha(math.sqrt(((self.tangente*self.raio)**2) + (self.raio**2)) - self.raio)
            t.right(self.grau + 90)
            t.forward(self.tangente * self.raio)
            print (self.tangente)
        elif self.quadrante == 2:
            t.left(180)
            t.forward(self.raio)
            t.pendown()
            self.linha(math.sqrt(((self.tangente*self.raio)**2) + (self.raio**2)) - self.raio)
            t.left(90 - self.grau)
            t.forward(self.tangente * self.raio)
            print (self.tangente)
        elif self.quadrante == 3:
            t.left(180)
            t.forward(self.raio)
            t.pendown()
            self.linha(math.sqrt(((self.tangente*self.raio)**2) + (self.raio**2)) - self.raio)
            t.right(self.grau - 90)
            t.forward(self.tangente * self.raio)
            print (self.tangente)
        elif self.quadrante == 4:
            t.forward(self.raio)
            t.pendown()
            self.linha(math.sqrt(((self.tangente*self.raio)**2) + (self.raio**2)) - self.raio)
            t.right(90 + self.grau)
            t.forward(self.tangente * self.raio)
            print (self.tangente)
        else: 
            print("Erro: angulo invalido")
        self.reset()
    
