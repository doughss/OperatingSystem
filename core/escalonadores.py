# -*- coding: utf-8 -*-

from time import time, sleep

from .processador import Processador

class Escalonador_Fifo(object):
    """
        Define uma classe que representa um escalonador fifo.
    """


    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria     = memoria
        self.processos   = []


    def escalonar_processos(self):
        """
            Método para iniciar a execução e escalonamento dos
            proecessos por meio de métodos auxiliares.
        """
        if self.processos:
            self.excecutar_processo()
            processo = self.processo_em_execucao()
            print "Processo {0} {1}...".format(processo.pid,
                                               processo.status_do_processo())
            segundos = 1
            while (processo.tempo_em_execucao < processo.tempo_do_processo):
                # o processo fica em execução até o tempo de execução ser igual
                # ao tempo de execução
                sleep(1)
                processo.tempo_em_execucao += 1
                print "{0} s".format(segundos)
                segundos += 1
            self.finaliza_processo(processo)


    def excecutar_processos(self):
        """
            Método que pega o primeiro processo da fila de processos, e
            adiciona um processo na memoria através do metodo first fit
            se o algoritmo first fit alocar o processo configura
            informções de execução do processo caso contrário devolve o processo para
            a lista deprocessos do escalonador.
        """
        processo              = self.processos.pop(0)
        processo_alocado      = self.first_fit(processo)
        if processo:
            processo.estado       = 1
            processo.tempo_inicio = int(time())
        else:
            self.processos.append(processo)


    def first_fit(self,processo):
        """Método first fit para alocar porcesso na Memória."""
        for pagina in self.memoria.paginas:
            if not pagina.processo and pagina.tamanho >= processo.tamanho:
                pagina.processo = processo
                return True
        return False


    def processo_em_execucao(self):
        """
            Pega o atual processo em execução no processador
        """
        return self.processador.processo_em_execucao


    def finaliza_processo(self, processo):
        """
            Método para finalizar e remover um dado processo.
        """
        proc = self.processador.processo_em_execucao
        print "Processo {0} Finalizado\n".format(proc.pid)
        #retira  o processo do processador
        self.processador.processo_em_execucao = None


class Escalonador_Round_Robin(object):
    """
        Define uma classe que representa um escalonador Round Robin.
    """


    def __init__(self, processador, memoria, quantum):
        self.processador = processador
        self.memoria     = memoria
        self.quantum     = quantum
        self.processos   = []


    def escalonar_processos(self):
        """
            Método para iniciar a execução e escalonamento dos
            proecessos.
        """
        if self.processos:
            self.excecutar_processo()
            processo = self.processo_em_execucao()
            print "Processo {0} {1}...".format(processo.pid,
                                               processo.status_do_processo())
            segundos = 1
            while (processo.tempo_em_execucao < self.quantum and\
                   processo.tempo_em_execucao < processo.tempo_do_processo and\
                   processo.tempo_executado   < processo.tempo_do_processo):
                sleep(1)
                processo.tempo_em_execucao += 1
                processo.tempo_executado   += 1
                print "{0} s".format(segundos)
                segundos += 1
            if processo.tempo_executado == processo.tempo_do_processo:
                self.finaliza_processo(processo)
            else:
                processo.estado = 0
                self.processos.append(processo)


    def excecutar_processo(self):
        """
            Método que pega o primeiro processo da fila de processos, configura
            informções de execução do processo e o coloca no processador.
        """
        processo                   = self.processos.pop(0)
        processo.estado            = 1
        processo.tempo_em_execucao = 0
        if not processo.tempo_inicio:
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
        proc = self.processador.processo_em_execucao
        print "Processo {0} Finalizado\n".format(proc.pid)
        #retira  o processo do processador
        self.processador.processo_em_execucao = None
