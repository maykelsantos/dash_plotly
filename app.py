# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import requests

url = 'https://servicodados.ibge.gov.br/api/v3/agregados/6784/periodos/2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020/variaveis/9808|93|9812?localidades=N1[all]'
requisicao = requests.get(url)
dados = requisicao.json()

pib = dados[0]['resultados'][0]['series'][0]['serie']
df =pd.DataFrame.from_dict(pib, orient = 'index', columns = ['PIB'])
df.reset_index(inplace = True)
df.columns = ['Ano', 'PIB']
df['PIB'] = df['PIB'].astype('int')
pais = dados[0]['resultados'][0]['series'][0]['localidade']['nome']
