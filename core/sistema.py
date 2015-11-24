__author__ = 'douglas'

from .processo import Processo
from time      import time

class SistemaOperacional(object):
    """
        Define a classe que representa um sistema operacional.
    """

    def __init__(self, escalonador, quantum):
        self.escalonador          = escalonador

    def criar_processo(self, dados):
        """Methodo para criar qualquer processo a ser executedo
           no so."""
        tempo           = time()
        pid             = len(self.escalonador.processos) + 1
        processo        = Processo(tempo, pid)
        self.escalonador.processos.append(processo)

    def remover_processo(self, processo):
        processos = self.escalonador.processos
        for indice,proc in enumerate(processos):
            if proc.pid == processo.pid:
                processos.pop(indice)
                break
