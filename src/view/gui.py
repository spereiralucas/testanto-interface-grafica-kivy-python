import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

from src.control.bancodedados import Arquivo
from src.model.bancodedados import RedeMeio

class GerenciadorDeTelas(ScreenManager):
	pass

class Menu(Screen):
	pass

class JanelaPrincipal(Screen):
	def __init__(self, **kwarg):
		super(JanelaPrincipal, self).__init__(**kwarg)
		self.arquivo = Arquivo()
		self.redemeio = RedeMeio('RedeMeio.db')

	def regressarArquivo(self):
		self.arquivo.obterArquivo(sentido='-')
		self.atualizarTelaDeResultado('...')

	def avancarArquivo(self):
		self.arquivo.obterArquivo(sentido='+')
		self.atualizarTelaDeResultado('...')

	def atualizarTituloDaQuerry(self):
		if self.arquivo.indiceDoArquivo == -1:
			titulo = "Criar Banco De Dados"
		else:
			titulo = self.arquivo.obterArquivo(sentido=None)
		self.ids.tituloDaQuerry.text = titulo

	def atualizarCodeInput(self):
		codigo =  self.arquivo.abrirArquivo(self.ids.tituloDaQuerry.text)
		if codigo == None:
			codigo = "def criarBancoDeDados(self, nomeDoBancoDeDados):\n\ttry:\n\t\tself.con = sqlite3.connect(nomeDoBancoDeDados)\n\t\tprint(""Banco De Dados Criado Com Sucesso"")\n\texcept:\n\t\tprint(""Erro"")\ncriarBancoDeDados(""RedeMeio.bd"")"
		self.ids.codeInput.text = codigo

	def atualizarTelaDeResultado(self, resultado=None):
		try:
			if resultado != None:
				print("====")
				print(resultado)
				self.ids.telaDeResultado.text = resultado
			if resultado == None:
				res = self.redemeio.resultadoDoComando()
				print('53')
				self.ids.telaDeResultado.text = str(res)

		except:
			self.ids.telaDeResultado.text = "Erro"

	def executarComando(self):
		codigo = self.ids.codeInput.text

		if self.arquivo.indiceDoArquivo == -1:
			self.atualizarTelaDeResultado(resultado='Banco De Dados Criado Com Sucesso')
		else:
			self.redemeio.executarComando(codigo)
			self.atualizarTelaDeResultado()

	def salvarModificacao(self):
		self.redemeio.salvarModificacao()

	def on_leave(self, *kwarg):
		try:
			tecla = kwarg[1]
			print(tecla)
			if tecla == 27:
				self.redemeio.fechar()
				Gui().stop()
		except:
			pass

	def on_pre_enter(self, **kwargs):
		Window.bind(on_keyboard=self.on_leave)

class Gui(App):
	def build(self):
		return GerenciadorDeTelas()
