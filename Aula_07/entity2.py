#ENTIDADE
import math
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
    def calc_area(self):
        return math.pi * self.__r**2
    def calc_circunferencia(self):
        return 2 * math.pi * self.__r

class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, d):
        if d>=0: self.__distancia = d
        else: raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def set_tempo(self, t):
        if t>0: self.__tempo = t
        else: raise ValueError()
    def get_tempo(self):
        return self.__tempo
    def velocidade_media(self):
        return self.__distancia / self.__tempo
    
class Banco:
    def __init__(self):
        self.__titular = ""
        self.__numero = 0
        self.__saldo = 0.0
    def set_titular(self, nome):
        if nome != "": self.__titular = nome
        else: raise ValueError()
    def set_numero(self, num):
        if num>0: self.__numero = num
        else: raise ValueError()
    def set_saldo(self, valor):
        if valor >=0: self.__saldo = valor
        else: raise ValueError()
    def get_titular(self):
        return self.__titular
    def get_numero(self):
        return self.__numero
    def get_saldo(self):
        return self.__saldo
    def depositar(self, valor):
        if valor>0:
            self.__saldo +=valor
        else: raise ValueError()
    def sacar(self, valor):
        if valor>0 and valor<=self.__saldo:
            self.__saldo -= valor
        else: raise ValueError()
    
class Cinema:
    def __init__(self):
        self.__d = ""
        self.__h = 0
        self.base = 0
        self.ingresso = 0
    def set_dia(self, v):
        if v in ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']:
            self.__d = v
        else: raise ValueError("Dia da semana inválido")
    def set_hora(self, v):
        if v<=23: self.__h = v
        else: raise ValueError()
    def get_dia(self):
        return self.__d
    def get_hora(self):
        return self.__h
    def calc_ingresso(self):
        if self.__d == 'quarta':
            return 8
        if self.__d in ['segunda', 'terça', 'quinta']:
            base = 16
        else:
            base = 20
        if self.__h >=17:
            return base *1.5
        else:
            return base
    
#INTERFACE COM O USUÁRIO
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2:UI.circulo()
            if op == 3:UI.viagem()
            if op == 4:UI.conta()
            if op == 5:UI.cinema()
            if op == 9:UI.circulo()
    @staticmethod
    def menu():  
        print("1-Triangulo 2-Círculo 3-Viagem 4- Conta Bancaria 5-Ingresso 9-Fim")
        op=int(input("Escolha uma opção: "))
        if op == 9:
            print("Programa Finalizado. Tchau :)")
        return op
    @staticmethod
    def triangulo():
        print("Cálculo da área de um triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base:")))
        x.set_altura(float(input("Informe o valor da altura:")))
        area = x.calc_area()
        print(f"Um triângulo com a base {x.get_base()} e altura{x.get_altura()} tem área = {area}")
    @staticmethod
    def circulo():
        print("Cálculo da área e comprimento da circunferência de um circulo")
        x = Circulo()
        x.set_raio(float(input("Digite o valor do raio: ")))
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um círculo de raio {x.get_raio()} tem área = {area} e circunferencia = {circunferencia}")
    @staticmethod
    def viagem():
        print("Cálculo da velocidade média de uma viagem")
        x = Viagem()
        x.set_distancia(float(input("Digite a distância em km: ")))
        x.set_tempo(float(input("Digite o tempo em horas (1h30 = 1.5):")))
        v = x.velocidade_media()
        print(f"A velocidade média foi de {v:.2f} km/h")
    @staticmethod
    def conta():
        print("Operações de Conta Bancária")
        x= Banco()
        x.set_titular(input("Nome do titular: "))
        x.set_numero(int(input("Número da conta: ")))
        print(f"Conta criada! Saldo atual: {x.get_saldo()}")
        op = int(input("1-Depositar 2-Sacar: "))
        if op==1:
            valor=float(input("Valor do deposito: "))
            x.depositar(valor)
        elif op==2:
            valor=float(input("Valor do saque: "))
            x.sacar(valor)
        print(f"Saldo atual: {x.get_saldo()}")
    @staticmethod
    def cinema():
        print("Operações de Compra de Ingressos")
        x= Cinema()
        x.set_dia(input('Dia da semana da sessão: ').lower())
        x.set_hora(int(input('Horário (0-23): ')))
        print(f"Dia da sessão: {x.get_dia()}")
        print(f"Horário: {x.get_hora()}")
        print(f"Valor do Ingresso: {x.calc_ingresso():.0f},00")
UI.main()