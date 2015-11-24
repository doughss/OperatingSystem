from .sistema import SistemaOperacional

class Escalonador(object):
    """
        Define a class to represents a round-robin scheduler for the operating system.
    """

    def __init__(self,processos):
        self.processos            = []
        self.processos_bloqueados = []
        self.em_execucao          = None
        self.quantum              = quantum
        
    def executar():
        if not self.tempo_inicio:
            #atribui o tempo ao qual o processo comecou
            self.tempo_inicio = int(time())

        while self.tempo_inicio < self.tempo_do_processo:
            sleep(1)
            self.tempo_em_execucao += 1
            self.tempo_executado   += 1
