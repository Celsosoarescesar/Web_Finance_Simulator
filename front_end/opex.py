# Módulo OPEX - Despesas de Operação

# Imports
import numpy as np
import pandas as pd
import streamlit as st
import front_end.constantes as const

# Função para despesas gerais
def other_expense(number, data, location=st):
	
	name = location.text_input(f'#{number} - Descrição da Despesa:', '-')
	
	amount = location.number_input(f"#{number} - {name} ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)
	
	const.spacer('text', location)

	return {name: amount}

# Inputs Opex
def get_opex_inputs(data, location=st):
	
	data.taxa_imposto_propriedade = location.number_input("Taxa de Imposto de Propriedade do Seu Estado (%)", min_value = 0., max_value = 15., value = 0.65, step = 0.01)
	
	data.taxa_propriedade = data.preco_compra * (data.taxa_imposto_propriedade/100)/12
	
	location.text(f'Taxa de Imposto de Propriedade Por Mês: ${data.taxa_propriedade:,.2f}')

	data.seguro = location.number_input("Seguro ($ Por Mês)", min_value = 25, max_value = 10_000, value = 100, step = 1)

	data.hoa = location.number_input("Taxas Extras ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)

	data.taxa_manutencao = location.number_input("Taxa de Manutenção (%)", 
												  min_value = 1., 
												  max_value = 99., 
												  value = const.percentages[data.tipo_propriedade]['manutencao'], 
												  step = 0.05)
	
	data.fundo_manutencao = data.faturamento_bruto * data.taxa_manutencao / 100
	
	location.text(f'Fundo de Manutenção Por Mês: ${data.fundo_manutencao:,.2f}')

	data.taxa_gerenciamento = location.number_input("Taxa de Manutenção (%)", 
												 min_value = 0., 
												 max_value = 99., 
												 value = const.percentages[data.tipo_propriedade]['gerenciamento'], 
												 step = 0.05)
	
	data.fundo_gerenciamento = data.faturamento_bruto * data.taxa_gerenciamento/100
	
	location.text(f'Taxa de Condomínio Por Mês: ${data.fundo_gerenciamento:,.2f}')

	location.subheader('Utilidades')
	
	data.city_water = location.number_input("Água e Esgoto ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)

	data.electric = location.number_input("Eletricidade ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)

	data.natural_gas = location.number_input("Gás Natural ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)

	data.garbage = location.number_input("Coleta de Lixo ($ Por Mês)", min_value = 0, max_value = 10_000, value = 0, step = 1)

	location.subheader('Despesas Gerais')

	unit_count = int(location.number_input('Número Adicional de Despesas', min_value = 0, max_value = 100, value = 0, step = 1))
	
	const.spacer('write', location)

	_ = [data.expenses_dict.update(other_expense(i+1, data, location)) for i in range(unit_count)]

	return data

# Função para mostrar os resultados
def display_results(data, location=st):
	
	st.sidebar.title('OPEX - Despesas de Operação')
	
	const.spacer('text', st.sidebar)
	
	location.write(f'**Total OPEX:** ${data.opex:,.2f} Por Mês')
	
	if location.checkbox('Despesas:'):
		for key, val in data.expenses_dict.items():
			if val > 0:
				key = key.replace('_', ' ').title()
				location.text(f'{key}: ${val:,.2f} Por Mês')

		const.line(st.sidebar)

	data.net_op_income = data.faturamento_bruto - data.opex
	location.write(f'**Custo Operacional Líquido:** ${data.net_op_income:,.0f} Por Mês')
	const.line(st.sidebar)

# Função de cálculo do Opex
def calc_opex(data, location=st):
	
	location.header('Despesas de Operação 💲')

	data = get_opex_inputs(data, location)
	
	data.combine_expenses()

	display_results(data, st.sidebar)

	const.line(location)

	data.profit = data.net_op_income - data.pmt

	return data


	