class Viagem:
    def __init__(self, dest, dist, lit):
        self.set_destino(dest) = ""
        self.set_distancia(dist) = 0.0
        self.set_litros(lit) = 0.0
    def set_destino(self, dest):
        if dest != "": self.__destino = dest
        else: raise ValueError()
    def set_distancia(self, dist):
        if dist >= 0: self.__distancia = dist
        else: raise ValueError()
    def set_litros(self, lit):
        if lit >= 0: self.__litros = lit
        else: raise ValueError()
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def Consumo(self):
        return self.__distancia/self.__litros
    def __str__(self):
        return (f"Destino:{self.get_destino}")

    
class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
        print("Programa Finalizado. Tchau :)")
    @staticmethod
    def menu():  
        print("1-Calcular 2-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def calculo():
        dest = input("Qual o destino da viagem?")
        dist = float(input("Qual a distância percorrida em km?"))
        lit = float(input("Quantos litros de combustível foram gastos?"))
        x = Viagem(dest, dist, lit)

ViagemUI.main()
