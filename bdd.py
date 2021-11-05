from ropa import Ropa
from repositorioProductos import RepositorioProductos
from calzado import Calzado

class Bdd:

#Colección de Articulos 

	def __init__(self):
		self.repo = RepositorioProductos()
		self.prendas = self.repo.get_all()


	def nuevoProducto(self, talle, precio, codigo, producto):
		#Crea un nuevo Producto y lo agrega en la lista de prendas y en la BDD
		prenda = Ropa(talle, precio, codigo, producto)
		self.repo.store(prenda)
		self.prendas.append(prenda)
		return prenda
	
	def nuevoCalzado(self, talle, precio, codigo, producto, tipo):
		#Crea un nuevo Producto (Con la clase madre Ropa) y lo agrega en la lista de prendas y en la BDD
		prenda = Calzado(talle, precio, codigo, producto, tipo)
		self.prendas.append(prenda)
		self.repo.store(prenda)
		

	def buscarPorCodigo(self, codigo):
		#Debe retornar el Producto con el codigo dado, o None si no existe dicho producto.
		for prenda in self.prendas:
			if codigo == prenda.codigo:
				return prenda
		return None

		
	def modificarUnProducto(self, codigo, producto):
		#Busca el Producto con el codigo dado y modifica el Producto
		
		prenda = self.buscarPorCodigo(codigo)
		
		if prenda:
			prenda.producto = producto
			self.repo.update(prenda)
			return True
		
		return False

	def modificarUnTalle(self, codigo, talle):
		#Busca el Producto con el codigo dado y modifica el Talle
		
		prenda = self.buscarPorCodigo(codigo)
		
		if prenda:
			prenda.talle = talle
			self.repo.update(prenda)
			return True
		
		return False
	
	def modificarUnPrecio(self, codigo, precio):
		#Busca el Producto con el codigo dado dado y modifica el precio
		prenda = self.buscarPorCodigo(codigo)
		
		if prenda:
			prenda.precio = precio
			self.repo.update(prenda)
			return True 
			
		
		return False

	def buscar(self, filtro):
		
		prendas = Ropa.coincide(self, filtro)
		return prendas
	
	def buscarTalle(self, filtro):
		
		prendas = []
		for prenda in self.prendas:
			if filtro in prenda.talle:
				prendas.append(prenda)
		return prendas
	
	def buscarProducto(self, filtro):
		
		prendas = []
		for prenda in self.prendas:
			if filtro in prenda.producto:
				prendas.append(prenda)
		return prendas
		

	def borrarUnProducto(self, codigo):
		prenda = self.buscarPorCodigo(codigo)
		if prenda:
			self.repo.delete(prenda)
			self.prendas.remove(prenda)
			print("El Producto fue eliminado correctamente")
			return True
		else:
			print("No se encontro el Producto buscado")
			return False
			
	
		
	