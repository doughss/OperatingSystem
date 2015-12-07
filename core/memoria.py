# -*- coding: utf-8 -*-
from random import randint

from .pagina import Pagina


class Memoria(object):
    """
        Define a classe que representa a memoria no sistema operacional.
    """

    def __init__(self):
        self.paginas  = []


    def criar_paginas(self, tamanho_minimo, tamanho_maximo, quantidade):
        """
            Metodo para criar X páginas aleatórias com um tamanho minimo
            e um tamanho máximo
        """
        numero = 1
        for i in range(quantidade):
            tamanho = randint(tamanho_minimo,tamanho_maximo)
            pagina = Pagina(tamanho,numero)
            self.paginas.append(pagina)
            numero +=1

    def tem_processos_executando(self):
        """Método para checar se a memoria possui algum processo em execução"""
        for  pagina in self.paginas:
            if pagina.processo:
                return True
        return False
