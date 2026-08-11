#class Triangulo:
#    def __init__(self):
#        self.__b = 0
#        self.__h = 0
#
#print(x)
#printa as coordenadas/endereço de onde esta a class
class Triangulo:
    def __init__(self, b, h): #dentro do parenteses são parametros
        self.__b = 0
        self.__h = 0
    def __str__(self): #metodos magicos com underlines
        return f"Eu sou um triangulo, minha base é {self.__b} e minha altura é {self.__h}"

x = Triangulo(10, 20)


print(x)