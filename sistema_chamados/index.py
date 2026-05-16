import streamlit as st
st.title('Sistema de Chamados')
# Criar Lista de Chamados
if 'Chamados' not in st.session_state:
    st.session_state.chamados = []

#Abrir chamado
st.subheader('Abrir Chamado')
st.text_input('Título do Chamado')
titulo = st.text_area('Título do Chamado')
descricao = st.text_area('Descrição do Serviço')

if st.button('Abrir Chamado'):
    if titulo != '' and descricao != '':
        chamado = {
            'titulo': titulo,
            'descricao': descricao,
            'status': 'Aberto'
        }
        st.session_state.chamados.append(chamado)
        st.success('Chamado Aberto com Sucesso')
        