class Usuario:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    def __str__(self):
        return f"id: {self.id} -- Nombre: {self.nombre}"
    def actualizarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre
        print(f"Se actualizo correctamente el nombre, ahora es {self.nombre}")
