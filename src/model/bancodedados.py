import sqlite3

class RedeMeio:
	def __init__(self, nomeDoBancoDeDados, *kwarg):
		self.conexcao = sqlite3.connect(nomeDoBancoDeDados)
		self.cursor = self.conexcao.cursor()
		self.resultado_bd = ""

	def executarComando(self, comando):
		try:
			self.cursor.execute(comando)
			self.resultado_bd = self.cursor.fetchall()
		except:
			self.resultado_bd = ["Erro", self.cursor.fetchall()]

	def salvarModificacao(self):
		self.conexcao.commit()

	def resultadoDoComando(self):
		return self.resultado_bd 

	def fechar(self):
		self.conexcao.close()
