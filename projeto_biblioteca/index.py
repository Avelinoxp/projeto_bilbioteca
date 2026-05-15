import streamlit as st

st.title('Sistema De Biblioteca')

# Criar Lista de livros
if 'Livros' not in st.session_state:
    st.session_state['Livros'] = []

# Cadastrar Livro
st.subheader('Cadastrar Livro')
nome_livro = st.text_input('Nome Do Livro')
autor = st.text_input('Autor')

if st.button('Cadastrar Livro'):
    if nome_livro != '' and autor != '':
        livro = {
            'nome': nome_livro,
            'autor': autor,
            'emprestado': False
        }
        st.session_state['Livros'].append(livro)
        st.success('Livro Cadastrado com sucesso')

# Exibir Livros Cadastrados
st.subheader('Livros Cadastrados')
if len(st.session_state['Livros']) == 0:
    st.warning('Nenhum livro cadastrado')
else:
    for i, livro in enumerate(st.session_state['Livros']):
        st.write(f"{livro['nome']}")
        st.write(f"Autor: {livro['autor']}")
        if livro['emprestado']:
            st.error('Emprestado')
        else:
            st.success('Disponível')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Emprestar', key=f'emp{i}'):
                st.session_state['Livros'][i]['emprestado'] = True
                st.rerun()
        with col2:
            if st.button('Devolver', key=f'dev{i}'):
                st.session_state['Livros'][i]['emprestado'] = False
                st.rerun()
        st.divider()        