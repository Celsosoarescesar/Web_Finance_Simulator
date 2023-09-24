
# Web_Finance_Simulator
import streamlit as st
from streamlit_option_menu import option_menu

# Imports
from datetime import datetime
import streamlit as st
import front_end.constantes as const
from front_end.financiamento import calc_financing
from front_end.faturamento import calc_faturamento_bruto
from front_end.opex import calc_opex
from front_end.custos_aquisicao import calc_acquisition
from front_end.analytics import display_all_results
from back_end.data import ModelData

# Função de configuração da página
def page_config():
	st.set_page_config(page_title = 'Web_Finance_Simulator', 
					   page_icon = '🚀', 
					   layout = 'centered', 
					   initial_sidebar_state = 'auto')

	st.title('Web_Finance_Simulator')
	const.spacer('title')
	const.spacer('title')
	st.sidebar.text('Web_Finance_Simulator')
	st.sidebar.text(datetime.today().strftime('%B %d, %Y'))
	const.spacer('title', st.sidebar)

# Função para o rodapé
def page_footer():
	const.spacer('title', st.sidebar)
	const.spacer('title', st.sidebar)
	const.spacer('title', st.sidebar)
	st.sidebar.text('v1.0.0')
	st.sidebar.text('Projeto Final')

# Função main
def main():
	
	# Cria o modelo de dados
	data = ModelData()

	# Config
	page_config()

	# Executa os cálculos
	data = calc_faturamento_bruto(data)
	data = calc_financing(data)
	data = calc_opex(data)
	data = calc_acquisition(data)
	data = display_all_results(data)

	# Rodapé
	page_footer()

# Executa a app
if __name__ == '__main__':
	main()



	


