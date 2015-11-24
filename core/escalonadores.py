from .processador import Processador

class Escalonador_Fifo(object):
    """
        Define uma classe que representa um escalonador fifo.
    """

    def __init__(self, processador):
        self.processador          = processador
        self.processos            = []


    def escalonar_processos(self):
        if processos:
        while self.tempo_inicio < self.tempo_do_processo:
            sleep(1)
            self.tempo_em_execucao += 1
            self.tempo_executado   += 1


    def excecutar_processo(self):
        """
            Método que pega um processo da fila de processos
            e o coloca no processador.
        """
        self.processador.processo_em_execucao = self.processos.pop[0]


    def remover_processo(self, processo):
        """Methodo para remover um dado.  Quem remove processo é o escalonador!!!!"""
        processos = self.escalonador.processos
        for indice,proc in enumerate(processos):
            if proc.pid == processo.pid:
                processos.pop(indice)
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
