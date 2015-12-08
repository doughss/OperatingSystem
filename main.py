# -*- coding: utf-8 -*-

__author__ = 'douglas'

from core.sistema import SistemaOperacional


###########################################
##MAIN FILE TO INITIALIZE THE PROJECT
###########################################


if __name__ == '__main__':

    escalonamento={1:"Escalonamento RoundRobin" , 0:"Escalonaemnto Fifo"}
    escalonador = -1
    while escalonador!=0 and escalonador!=1:
        escalonador = int(raw_input("Deseja Escalonamento Fifo(0) ou RoundRobin(1)? "))

    if escalonador==1:
        quantum=-1
        while quantum<=0:
            quantum = int(raw_input("Valor do quantum: "))
        so = SistemaOperacional(escalonador,quantum)
    else:
        so = SistemaOperacional(escalonador)

    print(escalonamento[escalonador])

    so.criar_processo(14)
    so.criar_processo(15)
    so.criar_processo(16)
    so.criar_processo(12)
    so.criar_processo(20)
    so.criar_processo(19)
    so.criar_processo(10)

    so.start_sistema_operacional()
