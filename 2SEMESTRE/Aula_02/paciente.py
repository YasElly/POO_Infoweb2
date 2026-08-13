from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nasc = nasc
    def __str__(self):
        return f"Nome = {self.__nome} - CPF = {self.__cpf} - Telefone = {self.__fone} - Nascimento = {self.__nasc.strftime('%d/%m/%Y')}"
    def Idade(self):
        x = datetime.now() - self.__nasc
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"
    