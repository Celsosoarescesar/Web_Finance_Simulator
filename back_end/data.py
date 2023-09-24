# Back-end

# Imports
import numpy as np
import streamlit as st

# Classe para o modelo de dados
class ModelData:

	# Construtor
	def __init__(self):

		self.model_dict = {}

		self.percentages = {'residencial': {'taxa_desocupacao': 5., 'manutencao': 3., 'gerenciamento': 5.},
							'comercial': {'taxa_desocupacao': 10., 'manutencao': 10., 'gerenciamento': 7.5}}

		# Faturamento
		self.tipo_propriedade = 'tipo_propriedade'
		self.faturamento = 'faturamento'
		self.taxa_desocupacao = 'taxa_desocupacao'
		self.fundo_desocupacao = 'fundo_desocupacao'
		self.faturamento_bruto = 'faturamento_bruto'

		# Financiamento
		self.preco_compra = 'preco_compra'
		self.taxa_juros = 'taxa_juros'
		self.periodo_amortizacao = 'periodo_amortizacao'
		self.pct_down = 'pct_down'
		self.down_pmt = 'down_pmt'
		self.loan_amount = 'loan_amount'
		self.pmt = 'pmt'
		self.closing_date = 'closing_date'

		# OPEX
		self.taxa_imposto_propriedade = 'taxa_imposto_propriedade'
		self.taxa_propriedade = 'taxa_propriedade'
		self.seguro = 'seguro'
		self.city_water = 'city_water'
		self.electric = 'electric'
		self.natural_gas = 'natural_gas'
		self.garbage = 'garbage'
		self.hoa = 'hoa'
		self.expenses_dict = {}
		self.taxa_manutencao = 'taxa_manutencao'
		self.fundo_manutencao = 'fundo_manutencao'
		self.taxa_gerenciamento = 'taxa_gerenciamento'
		self.fundo_gerenciamento = 'fundo_gerenciamento'
		self.net_op_income = 'net_op_income'
		self.profit = 'profit'

		# Custo de aquisição
		self.taxa_corretora = 'taxa_corretora'
		self.avaliacao = 'avaliacao'
		self.titulo_seguro = 'titulo_seguro'
		self.juros = 'juros'
		self.poupanca = 'poupanca'
		self.garantia_seguro = 'garantia_seguro'
		self.inspecao = 'inspecao'
		self.acquisition_dict = {}
		self.entrada = 'entrada'

		# Resultado
		self.cocr = 'cash-on-cash_return'

	# Método para combinar as despesas
	def combine_expenses(self):
		self.expenses_dict['taxa_propriedade'] = self.taxa_propriedade
		self.expenses_dict['seguro'] = self.seguro
		self.expenses_dict['city_water_&_sewer'] = self.city_water
		self.expenses_dict['electric'] = self.electric
		self.expenses_dict['natural_gas'] = self.natural_gas
		self.expenses_dict['garbage'] = self.garbage
		self.expenses_dict['hoa'] = self.hoa
		self.expenses_dict['fundo_manutencao'] = self.fundo_manutencao
		self.expenses_dict['fundo_gerenciamento'] = self.fundo_gerenciamento

		self.opex = np.sum([val for key, val in self.expenses_dict.items()])

	# Método para combinar os custos de aquisição
	def combine_acquisition_costs(self):
		self.acquisition_dict['taxa_corretora'] = self.taxa_corretora
		self.acquisition_dict['avaliacao'] = self.avaliacao
		self.acquisition_dict['titulo_seguro'] = self.titulo_seguro
		self.acquisition_dict['juros'] = self.juros
		self.acquisition_dict['poupanca'] = self.poupanca
		self.acquisition_dict['garantia_seguro'] = self.garantia_seguro
		self.acquisition_dict['inspecao'] = self.inspecao

		self.acquisition = np.sum([val for key, val in self.acquisition_dict.items()])

	# Método para space
	def spacer(self, space_type, location=st):
		if 'title' in space_type:
			location.title('')
		if 'head' in space_type:
			location.header('')
		if 'subheader' in space_type:
			location.subheader('')

	# Método para linha
	def line(self, location=st):
		location.write('_____')




