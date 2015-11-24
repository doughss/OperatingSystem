from time import time, sleep

class Processo(object):
    """
        Define a class to represents a process on the operating system.
        status de um processo :
        0 = Pronto
        1 = Executando
        2 = Bloqueado
    """
    
    def __init__(self,tempo,pid):
        self.pid                = pid
        self.estado             = 0
        self.tempo_do_processo  = tempo
        self.tempo_inicio       = 0
        self.tempo_em_execucao  = 0
        self.tempo_executado    = 0
