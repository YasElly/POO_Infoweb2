class Time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self,id):
        if id<0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self,nome):
        if nome =="": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_estado(self,estado): 
        if estado =="": raise ValueError("Estado não pode ser vazio")
        self.__estado = estado
    def __str__(self): return f"ID:{self.__id} - NOME:{self.__nome} - ESTADO:{self.__estado}"
class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def get_id(self):
        return self.__id
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError("Id do time deve ser positivo")
        self.__idTime = idTime
    def get_idTime(self):
        return self.__idTime
    def set_nome(self, nome):
        if nome == "":raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_camisa(self, camisa):
        if camisa <= 0: raise ValueError("Número da camisa inválido")
        self.__camisa = camisa
    def get_camisa(self):
        return self.__camisa
    def __str__(self):
        return f"ID:{self.__id} - TIME:{self.__idTime} - NOME:{self.__nome} - CAMISA:{self.__camisa}"

class UI:
    times = []
    jogadores = []

    @staticmethod
    def menu():
        op = 0
        while op != 9:
            print("1-Inserir time")
            print("2-Listar times")
            print("3-Atualizar time")
            print("4-Excluir time")
            print("5-Inserir jogador")
            print("6-Listar jogadores")
            print("7-Listar jogadores de um time")
            print("8-Transferir jogador")
            print("9-Sair")

            op = int(input("Escolha uma opção: "))
            if op == 1:
                UI.inserir_time()

            elif op == 2:
                UI.listar_times()

            elif op == 3:
                UI.atualizar_time()

            elif op == 4:
                UI.excluir_time()

            elif op == 5:
                UI.inserir_jogador()

            elif op == 6:
                UI.listar_jogadores()

            elif op == 7:
                UI.listar_jogadores_do_time()

            elif op == 8:
                UI.transferir_jogador()
    @staticmethod
    def inserir_time():
        id = int(input("Id: "))
        nome = input("Nome: ")
        estado = input("Estado: ")

        t = Time(id, nome, estado)
        UI.times.append(t)

    @staticmethod
    def listar_times():
        for t in UI.times:
            print(t)

    @staticmethod
    def atualizar_time():
        id = int(input("Digite o id do time: "))

        for t in UI.times:
            if t.get_id() == id:
                nome = input("Novo nome: ")
                estado = input("Novo estado: ")

                t.set_nome(nome)
                t.set_estado(estado)

    @staticmethod
    def excluir_time():
        id = int(input("Digite o id do time: "))

        for t in UI.times:
            if t.get_id() == id:
                UI.times.remove(t)

    @staticmethod
    def inserir_jogador():
        id = int(input("Id do jogador: "))
        idTime = int(input("Id do time: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))

        j = Jogador(id, idTime, nome, camisa)
        UI.jogadores.append(j)

    @staticmethod
    def listar_jogadores():
        for j in UI.jogadores:
            print(j)

    @staticmethod
    def listar_jogadores_do_time():
        idTime = int(input("Id do time: "))

        for j in UI.jogadores:
            if j.get_idTime() == idTime:
                print(j)

    @staticmethod
    def transferir_jogador():
        idJogador = int(input("Id do jogador: "))
        novoTime = int(input("Novo time: "))

        for j in UI.jogadores:
            if j.get_id() == idJogador:
                j.set_idTime(novoTime)

UI.menu()          