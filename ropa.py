class Ropa:
#Clase Madre Ropa, tiene un constructor que define el talle, precio, codigo y el producto.
	def __init__(self, talle, precio, codigo, producto):
		'''Inicializa el prenda con un talle, con precio, id'''
		self.talle = talle
		self.precio = precio
		self.codigo = codigo
		self.producto = producto

	def coincide(self, filtro):
#Metodo de busqueda		
		prendas = []
		for prenda in self.prendas:
			
			if filtro in prenda.producto:
				prendas.append(prenda)
		return prendas
