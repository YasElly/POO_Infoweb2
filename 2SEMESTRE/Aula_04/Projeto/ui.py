from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 20:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            if op == 9: UI.horario_listar()
            if op == 10: UI.horario_atualizar()
            if op == 11: UI.horario_excluir()
            if op == 12: UI.profissional_inserir()
            if op == 13: UI.profissional_listar()
            if op == 14: UI.profissional_atualizar()
            if op == 15: UI.profissional_excluir()
            if op == 16: UI.atendimento_inserir()
            if op == 17: UI.atendimento_listar()
            if op == 18: UI.atendimento_atualizar()
            if op == 19: UI.atendimento_excluir()


    @staticmethod
    def menu():
        print("Clientes ----------------------------------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("Serviços ----------------------------------")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("Horários ----------------------------------")
        print("9-Listar , 10-Atualizar, 11-Excluir")
        print("Profissionais ----------------------------------")
        print("12-Inserir, 13-Listar, 14-Atualizar, 15-Excluir")
        print("Atendimentos ----------------------------------")
        print("16-Inserir, 17-Listar, 18-Atualizar, 19-Excluir")
        print("20-Fim")
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
    def horario_inserir():
        data = input("Informe a data: ")
        confirmado = input("Confirmado: ")
        id_cliente = input("Informe o id do cliente: ")
        id_servico = input("Informe o id do serviço: ")
        id_profissional = input("Informe o id do profissional: ")
        Service.horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional)
    @staticmethod
    def horario_listar():
        for obj in Service.horario_listar(): print(obj)
    @staticmethod
    def horario_atualizar():
        for obj in Service.horario_atualizar(): print(obj)
        id = int(input("Informa o novo id: "))
        data = input("Informe a nova data: ")
        confirmado = input("Confirmado: ")
        id_cliente = input("Informe o novo id do cliente: ")
        id_servico = input("Informe o novo id do serviço: ")
        id_profissional = input("Informe o novo id do profissional: ")
        Service.horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional)
    @staticmethod
    def horario_excluir(id):
        for obj in Service.horario_excluir(): print(obj)
        id = int(input("Informe o id do horário a ser excluído: "))
        Service.horario_excluir(id)

    @staticmethod
    def profissional_inserir(id):
        pass

    @staticmethod
    def profissional_listar(id):
        pass

    @staticmethod
    def profissional_atualizar(id):
        pass

    @staticmethod
    def profissional_excluir(id):
        pass

    @staticmethod
    def atendimento_inserir(id):
        pass

    @staticmethod
    def atendimento_listar(id):
        pass

    @staticmethod
    def atendimento_atualizar(id):
        pass

    @staticmethod
    def atendimento_excluir(id):
        pass

UI.main()