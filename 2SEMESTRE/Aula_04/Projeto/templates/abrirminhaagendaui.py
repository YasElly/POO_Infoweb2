import streamlit as st
import time
from datetime import datetime
from service import Service

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        data = st.text_input(
            "Informe a data no formato dd/mm/aaaa",
            datetime.now().strftime("%d/%m/%Y")
        )

        hora_inicial = st.text_input(
            "Informe o horário inicial no formato HH:MM",
            "09:00"
        )

        hora_final = st.text_input(
            "Informe o horário final no formato HH:MM",
            "12:00"
        )

        intervalo = st.number_input(
            "Informe o intervalo entre os horários (min)",
            min_value=1,
            value=30,
            step=1
        )

        if st.button("Abrir Agenda"):
            try:
                inicio = datetime.strptime(
                    data + " " + hora_inicial,
                    "%d/%m/%Y %H:%M"
                )

                fim = datetime.strptime(
                    data + " " + hora_final,
                    "%d/%m/%Y %H:%M"
                )

                quantidade = Service.horario_abrir_agenda(
                    inicio,
                    fim,
                    int(intervalo),
                    st.session_state["usuario_id"]
                )

                st.success(
                    f"Agenda aberta com sucesso! {quantidade} horários criados."
                )

                time.sleep(2)
                st.rerun()

            except ValueError as e:
                st.error(str(e))