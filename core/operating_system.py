__author__ = 'douglas'

from .process import Process


class OperatingSystem(object):
    """
        Define a class to represents an operating system object.
    """
    def __init__(self,escalonador):
        self.processes_list = []
        self.escalonador = escalonador

    def add_process_in_list(self,process):
        """Method to add any process in the operating system's processes list."""
        self.processes_list.append(process)

    def create_process(self):
        """Method to create any process to be executed on the operating system."""
        process = Process()
        return process




