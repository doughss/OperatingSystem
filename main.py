# -*- coding: utf-8 -*-

__author__ = 'douglas'

from core.sistema import SistemaOperacional
from core.memoria import Memoria


###########################################
##MAIN FILE TO INITIALIZE THE PROJECT
###########################################


if __name__ == '__main__':
    memoria = Memoria()
    memoria.criar_paginas(10,20,5)

    so = SistemaOperacional(memoria)

    so.criar_processo(14,10)
    so.criar_processo(15,11)
    so.criar_processo(16,12)
    so.criar_processo(12,13)
    so.criar_processo(20,14)
    so.criar_processo(19,15)
    so.criar_processo(10,16)

    so.start_sistema_operacional()
