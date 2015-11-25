# -*- coding: utf-8 -*-

__author__ = 'douglas'

from core.sistema import SistemaOperacional


###########################################
##MAIN FILE TO INITIALIZE THE PROJECT
###########################################


if __name__ == 'main':
    so = SistemaOperacional()

    so.criar_processo(14)
    so.criar_processo(15)
    so.criar_processo(16)
    so.criar_processo(12)
    so.criar_processo(20)
    so.criar_processo(19)
    so.criar_processo(10)

    so.start_sistema_operacional()
