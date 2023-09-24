# Módulos com valores constantes

# Import
import streamlit as st

# Spacer
def spacer(space_type, location=st):
	if 'title' in space_type:
		location.title('')
	if 'head' in space_type:
		location.header('')
	if 'subheader' in space_type:
		location.subheader('')
	if 'write' in space_type:
		location.write('')
	if 'text' in space_type:
		location.text('')

# Linha
def line(location=st):
	location.write('_____')

# Percentuais
percentages = {
	'residencial': {
		'taxa_desocupacao': 5.,
		'manutencao': 3.,
		'gerenciamento': 5.
	},
	'comercial': {
		'taxa_desocupacao': 10.,
		'manutencao': 10.,
		'gerenciamento': 7.5
	}
}

# Financiamento
preco_compra = 'preco_compra'
taxa_juros = 'taxa_juros'
periodo_amortizacao = 'periodo_amortizacao'
pct_down = 'pct_down'
down_pmt = 'down_pmt'

# Renda
tipo_propriedade = 'tipo_propriedade'
faturamento = 'faturamento'
taxa_desocupacao = 'taxa_desocupacao'
fundo_desocupacao = 'fundo_desocupacao'
faturamento_bruto = 'faturamento_bruto'







