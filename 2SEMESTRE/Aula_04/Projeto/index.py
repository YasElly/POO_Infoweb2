from templates.manterclienteui import ManterClienteUI
from templates.manterservicoui import ManterServicoUI
from templates.manterhorarioui import ManterHorarioUI
from templates.manterprofissionalui import ManterProfissionalUI
from templates.manteratendimentoui import ManterAtendimentoUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horários", "Profissionais", "Atendimentos"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == "Horários": ManterHorarioUI.main()
        if op == "Profissionais": ManterProfissionalUI.main()
        if op == "Atendimentos": ManterAtendimentoUI.main()

IndexUI.main()

# Abstração é o que vai ser representado sobre cada entidade. Por exemplo, nome, matricula, nascimento, curso vinculados à entidade ALUNO.
# Entidade é o que irá ser representado do mundo real. No suap, por exemplo, são ALUNOS, NOTAS, PROFESSORES, etc.
# Classificação é a forma de organizar as coisas.
# Referência é x
# Instâncias são os objetos
