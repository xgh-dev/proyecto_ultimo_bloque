from validaciones import validar_tamaño
from clases.clase_video import Video
from clases.clase_usuario import Usuario,capturarId,capturarNombre


datos = []

class Mis_Videos_Online():
    def __init__(self):
        self.iniciarPrograma()
    def iniciarPrograma(self):
        print("Iniciando el programa")
        #crear un bucle que se encargue de inicializar el menu
        while True:
            print("""
            Seleccione una opción para navegar en el menu:
                1) Iniciar sesión
                2) Mostrar registros
                3) Salir
                """)
            accion = int(input("Acción a realizar: "))
            if accion == 1:
                self.acceso()
            elif accion == 2:
                self.mostrarRegistros()
            elif accion == 3:
                break
            else:
                print("Seleccione una opción a realizar")
    def acceso(self):
        usuario_id = capturarId()
        usuario_nombre = capturarNombre()
        
        cantidad_de_videos = 0
        while True:
            cantidad_de_videos = int(input("Ingrese la cantidad de videos a subir (no mayor a 3): "))
            if cantidad_de_videos > 0 and cantidad_de_videos < 4:
                break
            #cantidad_de_videos = int(input("Ingrese la cantidad de videos a subir (no mayor a 3): "))
        #print(f"hola {usuario_nombre}, su id es {usuario_id}, la cantidad de videos que subira es {cantidad_de_videos}")
        while True:
            print(f"hola {usuario_nombre}, su id es {usuario_id}, la cantidad de videos que subira es {cantidad_de_videos}")
            print("""
                La información es correcta: 
                    1) Si
                    2) No
                    """)
            comprobacion = int(input("Indique su opción: "))
            if comprobacion == 1:
                break
            elif comprobacion == 2:
                while True:
                    print("""
                        Indique el dato que quiere cambiar:
                            1) Nombre
                            2) Cantidad de videos
                            3) Salir
                            """)
                    opcion = int(input("Indique la opción a realizar: "))
                    if opcion == 1:
                        usuario_nombre = capturarNombre()
                    elif opcion == 2:
                        while True:
                            cantidad_de_videos = int(input("Ingrese la cantidad de videos a subir (no mayor a 3): "))
                            if cantidad_de_videos > 0 and cantidad_de_videos < 4:
                                break
                    elif opcion == 3:
                        break
        claseUsuario = Usuario(usuario_id,usuario_nombre)
        self.ingresarVideos(claseUsuario,cantidad_de_videos)
            
    def ingresarVideos(self,claseUsuario,cantidad):
        print("Ingrese los videos")
        objeto = {
            "id": claseUsuario.mostrarID(),
            "nombre": claseUsuario.mostrarNombre(),
            "videos": []
        }
        for i in range(cantidad):
            print(f" ------ Datos del video {i+1} ------ ")
            #titulo_del_video = input("Ingresa el titulo del video: ")
            nombre_del_video = input("Ingrese el nombre del video: ")
            ruta_del_video = input("Ingrese la ruta del video: ")
            #tamaño_del_video = input("Ingrese el tamaño del video (no mayor de 3 MB): ")
            while True:
                tamaño_del_video = input("Ingrese el tamaño del video (no mayor de 3 MB): ")
                if validar_tamaño(tamaño_del_video):
                    break
            video = Video(nombre_del_video,ruta_del_video, tamaño_del_video)
            objeto["videos"].append(video)
        datos.append(objeto)
    def mostrarRegistros(self):
        for dato in datos:
            print("-" * 40)
            print(f"ID: {dato['id']}")
            print(f"Nombre: {dato['nombre']}")
            for video in dato['videos']:
                print(video)
            print("-" * 40)
       
    
iniciarProgramacion = Mis_Videos_Online()