from time import time, sleep

class Processo(object):
    """
        Define a class to represents a process on the operating system.
    """
    def __init__(self,tempo):
	    self.estado             = 0 #0 = Pronto, 1 = Executando, 2 = Bloqueado
	    self.dados              = ""
	    self.pid                = 1
	    self.tempo_do_processo  = tempo
	    self.tempo_inicio       = 0
	    self.tempo_em_execucao  = 0
	    self.tempo_executado    = 0

	def executar():
		if not self.tempo_inicio:
			#atribui o tempo ao qual o processo começou
			self.tempo_inicio = int(time())
		
		while self.tempo_inicio < self.tempo_do_processo:
			sleep(1)
			self.tempo_em_execucao += 1
			self.tempo_executado   += 1

