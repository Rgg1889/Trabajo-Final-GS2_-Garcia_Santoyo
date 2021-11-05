from repositorio import Repositorio
from ropa import Ropa
from calzado import Calzado

class RepositorioProductos(Repositorio):
	#Metodos para CRUD en la BDD.

	def get_one(self, codigo):
		'''Recibe un codigo de prenda (número entero). Retorna un objeto Ropa. Si no
		lo encuentra, retorna None.'''
		consulta = "SELECT codigo, talle, precio FROM prendas WHERE codigo = ?"
		result = self.cursor.execute(consulta, [codigo]).fetchone()

		if result == None:
			return None
		else:
			return Ropa(result[1], result[2], result[0])

	def get_all(self):
		'''Retorna todas los prendas que haya almacenadas en el BD'''
		consulta = "SELECT codigo, talle, precio, producto, tipo FROM prendas"
		result = self.cursor.execute(consulta).fetchall()

		listaDeProductos = []

		for unResultado in result:
			
			if unResultado[4] is not None:
				listaDeProductos.append(
				Calzado(unResultado[1], unResultado[2], unResultado[0], unResultado[3], unResultado[4])
				)
			else:
				listaDeProductos.append(
					Ropa(unResultado[1], unResultado[2], unResultado[0], unResultado[3])
					)
		return listaDeProductos

	def store(self, prenda):
		'''Recibe un objeto prenda y lo almacena en el Base de Datos
		En caso de éxito, retorna el codigo de el prenda, número generado por el base
		de datos. En caso de fracaso, retorna 0 (cero).'''
		if hasattr(prenda, "tipo"):
			try:
				query = "INSERT INTO prendas (codigo, talle, precio, producto, tipo) VALUES (?, ?, ?, ?, ?)"
				result = self.cursor.execute(query, [prenda.codigo, prenda.talle, prenda.precio, prenda.producto, prenda.tipo])
			

				self.bd.commit()
				return prenda.codigo
			except:
				self.bd.rollback()
				
				return 0
		else:
			try:
				query = "INSERT INTO prendas (codigo, talle, precio, producto) VALUES (?, ?, ?, ?)"
				result = self.cursor.execute(query, [prenda.codigo, prenda.talle, prenda.precio, prenda.producto])
			

				self.bd.commit()
				return prenda.codigo
			except:
				self.bd.rollback()
				return 0
		
	def delete(self, prenda):
		'''Recibe un objeto Ropa y lo elimina de el Base de Datos.
		Retorna True si tuvo éxito, False de lo contrario.'''
		try:
			query = "DELETE FROM prendas WHERE codigo = ?"
			self.cursor.execute(query, [prenda.codigo])
			c = self.cursor.rowcount
			if c == 0:
				self.bd.rollback()
				return False
			else:
				self.bd.commit()
				return True
		except:
			self.bd.rollback()
			return False

	def update(self, prenda):
		'''Recibe un objeto prenda y actualiza sus datos en el base de datos
		(no se puede actualizar el codigo de el prenda, pero sí el resto de sus
		datos). Retorna True si tuvo éxito, False de lo contrario.'''

		# Aca diferencio si tiene el atributo TIPO, xq son dos querys distintas
		if hasattr(prenda, "tipo"):
			try:
				query = "UPDATE prendas SET talle = ?, precio = ?, producto = ?, tipo = ? WHERE codigo = ?"
				result = self.cursor.execute(query, [prenda.talle, prenda.precio, prenda.producto, prenda.tipo, prenda.codigo])
				if result.rowcount == 0:
					self.bd.rollback()
					return False
				else:
					self.bd.commit()
					return True
			except:
				self.bd.rollback()
				return False
		else:
			try:
				query = "UPDATE prendas SET talle = ?, precio = ?, producto = ? WHERE codigo = ?"
				result = self.cursor.execute(query, [prenda.talle, prenda.precio, prenda.producto, prenda.codigo])
				if result.rowcount == 0:
					self.bd.rollback()
					return False
				else:
					self.bd.commit()
					return True
			except:
				self.bd.rollback()
				return False
