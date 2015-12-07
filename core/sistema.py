# -*- coding: utf-8 -*-

__author__ = 'douglas'

from time           import time

from .processo      import Processo
from .escalonadores import Escalonador_Fifo, Escalonador_Round_Robin
from .processador   import Processador



class SistemaOperacional(object):
    """
        Define a classe que representa um sistema operacional.
    """

    def __init__(self,memoria):
        """
            Construtor da classe SistemaOperacional.
        """
        self.memoria = memoria
        self.processador = Processador()
        self.escalonador = Escalonador_Round_Robin(self.processador, 5)

    def criar_processo(self, tempo_do_processo,tamanho):
        """
            Método para criar qualquer processo a ser executedo no so.
        """
        pid      = len(self.escalonador.processos) + 1
        processo = Processo(pid, tempo_do_processo, tamanho)
        self.escalonador.processos.append(processo)

    def start_sistema_operacional(self):
        """
            Método de start do Sistema Operacional
        """
        print "Sistema Operacional em execucao"
        while self.escalonador.processos :
            print self.tabela_de_processos()
            self.escalonador.escalonar_processos()
        print "Sistema Operacional finalizado"
        return False


    def tabela_de_processos(self):
        """
            Método para formtação da tabela de processos
        """
        tabela  = "##############################################\n"
        tabela += "## id | Tempo de execucao | Tempo executado ##\n"
        tabela += "##############################################\n"
        for processo in self.escalonador.processos:
            tabela += "### {0} |".format(processo.pid)
            tabela += "        {0}         |".format(processo.tempo_do_processo)
            tabela += "       {0}        ###\n".format(processo.tempo_executado)
        tabela += "##############################################\n"
        return tabela
