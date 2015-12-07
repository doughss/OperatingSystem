# -*- coding: utf-8 -*-

class Pagina(object):

    def __init__(self,tamanho, numero):
        self.numero   = numero
        self.tamanho  = tamanho
        self.processo = None
        self.alocado  = False

    def __repr__(self):
        """
            Representação de um objeto em uma string
        """
        string  = "Pagina {0} - tamanho:{1} ".format(self.numero, self.tamanho)
        return string
