import streamlit as st
from service import Service
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        foto = st.file_uploader("ESCOLHA UMA NOVA FOTO", type=["jpg", "jpeg", "png"], key="foto_profissional_novo" )
        if st.button("Atualizar"):
            try:
                imagem = foto.getvalue() if foto else None
                id = op.get_id()
                Service.profissional_atualizar(id, nome, email, especialidade, senha, imagem)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
                        