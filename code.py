# Importar bibliotecas necessárias
import pandas as pd

from flask import Flask, jsonify

# Iniciar aplicativo
app = Flask(__name__)

# Criar função (página0)
@app.route('/')
def vendas():

  # Pegar arquivo csv
  tabela = pd.read_csv('base_de_dados.csv')

  # Lógica para calcular as vendas do arquivo csv
  total_de_vendas = tabela['Vendas'].sum()
  # Armazenar o calculo

  resposta = {'total_de_vendas': total_de_vendas}

  # Retornar em tipo json
  return jsonify(resposta)

# Rodar o aplicativo no host da Replit
app.run(host='0.0.0.0')