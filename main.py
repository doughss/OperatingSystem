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

    escalonamento={0:"Escalonamento RoundRobin" , 1:"Escalonaemnto Fifo"}
    escalonador = -1
    while escalonador!=0 and escalonador!=1:
        escalonador = int(raw_input("Deseja Escalonamento RoundRobin(0) ou Fifo(1)? "))
    print(escalonamento[escalonador])

    so = SistemaOperacional(memoria,escalonador)

    so.criar_processo(14,10)
    so.criar_processo(15,11)
    so.criar_processo(16,12)
    so.criar_processo(12,13)
    so.criar_processo(20,14)
    so.criar_processo(19,15)
    so.criar_processo(10,16)

    so.start_sistema_operacional()
