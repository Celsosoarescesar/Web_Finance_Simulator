# Módulo para cálculo da renda de aluguel

# Imports
import numpy as np
import pandas as pd
import streamlit as st
import front_end.constantes as const

# Função para os inputs
def property_units_inputs(location=st):

	tipo_propriedade = location.selectbox("Qual o Tipo de Imóvel?", [key.title() for key in const.percentages.keys()]).lower()
	const.spacer(['title', 'title'], location)

	text = 'Quantos Quartos o Imóvel Possui?'
	start_val = 1
	unit_count = int(location.number_input(text, value = start_val, step = 1, min_value = 1, key = 'number_units'))

	faturamento = np.sum([location.number_input(f'Quarto #{i+1} Aluguel Por Mês ($)', value = 1_350, step = 10, min_value = 1) for i in range(unit_count)])
	
	const.spacer(['subhead'], location)

	st.sidebar.title('Visão Geral do Faturamento')
	
	const.spacer('text', st.sidebar)
	
	st.sidebar.write(f'Faturamento Bruto: ${faturamento:,.0f} Por Mês')

	return {const.tipo_propriedade: tipo_propriedade, const.faturamento: faturamento}

# Faturamento bruto
def faturamento_bruto(model_dict, location=st):
	
	const.spacer(['title', 'head'], location)

	taxa_desocupacao = location.number_input('Taxa de Desocupação (%)', 
										     min_value = 1., 
										     max_value = 30., 
										     value = const.percentages[model_dict[const.tipo_propriedade]][const.taxa_desocupacao], 
										     step = 0.5)

	model_dict[const.taxa_desocupacao] = taxa_desocupacao

	fundo_desocupacao = model_dict[const.faturamento] * (taxa_desocupacao / 100)
	
	model_dict[const.fundo_desocupacao] = fundo_desocupacao
	
	location.write(f'Para o fundo de desocupação a cada mês: **${fundo_desocupacao:,.2f}**')

	faturamento_bruto = model_dict[const.faturamento] - fundo_desocupacao
	
	model_dict[const.faturamento_bruto] = faturamento_bruto
	
	st.sidebar.write(f'Faturamento Líquido: ${faturamento_bruto:,.0f} Por Mês')

	const.line(location)
	return model_dict

# Cálculo do faturamento
def calc_faturamento_bruto(data, location=st):

	location.title('Faturamento 💸')
	
	model_dict = property_units_inputs(location)
	
	model_dict = faturamento_bruto(model_dict, location)

	data.tipo_propriedade = model_dict[const.tipo_propriedade]
	data.faturamento = model_dict[const.faturamento]
	data.taxa_desocupacao = model_dict[const.taxa_desocupacao]
	data.fundo_desocupacao = model_dict[const.fundo_desocupacao]
	data.faturamento_bruto = model_dict[const.faturamento_bruto]
	
	return data
