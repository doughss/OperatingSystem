from .sistema import SistemaOperacional

class Escalonador(object):
    """
        Define a class to represents a round-robin scheduler for the operating system.
    """

    def __init__(self):
        super(Escalonador, self).__init__()

    def rr(self,so):
        