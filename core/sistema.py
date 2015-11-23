__author__ = 'douglas'

from .processo import Processo


class SistemaOperacional(object):
    """
        Define a class to represents an operating system object.
    """
    quantum = 4
    def __init__(self,escalonador):
        self.processos = []
        self.escalonador = escalonador

    def criar_processo(self, dados):
        """Method to create any process to be executed on the operating system."""
        proc = Processo()
        proc.dados = dados
        proc.codigo = len(self.processos) + 1
        self.processos.append(proc)
        return "Processo criado"

    def matar_processo(self, pid):
        for proc in self.processos:
            if proc.pid == pid:
                self.processos.remove(proc)
                break
    