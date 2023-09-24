# Módulo de cálculo do financiamento

# Imports
import numpy_financial as npf
import pandas as pd
import streamlit as st
import front_end.constantes as const

# Obtém os inputs
def get_financing_inputs(data, location=st):

	data.preco_compra = location.number_input('Preço de Compra ($)',
		min_value = 1,
		max_value = 100_000_000,
		value = 200_000,
		step = 100,
		key = 'preco_compra')

	data.taxa_juros = location.number_input('Taxa de Juros (%)',
		min_value = 0.1,
		max_value = 20.,
		value = 4.75,
		step = 0.01,
		key = 'taxa_juros')

	data.periodo_amortizacao = location.number_input('Período de Amortização (anos)',
		min_value = 1,
		max_value = 30,
		value = 30,
		step = 1,
		key = 'periodo_amortizacao')

	down = location.number_input('Pagamento Inicial (Entrada) (% or $)',
		min_value = 1,
		max_value = 100_000_000,
		value = 20,
		step = 1)

	if down < 100:
		location.text(f'{down:.0f}% Entrada')
		data.pct_down = down
		data.down_pmt = data.preco_compra * (down/100)
	else:
		location.text(f'${down:,.0f} Pagamento de Entrada')
		data.pct_down = (down / data.preco_compra)*100
		data.down_pmt = down

	data.loan_amount = data.preco_compra - data.down_pmt

	data.pmt = npf.pmt(rate = data.taxa_juros/100/12, nper = data.periodo_amortizacao * 12, pv =- data.loan_amount)

	data.closing_date = location.date_input('Data de Fechamento', pd.to_datetime("today") + pd.to_timedelta(30, unit = 'day'), key = 'closing_date')

	location.text(f'{max((pd.to_datetime(data.closing_date)-pd.to_datetime("today")).days, 0)} Dias Para o Fechamento')

	return data

# Função para mostrar os resultados
def display_results(data, location=st):
	const.line(st.sidebar)
	st.sidebar.title('Visão Geral do Financiamento')
	const.spacer('text', st.sidebar)
	st.sidebar.write(f'**Preço de Compra:** ${data.preco_compra:,.0f}')
	st.sidebar.write(f'**{data.pct_down}% Entrada:** ${data.down_pmt:,.0f}')
	st.sidebar.write(f'**Total de Empréstimo:** ${data.loan_amount:,.0f}')
	st.sidebar.write(f'**Pagamento do Empréstimo:** ${data.pmt:,.2f}')
	const.line(st.sidebar)


# Função de cálculo do financiamento
def calc_financing(data, location=st):
	
	location.header('Financiamento 🏦')

	data = get_financing_inputs(data, location)
	
	const.line(location)
	
	display_results(data, location)

	return data


