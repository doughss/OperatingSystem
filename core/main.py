__author__ = 'douglas'

from .scheduler import Scheduler
from .operating_system import OperatingSystem


###########################################
##MAIN FILE TO INITIALIZE THE PROJECT
###########################################


if __name__ == 'main':

    escalonador = Scheduler()
    operating_system = OperatingSystem(escalonador)

