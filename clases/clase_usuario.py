from validaciones import validar_usuario_id,validar_nombre_usuario

class Usuario:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
    def __str__(self):
        return f"id: {self.id} -- Nombre: {self.nombre}"
    def actualizarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre
        print(f"Se actualizo correctamente el nombre, ahora es {self.nombre}")
    def mostrarID(self):
        return self.id
    def mostrarNombre(self):
        return self.nombre


def capturarId():
    while True:
        usuarioId = input("Ingrese su ID: ")
        if validar_usuario_id(usuarioId) == True:
            break
    return usuarioId

def capturarNombre():
    while True:
        usuarioNombre = input("Ingrese su nombre: ")
        if validar_nombre_usuario(usuarioNombre) == True:
            break
    return usuarioNombre