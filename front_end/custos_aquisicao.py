# Módulo de custos de aquisição

# Imports
import pandas as pd
import numpy_financial as npf
import streamlit as st
from calendar import monthrange
import front_end.constantes as const

# Função para calcular outras despesas
def other_expense(number, data, location=st):
	name = location.text_input(f'#{number} - Descrição de Custo/Reparo:', '-')
	amount = location.number_input(f"#{number} - {name} ($)", min_value = 0, max_value = 10_000, value = 0, step = 1)
	const.spacer('text', location) 
	return {name: amount}

# Função de inputs dos custos de aquisição
def get_acquisition_inputs(data, location=st):

	data.taxa_corretora = location.number_input('Taxa da Corretora de Imóveis ($)',
		min_value = 0.,
		max_value = data.loan_amount * 0.99,
		value = data.loan_amount * 0.01,
		step = 10.,
		key = 'taxa_corretora')

	data.avaliacao = location.number_input('Taxa de Avaliação do Imóvel ($)',
		min_value = 0,
		max_value = 5_000,
		value = 750,
		step = 10,
		key = 'avaliacao')

	data.titulo_seguro = location.number_input('Taxa de Título de Seguro ($)',
		min_value = 0,
		max_value = 5_000,
		value = 1000,
		step = 10,
		key = 'seguro')

	days_per_month = monthrange(data.closing_date.year, data.closing_date.month)[-1]
	
	ipmt = npf.ipmt(rate = data.taxa_juros/100/12,
		per = 1.,
		nper = data.periodo_amortizacao * 12,
		pv =- data.loan_amount)

	data.juros = location.number_input('Juros Pré-Pagos ($)',
		min_value = 0.,
		max_value = float(data.pmt),
		value = float(ipmt * ((days_per_month - data.closing_date.day) / days_per_month)),
		step = 1.,
		key = 'juros')

	data.poupanca = location.number_input('Poupança de Imposto Sobre a Propriedade ($)',
		min_value = 0.,
		max_value = float(data.taxa_propriedade * 12),
		value = float(data.taxa_propriedade * 4),
		step = float(data.taxa_propriedade),
		key = 'poupanca')

	data.garantia_seguro = location.number_input('Garantia de Seguro ($)',
		min_value = 0.,
		max_value = float(data.seguro * 12),
		value = float(data.seguro * 4),
		step = float(data.seguro),
		key = 'garantia_seguro')

	data.inspecao = location.number_input('Inspeção (ões) de Propriedade ($)',
		min_value = 0,
		max_value = 2_000,
		value = 750,
		step = 10,
		key = 'inspecao')

	location.subheader('Outros Custos e Reparos')

	unit_count = int(location.number_input('Número de Custos Adicionais/Reparos',
		min_value = 0,
		max_value = 100,
		value = 0,
		step = 1))

	const.spacer('write', location)

	_ = [data.acquisition_dict.update(other_expense(i+1, data, location)) for i in range(unit_count)]

	return data

# Mostra os resultados
def display_results(data, location=st):
	
	st.sidebar.title('Visão Geral dos Custos de Aquisição')
	
	const.spacer('text', st.sidebar)
	
	location.write(f'**Total dos Custos de Aquisição:** ${data.acquisition:,.2f}')
	
	if location.checkbox('Visualizar os Custos:'):
		for key, val in data.acquisition_dict.items():
			if val > 0:
				key = key.replace('_', ' ').title()
				location.text(f'{key}: ${val:,.2f}')

		const.line(st.sidebar)

	data.entrada = data.down_pmt + data.acquisition
	
	location.write(f'**Investimento Para Fechar o Negócio Hoje:** ${data.entrada:,.0f}')
	
	const.line(st.sidebar)

# Calcula os custos de aquisição
def calc_acquisition(data, location=st):
	
	location.header('Custos de Aquisição 💰')

	data = get_acquisition_inputs(data, location)
	data.combine_acquisition_costs()
	const.line(location)
	display_results(data, st.sidebar)

	return data

	