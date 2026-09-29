from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            if op == 9: UI.departamento_inserir()
            if op == 10: UI.departamento_listar()
            if op == 11: UI.departamento_atualizar()
            if op == 12: UI.departamento_excluir()

    @staticmethod
    def menu():
        print("Clientes ----------------------------------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Serviços ----------------------------------")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Departamentos -----------------------------")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print("13-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        #id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

    @staticmethod
    def departamento_inserir():
        nome = input("Informe o nome: ")
        diretor = input("Informe o diretor: ")
        fone = input("Informe o telefone: ")
        Service.departamento_inserir(nome, diretor, fone)

    @staticmethod
    def departamento_listar():
        for obj in Service.departamento_listar(): print(obj)

    @staticmethod
    def departamento_atualizar():
        for obj in Service.departamento_listar(): print(obj)
        id = int(input("Informe o id do departamento a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        diretor = input("Informe o novo diretor: ")
        fone = input("Informe o novo telefone: ")
        Service.departamento_atualizar(id, nome, diretor, fone)

    @staticmethod
    def departamento_excluir():
        for obj in Service.departamento_listar(): print(obj)
        id = int(input("Informe o id do departamento a ser excluído: "))
        Service.departamento_excluir(id)
UI.main()