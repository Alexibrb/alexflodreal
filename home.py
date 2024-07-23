import streamlit as st
import pandas as pd
import os
import time
from funcoes import *



########## CONFIGURAÇÕES
st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto"
)
titulo()
#estilos()

########################################### Barra Lateral #######################################


spinner()
link3 = "logogrande.jpeg"
link2 = "grafico.png"
icone = "icone.jpeg"
op = "Operador"

st.logo(link2, icon_image=link2)
st.markdown('# Bem-vindo ao Sistema')

col1, col2 = st.columns(2)

with col1:

    st.image(link3, width=500)
    st.markdown(
    f'<img src="{link3}" style="border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);" width="500">',
    unsafe_allow_html=True
)

with col2:
    if os.path.exists('parametros.csv'):
        tabelaconfig = pd.read_csv('parametros.csv', sep=",")
        nome = tabelaconfig['operador'][0]
        if nome != '':

            st.title(f'  :blue[Operador⤵️]')
            st.success(f'# 🧑‍💻 {nome}')
    else:
        st.error("## 🚨Parâmetros não cadastrados🚨")
        st.success("## Acesse o menu da barra lateral para cadastrar")



