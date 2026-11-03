import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")

        op = Service.profissional_listar_id(
            st.session_state["usuario_id"]
        )

        if op == None:
            st.error("Profissional não encontrado")
        else:
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            especialidade = st.text_input(
                "Informe a nova especialidade", op.get_especialidade()
            )
            senha = st.text_input(
                "Informe a nova senha", op.get_senha(), type="password"
            )

            if st.button("Atualizar"):
                try:
                    Service.profissional_atualizar(
                        op.get_id(), nome, email, especialidade, senha
                    )

                    st.success("Dados atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()

                except ValueError as e:
                    st.error(str(e))