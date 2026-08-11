#Algumas variáveis podem assumir apenas valores definidos
#Ex: Dias da semana(seg, ter, qua, qui, sex, sab, dom); Estações (outono, inverno, primavera, verão)
import enum

class Estacao(enum.Enum):
    OUTONO = 1
    INVERNO = 2
    PRIMAVERA = 3
    VERAO = 4

a = Estacao.INVERNO
b = Estacao["OUTONO"]
c = Estacao(3)

print(a)
print(b)
print(c)
print(c.name)
print(c.value)
