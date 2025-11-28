import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'best_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Título do aplicativo
st.title('Previsão do Nível de Obesidade')

# Inserção das variáveis
st.write("Insira as informações para previsão:")

# Variáveis de Categoria
gender = st.selectbox('Sexo', ['Masculino', 'Feminino'])
favc = st.selectbox('Você consome frequentemente alimentos de alta caloria  ?', ['Sim', 'Não'])
smoke = st.selectbox('Você fuma?', ['Sim', 'Não'])
scc = st.selectbox('Você controla seu consumo de calorias?', ['Sim', 'Não'])
calc = st.selectbox('Com qual frequência você consome bebida alcólica?', ['Não', 'As vezes', 'Frequentemente'])
caec = st.selectbox('Consumo de lanches/comes entre as refeições', ['Sempre', 'Frequentemente', 'As vezes', 'Não'])
mtrans = st.selectbox('Meio de transporte habitual', ['Carro', 'Bicicleta', 'Moto', 'Transporte Público', 'A pé'])

# Variaveis numéricas
age = st.number_input('Idade', min_value=0)
height = st.number_input('Altura (em cm)', min_value=0.0)
weight = st.number_input('Peso (em kg)', min_value=0.0)

# Frequencia de consumos de vegetais
fcvc_options = ['As vezes', 'Sempre', 'Nunca']

# Frequencia de consumo de vegetais captura
fcvc_input = st.selectbox('Com que frequência você come vegetais', fcvc_options)

# mapeamento numérico
fcvc_map = {'As vezes': 1, 'Sempre': 3, 'Nunca': 0}
fcvc = fcvc_map[fcvc_input]

# Numero de refeições principais
ncp_options = ['Mais de 3', 'Entre 1 e 2', 'Três']

# Numero de refeições principais
ncp_input = st.selectbox('Quantidade de refeições', ncp_options)

# Mapeamento numerico
ncp_map = {'Mais de 3': 4, 'Entre 1 e 2': 2.5, 'Três': 3}
ncp = ncp_map[ncp_input]

ch2o_options = ['Entre 1 e 2 Litros', 'Mais de 2 Litros', 'Menos de 1 Litro']
ch2o_input = st.selectbox('Qual seu consumo diário de água', ch2o_options)
ch2o_map = {'Menos de 1 Litro': 0, 'Entre 1 e 2 Litros': 1, 'Mais de 2 Litros': 2}
ch2o = ch2o_map[ch2o_input]

# Tempo de uso de tecnologia
tue_options = ['Não uso', '0–2 horas', '3–5 horas']

# Tempo de uso de tecnologia captura
tue_input = st.selectbox('Tempo de uso de dispositivos eletrônicos (horas por dia)', tue_options)

# mapeamento numerico
tue_map = {'Não uso': 0, '0–2 horas': 1, '3–5 horas': 2}
tue = tue_map[tue_input]

# Frequencia de atividade física
faf_options = ['Não tenho', '1 a 2 dias', '2 a 4 dias', '4 a 5 dias']

# Frequencia de atividade física input
faf_input = st.selectbox('Frequencia de atividade física (por semana)', faf_options)

# imput numerico
faf_map = {'Não tenho': 0, '1 a 2 dias': 1, '2 a 4 dias': 2, '4 a 5 dias': 3}
faf = faf_map[faf_input]


# Mapeamento das categorias
gender = 1 if gender == 'Masculino' else 0
favc = 1 if favc == 'Sim' else 0
smoke = 1 if smoke == 'Sim' else 0
scc = 1 if scc == 'Sim' else 0
calc_map = {'Não': 0, 'As vezes': 1, 'Frequentemente': 2}
calc = calc_map[calc]
caec_map = {'Sempre': 0, 'Frequentemente': 1, 'As vezes': 2, 'Não': 3}
caec = caec_map[caec]
mtrans_map = {'Carro': 0, 'Bicicleta': 1, 'Moto': 2, 'Transporte Público': 3, 'A pé': 4}
mtrans = mtrans_map[mtrans]

# Concatena todas as variáveis em um array
features = np.array([gender, age, height, weight, favc, fcvc, ncp, smoke, ch2o, scc, faf, tue, calc, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]).reshape(1, -1)

# Predição
if st.button('Previsão'):
    prediction = model.predict(features)
    st.write(f'A previsão de obesidade é: {prediction[0]}')
