from time import time

from .processador import Processador

class Escalonador_Fifo(object):
    """
        Define uma classe que representa um escalonador fifo.
    """


    def __init__(self, processador):
        self.processador          = processador
        self.processos            = []


    def escalonar_processos(self):
        """
            Método para iniciar a execução e escalonamento dos
            proecessos por meio de métodos auxiliares.
        """
        if processos:
            self.excecutar_processo()
            processo = processo_em_execucao()
            while (processo.tempo_em_execucao < processo.tempo_do_processo):
                sleep(1)
                self.tempo_em_execucao += 1
            self.finaliza_processo(processo)

    def excecutar_processo(self):
        """
            Método que pega o primeiro processo da fila de processos, configura
            informções de execução do processo e o coloca no processador.
        """
        processo              = self.processos.pop[0]
        processo.estado       = 1
        processo.tempo_inicio = int(time())
        self.processador.processo_em_execucao = processo

    def processo_em_execucao(self):
        """
            Pega o atual processo em execução no processador
        """
        return self.processador.processo_em_execucao

    def finaliza_processo(self, processo):
        """
            Método para finalizar e remover um dado processo.
        """
        #retira  o processo do processador
        self.processador.processo_em_execucao = None
        for indice,proc in enumerate(self.processos):
            if proc.pid == processo.pid:
                #retira  o processo da lista de processos
                self.processos.pop(indice)
                break


class Escalonador_Round_Robin(object):
    """
        Define uma classe que representa um escalonador fifo.
    """

    def __init__(self, processador):
        self.processador          = processador
        self.processos            = []
        self.quantum              = quantum


    def escalonar_processos(self):



    def remover_processo(self, processo):
        """Methodo para remover um dado.  Quem remove processo é o escalonador!!!!"""
        processos = self.escalonador.processos
        for indice,proc in enumerate(processos):
            if proc.pid == processo.pid:
                processos.pop(indice)
                break
