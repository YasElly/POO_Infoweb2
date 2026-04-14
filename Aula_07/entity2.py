#ENTIDADE
class Triangulo:
    def __init__(self):
        self.__b =0
        self.__h =0
    def set_base(self, v):
        if v >=0:self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >=0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    
class Circulo:
    def __init__(self):
        self.__r = 0
    def set_raio(self, v):
        if v>=0:self.__r = v
        else: raise ValueError()
    def get_raio(self):
        return self.__r
    def calc_area(self, r, math):
        return math.pi * self.__r**2
    def calc_circunferencia(self, r, math):
        return 2 * math.pi * self.__r

class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def set_distancia(self, d):
        if d>=0: self.__d = d
    def get_distancia(self):
    def set_tempo(self, t);
    def get_tempo(self):
    def velocidade_media():
    
    
#INTERFACE COM O USUÁRIO
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu
            if op == 1: UI.triangulo()
            if op == 2:UI.circulo()
            if op == 3:UI.circulo()
            if op == 4:UI.circulo()
            if op == 5:UI.circulo()
            if op == 9:UI.circulo()
    @staticmethod
    def menu():  
        print("1-Triangulo 2-Círculo 3-Viagem 4- Conta Bancaria 5-Ingresso 9-Fim")
        op=int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triãngulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base:")))
        x.set_altura(float(input("Informe o valor da altura:")))
        area = x.calc
        print(f"Um triângulo com a base {x.get_base()} e altura{x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Cálculo da área e comprimento da circunferência de um circulo")
        x = Circulo()
        x.set_raio(float(input("Digite o valor do raio: ")))
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um círculo de raio{x.get_raio} tem área = {area} e circunferencia = {circunferencia}")
    def viagem():
        print("Em desenvolvimento")

UI.main()