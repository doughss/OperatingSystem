class Processo(object):
    """
        Define a class to represents a process on the operating system.
    """
    def __init__(self,**kwargs):
	    self.estado = 0 #0 = Pronto, 1 = Executando, 2 = Bloqueado
	    self.dados = ""
	    self.pid = 1
