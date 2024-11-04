class Video:
    def __init__(self,nombre,ruta,tamaño):
        self.nombre = nombre
        self.ruta = ruta
        self.tamaño = tamaño
    def __str__(self):
        return f"""
        *** Datos del video ***
            Video: {self.nombre}
            Ruta: {self.ruta}
            Tamaño: {self.tamaño} MB
                """    