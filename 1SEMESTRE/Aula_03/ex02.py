#A classe é o modelo, a forma de bolo
class Triangulo:
    #atributo - dados que vao ser armazenados : b(base), h(altura)
    def __init__(self):
        self.b = 0
        self.h = 0
    #método - cálclos que vão ser feitos
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
print("PRIMEIRO TRIÂNGULO")
print("Informe a base do triângulo")
x.b = float(input())
print("Informe o valor da altura")
x.h = float(input())
a = x.calc_area()
print(f"A área do triângulo é {a:.2f}")

print("SEGUNDO TRIÂNGULO")
y = Triangulo()
print(x.b, x.h)
print("Informe a base do triângulo")
y.b = float(input())
print("Informe o valor da altura")
y.h = float(input())
a = y.calc_area()
print(f"A área do triângulo é {a:.2f}")

print(f"Primeiro triângulo: base = {x.b}, altura = {x.h}, área = {x.calc_area()}")
print(f"Segundo triângulo: base = {y.b}, altura = {y.h}, área = {y.calc_area()}")