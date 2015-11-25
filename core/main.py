__author__ = 'douglas'

from .escalonador import Escalonador
from .sistema import SistemaOperacional


###########################################
##MAIN FILE TO INITIALIZE THE PROJECT
###########################################


if __name__ == 'main':
    so = SistemaOperacional()
    so.start_sistema_operacional()
