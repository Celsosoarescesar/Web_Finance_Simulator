# Módulo para os resultados

# Imports
import pandas as pd
import streamlit as st
import front_end.constantes as const

# Cálculo de métricas
def calc_display_basic_metrics(data, location=st):
	
	const.spacer('title')
	
	location.subheader(f'Total de Dinheiro Investido: ${data.entrada:,.0f}')

	if data.profit < 0:
		location.subheader(f'❌ **Prejuízo** Por Mês: ${-data.profit:,.2f}')
	else:
		location.subheader(f'Lucro Por Mês: ${data.profit:,.0f}')

	data.cocr = (max(data.profit, 0)*12) / data.entrada

	location.subheader(f'Retorno Sobre o Valor Investido: {data.cocr:.1%}')

	location.subheader(f'Taxa de Endividamento: {data.net_op_income / data.pmt:,.2f}')

	if st.session_state.number_units > 1:
		location.write(f'Lucro Médio Por Unidade Por Mês: ${max(data.profit, 0) / st.session_state.number_units:,.0f}')
		location.write(f'Custo Médio Por Unidade: ${data.preco_compra / st.session_state.number_units:,.0f}')

	location.write(f'Taxa de Capitalização: {(data.net_op_income * 12) / data.preco_compra:.1%}')
	
	location.write(f'Gross Rent Multiplier (Tempo Para o Investimento Se Pagar): {data.preco_compra / (data.faturamento_bruto * 12):.2f}')
	
	# GRM é é a razão entre o preço de um investimento imobiliário e sua receita anual de aluguel antes de contabilizar despesas como impostos sobre propriedades, 
	# seguros e serviços públicos; GRM é o número de anos que a propriedade levaria para se pagar com o aluguel bruto recebido.

# Mostra os resultados
def display_all_results(data, location=st):
	location.title('Analytics 🤔')

	calc_display_basic_metrics(data, location)

	return data
