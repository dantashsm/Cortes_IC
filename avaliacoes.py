import streamlit as st
import pandas as pd

cortes = ['Degradê','Zero','Militar','Americano']

local = ['Campos Elíseos','Monet','Alegria','Boa Vista']

def buscar():
    pass

def suporte():
    pass



st.title('Buscador de Cortes')

corte_selecionado = st.selectbox('Qual o tipo de corte que você procura?',cortes)

bairro_selecionado = st.selectbox('Qual a localidade de preferência?', local)

buscador = st.button('Buscar profissional de corte',on_click= buscar())
