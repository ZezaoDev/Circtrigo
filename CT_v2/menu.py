from CTclass import circtrigo
import sys
t = circtrigo()
class itensmenu():

    def __init__(self):
        self.opcao = 0
    
    def menu(self):
        print("           ")
        print("INICIAR (1)")
        print("SAIR    (2)")
        while True:
            self.opcao = int(input("Selecione a opção: "))
            if self.opcao == 1:
                self.iniciar()
                break
            elif self.opcao == 2:
                sys.exit()
                break
            
    def iniciar(self):
        t.circulo(250)
        t.eixos()
        self.iniciar_()
        while True:
            r_sn = str(input("Deseja inserir mais um ângulo (S/n)? "))
            if r_sn == 's' or r_sn == 'S':
                self.iniciar_()
            else:
                break
        self.menu()
    
    def iniciar_(self):
        t.angulo(int(input("Insira o valor do ângulo: ")))
        input("[ Seno     ]")
        t.sen()
        input("[ Cosseno  ]")
        t.csen()
        input("[ Tangente ]")
        t.tan()

print("                                                                     ")
print(" .d8888b.  d8b                  888            d8b                   ")
print("d88P  Y88b Y8P                  888            Y8P                   ")
print("888    888                      888                                  ")
print("888        888 888d888  .d8888b 888888 888d888 888  .d88b.   .d88b.  ")
print("888        888 888P    d88P     888    888P    888 d88P 88b d88  88b ")
print("888    888 888 888     888      888    888     888 888  888 888  888 ")
print("Y88b  d88P 888 888     Y88b.    Y88b.  888     888 Y88b 888 Y88..88P ")
print("  Y8888P   888 888       Y8888P   Y888 888     888   Y88888   Y88P   ")
print("                                                        888          ")
print("                                                   Y8b d88P          ")
print("v2.3.1                                               Y88P            ")
print("by José Vitor, Miriã Pedroso, Lívia Mariana, Larissa Amélia, Marineide Almeida.")

im = itensmenu()
im.menu()
