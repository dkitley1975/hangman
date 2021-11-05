import os
from time import sleep


# define clear function - information initally searched from Stackoverflow
def clear_terminal():
    """
    Clears the terminal screen after 1 second
    """
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
