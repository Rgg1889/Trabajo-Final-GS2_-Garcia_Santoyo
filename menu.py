from bdd import Bdd
import sys
class Menu:

	def __init__(self):
		self.bdd = Bdd()
		self.opciones= {
			"1": self.mostrarProductos,
			"2": self.buscarProductos,
			"3": self.agregarProductos,
			"4": self.updateProductos,
			"5": self.borrarProducto,
			"6": self.InformeProductos,
			"7": self.cerrarPrograma
		}

	def mostrar_menu(self):
#Menú de opciones
		print("""
Menú Cliente:
1) Mostrar todos los Productos.
2) Buscar uno o varios Productos.
3) Agregue un Producto.
4) Modificar un Producto.
5) Borrar un Producto
6) Emitir Informe de Productos.
7) Cerrar Programa
""")

	def ejecutar(self):
		#Muestra el menu y se selecciona una opcion.
		while True:
			self.mostrar_menu()
			opcion = input("Por favor, seleccione una opción: ")
		#Guardamos en el variable opcion el método que corresponde a la opción elegida por el usuario. 
			accion = self.opciones.get(opcion)
			if accion:
				accion()
			else:
				print("{0} Seleccion incorrecta, digite una opcion del 1 al 7".format(opcion))

	def mostrarProductos(self, prendas=None):
		#Si recibe como parámetro un lista de productos, muestra el codigo, talle y precio de esas prendas. Si no recibe el parámetro, muestra id, talle precio de todas los prendas'''
		if prendas is None:
			prendas =  self.bdd.prendas
		for prenda in prendas:
			
			print('Producto: ', prenda.producto)
			print('Codigo del Producto: ', prenda.codigo)
			print('Talle del Producto: ', prenda.talle)
			
			if hasattr(prenda, 'tipo'):
				print('Tipo de Calzado: ', prenda.tipo)
			print('Precio: $', prenda.precio)
			print('-' * 40)
	
	def buscarProductos(self):
    	#Buscar Productos a traves de filtros.
			
		busqueda = int(input("Buscar Producto por:  1)Producto 2)Codigo:  "))
		if busqueda == 1:
			filtro = input("Buscar: ")
			prendas = self.bdd.buscar(filtro)
			if prendas:
				self.mostrarProductos(prendas)
			else:
				print("Ningun articulo coincide con la búsqueda")
		
	#	elif busqueda == 2:
	#		talle = input("Buscar: ")
	#		prendas = self.bdd.buscar(talle)
	#		if prendas:
	#			self.mostrarProductos(prendas)
	#		else:
	#			print("Ningun articulo coincide con la búsqueda")
		
	#	elif busqueda == 3:
	#		precio = input("Buscar: ")
	#		prendas = self.bdd.buscar(precio)
	#		if prendas:
	#			self.mostrarProductos(prendas)
	#		else:
	#			print("Ningun articulo coincide con la búsqueda")
		
		
		elif busqueda == 2:
			while True:
				try:
					
					codigo = int(input("Ingrese Codigo de producto: "))
					break
				except ValueError:
					print("Debes escribir un número.")
			prenda = self.bdd.buscarPorCodigo(codigo)
			if prenda:
				print('Producto: ', prenda.producto)
				print('Codigo del producto: ', prenda.codigo)
				print('Talle del Producto: ', prenda.talle)
				
				if hasattr(prenda, 'tipo'):
					print('Tipo de Calzado: ', prenda.tipo)
				print('Precio del Producto: $', prenda.precio)
			else:
				print("Ninguna articulo coincide con la búsqueda")
		else:
			print("La opción seleccionada es invalida, por favor selecciones 1 o 2")


	def agregarProductos(self):
		#Agrega un nuevo producto 
		while True:
			try:
				codigo = int(input("Ingrese el Codigo del nuevo Producto: "))
				break
			except ValueError:
				print("Solo puede seleccionar un numero. No escribir simbolos o letras.")
		a = self.bdd.buscarPorCodigo(codigo)
		if a == None:
			producto = input("Ingrese el Producto: ")
			while True:
				try:
					precio = float(input("Ingrese el Precio del Producto: $"))

					break
				except ValueError:
					print("Ingrese un importe sin simbolos.")
			b = int(input("Si su producto es un Calzado digite 1, caso contrario digite 2: "))
			if b == 1:
				talle = input("Ingrese el talle: ") 
				tipo = input("Ingrese el tipo de Calzado :")
				prenda = self.bdd.nuevoCalzado(talle, precio, codigo, producto, tipo)
			elif b == 2:
				talle = input("Ingrese el talle: ")
				prenda = self.bdd.nuevoProducto(talle, precio, codigo, producto)
			else:
				print("Solo puede seleccionar un numero. No escribir simbolos o letras.")
		else:
			print("El Codigo seleccionado ya esta asignado a otro producto")
		

	def updateProductos(self):
		#Actualización de Productos
		codigo = int(input("Ingrese el codigo del Producto que desea modificar: "))
		prenda = self.bdd.buscarPorCodigo(codigo)
		if prenda != None:
			c = input("Seleccione la propiedad que desea modificar: 1)Producto, 2)Precio , 3)Talle : ")
			
			if c == "1":
				producto = input("Ingrese el Producto: ")
				self.bdd.modificarUnProducto(codigo, producto)
			elif c == "2":
				while True:
					try:
						precio = float(input("Ingrese el Precio: "))
						self.bdd.modificarUnPrecio(codigo, precio)
						break
					except ValueError:
						print("Escriba un importe sin simbolos.")
			elif c == "3":
				talle = input("Ingrese el Talle: ")
				self.bdd.modificarUnTalle(codigo, talle)
						
			else:
				print("Opción invalida")
		else:
			print("Articulo no encontrado")

	def cerrarPrograma(self):
		#Muestra un mensaje y sale del sistema
		print("Gracias por utilizar el Programa.")
		sys.exit(0)
		
	def borrarProducto(self):
		#Se borra un producto a traves de su codigo
		codigo = int(input("Ingrese el codigo del Producto que desea eliminar: "))
		self.bdd.borrarUnProducto(codigo)
		
	def InformeProductos(self):
		#Emisión de informe.
		prendas =  self.bdd.prendas
		suma = 0
		mayor = None
		menor = None
		mayores = []
		menores = []

		#Determina el mayor precio, el menor precio y la suma de los Productos en la lista'''
		
		for prenda in prendas:
			suma += prenda.precio
			if not mayor:
				mayor = prenda
			if mayor.precio < prenda.precio:
				mayor = prenda
			if not menor:
				menor = prenda
			if menor.precio > prenda.precio :
				menor = prenda
		for prenda in prendas:
			if mayor.precio == prenda.precio:
				mayores.append(prenda)
			if menor.precio == prenda.precio:
				menores.append(prenda)
		
		#Informe
		
		cantidad = len(prendas) 
		sumaprecios = suma
		promedio = suma / cantidad
		
		print("INFORME")
		print("Cantidad Total de Productos : ", cantidad)
		print("El promedio de los precios de los Productos es de: $", promedio)
		print("la sumatoria de precios es de: $", sumaprecios)

		if len(mayores) > 1:
			print("Los Productos con mayor costo son: ")
			for prodMayo in mayores:
				print(prodMayo.producto, "$ ", prodMayo.precio)
		else:
			print("El Producto", mayor.producto, "es el mas caro y su precio es de: $", mayor.precio)

		
		if len(menores) > 1:
			print("Hay", len(menores), "Productos con el menor precio y son:"  )
			for prodMenor in menores:
				print(prodMenor.producto, " con un precio de: ", prodMenor.precio)
		else:
			print("El Producto", menor.producto, "es el mas barato y su precio es de: $", menor.precio)
		

if __name__ == "__main__":
	#Esta parte del código está fuera de el clase Menu.
	Menu().ejecutar()
