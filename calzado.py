from ropa import Ropa

# SubClase Calzado 
# Crea instancias de calzados que tienen un talle, producto, codigo, precio, y un tipo''' 
class Calzado(Ropa):
	def __init__(self, talle, precio, codigo, producto, tipo):
		self.tipo = tipo
		super().__init__(talle, precio, codigo, producto)
		

