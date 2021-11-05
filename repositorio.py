import sqlite3

class Repositorio:
    #Consulta y escribe en el BD. Clase madre de los otros repositorios

    def __init__(self):
        self.bd = sqlite3.connect("bd.sqlite")
        self.cursor = self.bd.cursor()
        
