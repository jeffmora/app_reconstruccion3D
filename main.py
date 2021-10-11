# Este script permite lanzar la aplicación y mantenerla activa, mientras ejecutamos cada 
# una de las funciones de nuestra aplicación. Es importante que desde este script se
# configure el comportamiento de nuestra apliación y solo dejemos el script "app.py" para
# el diseño de la misma. Asi no mezclaremos funcionalidad con diseño.


# Importarmos todas las clases y métodos del la interfaz "app.py".
from app import *
from crear import *
from PyQt5.QtWidgets import QFileDialog

# Importamos librerias propias del sistama para trabajar.
import os
from os.path import expanduser
import shutil

class MainWindows(QtWidgets.QMainWindow, Ui_Aplicacion):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # Inicializamos la varible del directorio de imagnes vacío.
        self.dir_imagenes = ""

        # Cargamos la vista inicial de la aplicación.
        self.stackedWidget.setCurrentWidget(self.pgn_inicio)
        
        # Mostramos un mensaje de aplicación cargada.
        self.BarraEstado.showMessage("Listo")

        # Construimos las señales de activación de la barra de menú.
        self.NuevoProyecto.triggered.connect(self.nuevoproyecto)
        self.AbrirProyecto.triggered.connect(self.abrirproyecto)
        self.Salir.triggered.connect(self.salirapp)
        self.ImportarImagenes.triggered.connect(self.importarimagenes)
        self.Crear3d.clicked.connect(self.crearmodelo)

    def nuevoproyecto(self):
        '''Este metodo permite la creacion del directorio sobre el cual vamos a trabajar,
        asimismo se encarga de validar que exista el directorio de trabajo para habilitar
        la opcion de importar imagenes.'''
        crear_directorio = QFileDialog.getExistingDirectory(
            parent = self,
            caption = 'Crear directorio de trabajo',
            directory = expanduser("~")
        )

        if len(crear_directorio) != 0:
            directorio = "imagenes"
            self.dir_imagenes = os.path.join(crear_directorio, directorio)
            if os.path.exists(self.dir_imagenes) == True:
                self.BarraEstado.showMessage("El directorio '%s' ya existe, intente con 'Abrir proyecto'." %crear_directorio, 2000)
            else:
                os.mkdir(self.dir_imagenes)
                self.stackedWidget.setCurrentWidget(self.pgn_imagenes)
                self.BarraEstado.showMessage("Proyecto creado en '%s'." %crear_directorio, 2000)
                self.ImportarImagenes.setEnabled(True)
        else:
            self.BarraEstado.showMessage("No se creo el proyecto!")
        
    def abrirproyecto(self):
        '''Este metodo permite la apertura de un directorio previamente creado, sobre el cual vamos a trabajar,
        asimismo se encarga de validar que exista el directorio de trabajo para habilitar
        la opcion de importar imagenes.'''
        abrir_directorio = QFileDialog.getExistingDirectory(
            parent = self,
            caption = 'Abrir directorio de trabajo',
            directory = expanduser("~")
        )
        
        if len(abrir_directorio) != 0:
            directorio = "imagenes"
            self.dir_imagenes = os.path.join(abrir_directorio, directorio)
            if os.path.exists(self.dir_imagenes) == True:
                self.BarraEstado.showMessage("Proyecto '%s' abierto correctamente." %abrir_directorio, 2000)
                self.stackedWidget.setCurrentWidget(self.pgn_imagenes)
                self.ImportarImagenes.setEnabled(True)
            else:
                self.BarraEstado.showMessage("El proyecto que intenta abrir no se ha creado, intente con 'Nuevo proyecto'.", 2000)
        else:
            self.BarraEstado.showMessage("No ha seleccionado ningún proyecto!")    

    def salirapp(self):
        self.close()

    def crearmodelo(self):
        dir_entrada = self.dir_imagenes
        dir_salida = self.dir_imagenes+"/../"
        dir_coincidencias = dir_salida+"coincidencias"
        dir_reconstruccion = dir_salida+"reconstruccion"
        par_sensor = "/home/jefferson/Escritorio/tesis/openMVG/src/openMVG/exif/sensor_width_database/sensor_width_camera_database.txt"

        if not os.path.exists(dir_coincidencias):
            os.mkdir(dir_coincidencias)

        if not os.path.exists(dir_reconstruccion):
            os.mkdir(dir_reconstruccion)
        
        #run(dir_entrada, dir_coincidencias, par_sensor, dir_reconstruccion)
        print(dir_entrada)
        print(dir_salida)
        print(dir_coincidencias)
        print(dir_reconstruccion)
    
    def importarimagenes(self):
        '''Este metodo permite la importar cada una de las imagenes con las que vamos a trabajar,
        al directorio de trabajo/imagenes creado anteriormente.'''
        archivo = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Importar archivo',
            directory = expanduser("~"),
            filter = "Imagenes (*.jpg *.jpeg)"
        )

        if len(archivo) != 0:
            for a in archivo[0]:
                shutil.copy2(a, self.dir_imagenes)
            
            self.BarraEstado.showMessage("Imagenes importadas correctamente")
        else:
            self.BarraEstado.showMessage("Seleccione las imagenes para continuar")      
   

# Bucle de trabajo.
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()