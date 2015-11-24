__author__ = 'douglas'

from .processo      import Processo
from .escalonadores import Escalonador_Fifo, Escalonador_Round_Robin
from time           import time

class SistemaOperacional(object):
    """
        Define a classe que representa um sistema operacional.
    """

    def __init__(self):
        """
            Construtor da classe SistemaOperacional.
        """
        self.processador = Processador()
        self.escalonador = Escalonador_Fifo(processador)

    def criar_processo(self, tempo_do_processo):
        """
            Método para criar qualquer processo a ser executedo no so.
        """        
        pid      = len(self.escalonador.processos) + 1
        processo = Processo(pid, tempo_do_processo)
        self.escalonador.processos.append(processo)

    def start_sistema_operacional():
        """
            Método de start do Sistema Operacional
        """
        print "Sistema Operacional em execução"
        while True:
            #Doing Samithing
            continue

        print "Sistema Operacional finalizado"
    return False
