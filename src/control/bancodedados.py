class Arquivo:
	def __init__(self, *kwargs):
		self.pastas = [ './data/database/tables/create/',
						'./data/database/querrys/insert/',
						'./data/database/querrys/select/']

		self.arquivos = [self.pastas[0]+'CLIENTE.sql',
						 self.pastas[0]+'CARRO.sql',
						 self.pastas[0]+'POSTO.sql',
						 self.pastas[0]+'BOMBA.sql',
						 self.pastas[0]+'ABASTECIMENTO.sql',

						 self.pastas[1]+'CLIENTE.sql',
						 self.pastas[1]+'CARRO.sql',
						 self.pastas[1]+'POSTO.sql',
						 self.pastas[1]+'BOMBA.sql',
						 self.pastas[1]+'ABASTECIMENTO.sql',

						 self.pastas[2]+'mostrarAQuantidadeDeCombustivelEOTipoQueForamVendidosEmUmPosto.sql',
						 self.pastas[2]+'mostrarAQuantidadeDeVezesQueOsClientesAbasteram.sql',
						 self.pastas[2]+'mostrarAQuantidadeDeVezesQueUmCliente.sql',
						 self.pastas[2]+'mostrarAsVendasPorMes.sql',
						 self.pastas[2]+'mostrarClientesPorOrdemAlfabetica.sql',
						 self.pastas[2]+'mostrarClientesQueAbasteceramComUmTipoDeGasolina.sql',
						 self.pastas[2]+'mostrarClientesQueAbasteceramEmUmaBomba.sql',
						 self.pastas[2]+'mostrarClientesQueAbasteceramEmUmMes.sql',
						 self.pastas[2]+'mostrarClientesQueAbasteceramEmUmOuMaisPostos.sql',
						 self.pastas[2]+'mostrarClientesQueAbasteceramUmValorMaiorQue.sql',
						 self.pastas[2]+'mostrarHistoricoDoClientePorCpf.sql',
						 self.pastas[2]+'mostrarNotaParaOCliente.sql',
						 self.pastas[2]+'mostrarQualCombustivelVendeuMais.sql'
						 ]

		self.indiceDoArquivo = -1
	
	def obterCaminhos(self):
		return self.pastas

	def obterArquivos(self):
		return self.arquivos

	def atualizarIndice(self, sentido=None):
		if self.indiceDoArquivo >= -1:
			if sentido == '+':
				self.indiceDoArquivo += 1

		if self.indiceDoArquivo > -1:
			if sentido == '-':
				self.indiceDoArquivo -= 1

	def validarIndice(self):
		try:
			self.arquivos[self.indiceDoArquivo]
			return True
		except:
			return False

	def obterArquivo(self, sentido=None):
		if self.validarIndice() == False:
			self.atualizarIndice('-')

		self.atualizarIndice(sentido)

		if self.indiceDoArquivo != -1:
			indice = self.indiceDoArquivo
		else:
			return None

		try:
			return self.arquivos[indice]
		except:
			pass

	def abrirArquivo(self, arquivo):
		try:
			arqv = open(arquivo)
			arq = arqv.read()
			arqv.close()
			return arq
		except:
			return None
