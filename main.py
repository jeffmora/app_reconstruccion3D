# Creado por Jefferson Mora Meza. May-2021

# Este script permite lanzar la aplicacion y mantenerla activa, mientras ejecutamos cada 
# una de las funciones de nuestra aplicacion. Es importante que desde este script se
# configure el comportamiento de nuestra apliacion y solo dejemos el script "app.py" para
# el diseño de la misma. Asi no mezclaremos funcionalidad con diseño.


# Importarmos todas las clases y metodos del la interfaz "app.py".
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from app import *
from crear import *
from PyQt5.QtWidgets import QFileDialog, QListWidget

# Importamos librerias propias del sistema para trabajar.
import os
from os.path import expanduser
import shutil

# Esta es la clase que crea la ventana de trabajo, tomando las carecteriticas de diseño y enlazando las
# funciones de los botones de "app.py". 

class MainWindows(QtWidgets.QMainWindow, Ui_Aplicacion):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # ============================== PARAMETROS INICIALES ============================== 
        self.stackedWidget.setCurrentWidget(self.pgn_inicio)
        self.BarraEstado.showMessage("Listo")
        self.dir_imagenes = ""

        # ============================== RELACION BOTON-FUNCION ==============================
        # Relacionamos cada una de las señales que se emiten por la pulsacion de cada boton con una funcion
        # especifica que se debe llevar a cabo.

        self.NuevoProyecto.triggered.connect(self.nuevoproyecto)
        self.AbrirProyecto.triggered.connect(self.abrirproyecto)
        self.Salir.triggered.connect(self.salirapp)
        self.ImportarImagenes.triggered.connect(self.importarimagenes)
        self.Crear3d.clicked.connect(self.crearmodelo)
        self.listaimg.itemClicked.connect(self.mostrarimagen)
        self.agregar.clicked.connect(self.importarimagenes)
        self.eliminar.clicked.connect(self.eliminarimagen)

    # ============================== FUNCIONES ==============================
    
    # ===== NUEVO PROYECTO =====
    # Permite la creacion del directorio sobre el cual vamos a trabajar, asimismo se encarga de validar que exista
    # el directorio de trabajo para habilitar la opcion de importar imagenes.
    def nuevoproyecto(self):
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
                self.leerdirectorio()
        else:
            self.BarraEstado.showMessage("No se creo el proyecto!")

    # ===== ABRIR PROYECTO =====
    # Permite la apertura de un directorio previamente creado, sobre el cual vamos a trabajar, asimismo se encarga
    # de validar que exista el directorio de trabajo para habilitar la opcion de importar imagenes.     
    def abrirproyecto(self):
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
                self.leerdirectorio()
                if self.leer_imagenes != []:
                    self.habilitarcrear3d()
            else:
                self.BarraEstado.showMessage("El proyecto que intenta abrir no se ha creado, intente con 'Nuevo proyecto'.", 2000)
        else:
            self.BarraEstado.showMessage("No ha seleccionado ningún proyecto!")    

    # ===== SALIR DE LA APLICACION =====
    def salirapp(self):
        self.close()

    # ===== CREAR MODELO 3D =====
    # Este metodo es el encargado de procesar cada imagen y generar el modelo 3D de la reconstrucción final.
    # Para esto se utiliza el script "crear.py" encargado de ejecutar cada una de la funciones de las librerias.
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
    
    # ===== IMPORTAR IMAGENES =====
    # Permite al usuario importar cada una de las imagenes a procesar al directorio de trabajo creado o abierto
    # anteriormente.
    def importarimagenes(self):
        self.listaimg.clear()
        self.leer_imagenes = []
        archivo = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Importar archivo',
            directory = expanduser("~"),
            filter = "Imagenes (*.jpg *.jpeg)"
        )
        if archivo:
            for a in archivo[0]:
                shutil.copy2(a, self.dir_imagenes)
            self.leerdirectorio()
            self.habilitarcrear3d()
            self.BarraEstado.showMessage("Imagenes importadas correctamente")
        else:
            self.BarraEstado.showMessage("Seleccione las imagenes para continuar")

    # ===== LEER DIRECTORIO =====
    # Permite eliminar imagenes del directorio de trabajo.
    def eliminarimagen(self):
        if self.selimagen:
            os.remove(str(self.selimagen))
            self.selimagen = []
            self.leerdirectorio()

    # ===== LEER DIRECTORIO =====
    # Comprobara la existencia de las imagenes en el directorio de trabajo y se presentaran en pantalla según su
    # disponibilidad.
    def leerdirectorio(self):
        self.listaimg.clear()
        self.leer_imagenes = sorted(os.listdir(self.dir_imagenes))
        if self.leer_imagenes:
            self.listaimg.addItems(self.leer_imagenes)
            self.visualimg.setPixmap(QPixmap(self.dir_imagenes+"/"+str(self.leer_imagenes[0])).scaledToWidth(400))
        else:
            self.listaimg.addItem("Aún no hay imagenes importadas!")
            self.visualimg.setPixmap(QPixmap("media/2130.png").scaledToWidth(400))
    
    # ===== MOSTRAR IMAGEN =====
    # Como su nombre lo indica, permite visualizar escaladamente cada una de las imagenes que han sido importadas. El
    # usuario debera clickear sobre algun elemento de la lista para ver la imagen.
    def mostrarimagen(self):
        self.selimagen = self.dir_imagenes+"/"+self.listaimg.currentItem().text()
        self.visualimg.setPixmap(QPixmap(self.selimagen).scaledToWidth(400))

    # ===== HABILITAR CREAR 3D =====
    # Este metodo habilita el boton "crear modelo 3D" una vez se ha configurado el proyecto.  
    def habilitarcrear3d(self):
        self.Crear3d.setEnabled(True)
        self.Crear3d.setStyleSheet("border-radius: 0px;\n"
        "background-color: rgb(46, 52, 54);\n"
        "color: rgb(255, 255, 255);\n"
        "")
   

# Bucle de trabajo.
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()