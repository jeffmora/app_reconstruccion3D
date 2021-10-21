#!/venv/bin/ python

"""
Creado Octubre 19 de 2021
Autor: Jefferson Mora M.
"""

# Este script permite lanzar la aplicacion y mantenerla activa, mientras ejecutamos cada una de las funciones de 
# nuestra aplicacion. Es importante que desde este script se configure el comportamiento de nuestra aplicacion y 
# solo dejemos el script "app.py" para el diseño de la misma. Asi no mezclaremos funcionalidad con diseño.

# app.py = Script de diseño de la aplicacion.
# crear.py = Script que llama las dependencias segun las necesite para el proceso de reconstrucción.

# ==================================== IMPORTAR LIBRERIAS ====================================
# Se importan todas las clases/metodos de la interfaz "app.py" y el metodo de las dependencias "crear.py". Asimismo
# las librerias para interacturar con el sistema.
from PyQt5.QtGui import QPixmap
from app import *
from crear import *
from PyQt5.QtWidgets import QFileDialog
import os
from os.path import expanduser
import shutil
import subprocess

# =================================== CLASE PRINCIPAL =================================== 
# Esta es la clase que crea la ventana de trabajo, tomando las carecteriticas de diseño y enlazando las
# funciones de los botones de "app.py".
class MainWindows(QtWidgets.QMainWindow, Ui_Aplicacion):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
                
        # ============================== PARAMETROS INICIALES ============================== 
        self.stackedWidget.setCurrentWidget(self.pgn_inicio)
        self.configdefecto()
        self.BarraEstado.showMessage("Listo")

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
        self.Cargar.clicked.connect(self.cargarconfig)
        self.ir_resultados.clicked.connect(self.resultados)
        self.ir_importadas.clicked.connect(self.importadas)
        self.Visualizar.clicked.connect(self.visualizar)

    # ============================== FUNCIONES ==============================
    
    # ===== NUEVO PROYECTO =====
    # Crea un directorio de trabajo de acuerdo al nombre que el usuario decida. Asimismo se encarga de validar que exista
    # el directorio de trabajo para habilitar la opcion de importar imagenes.
    def nuevoproyecto(self):
        crear_directorio = QFileDialog.getExistingDirectory(
            parent = self,
            caption = 'Crear directorio de trabajo',
            directory = expanduser("~")
        )
        if len(crear_directorio) != 0:
            self.configdefecto()
            directorio = "imagenes"
            self.dir_imagenes = os.path.join(crear_directorio, directorio)
            if os.path.exists(self.dir_imagenes) == True:
                self.BarraEstado.showMessage("El directorio '%s' ya existe, intente con 'Abrir proyecto'." %crear_directorio, 2000)
            else:
                os.mkdir(self.dir_imagenes)
                self.stackedWidget.setCurrentWidget(self.pgn_imagenes)
                self.importadas()
                self.BarraEstado.showMessage("Proyecto creado en '%s'." %crear_directorio, 2000)
                self.ImportarImagenes.setEnabled(True)
                self.leerdirectorio()
        else:
            self.BarraEstado.showMessage("No se creo el proyecto!")

    # ===== ABRIR PROYECTO =====
    # Abre un directorio previamente creado. Asimismo se encarga de validar que exista el directorio de trabajo para habilitar
    # la opcion de importar imagenes, de haber hay imagenes y/o resultados los muestra al usuario.     
    def abrirproyecto(self):
        abrir_directorio = QFileDialog.getExistingDirectory(
            parent = self,
            caption = 'Abrir directorio de trabajo',
            directory = expanduser("~")
        )
        if len(abrir_directorio) != 0:
            self.configdefecto()
            directorio = "imagenes"
            self.dir_imagenes = os.path.join(abrir_directorio, directorio)
            if os.path.exists(self.dir_imagenes) == True:
                self.BarraEstado.showMessage("Proyecto '%s' abierto correctamente." %abrir_directorio, 2000)
                self.stackedWidget.setCurrentWidget(self.pgn_imagenes)
                self.importadas()
                self.ImportarImagenes.setEnabled(True)
                self.leerdirectorio()
                if self.leer_imagenes != []:
                    self.bloqueoinferfaz(crear="On")
                    self.leerresultados()
                    if self.leer_resultados != []:
                        self.bloqueoinferfaz(ir_resultados="On")
                    else:
                        self.bloqueoinferfaz(ir_resultados="Off")
            else:
                self.BarraEstado.showMessage("El proyecto que intenta abrir no se ha creado, intente con 'Nuevo proyecto'.", 2000)
        else:
            self.BarraEstado.showMessage("No ha seleccionado ningún proyecto!")    

    # ===== SALIR DE LA APLICACION =====
    def salirapp(self):
        self.close()

    # ===== CREAR MODELO 3D =====
    # Ejecuta el procesamiento de cada imagen y llama las dependencias para generar el modelo 3D de la reconstrucción final.
    # Para esto se utiliza el script "crear.py" encargado de ejecutar cada una de la funciones de las librerias.
    def crearmodelo(self):
        self.dir_entrada = self.dir_imagenes
        dir_salida = self.dir_imagenes+"/../"
        dir_coincidencias = dir_salida+"coincidencias"
        dir_reconstruccion = dir_salida+"reconstruccion"

        if not os.path.exists(dir_coincidencias):
            os.mkdir(dir_coincidencias)

        if not os.path.exists(dir_reconstruccion):
            os.mkdir(dir_reconstruccion)
        
        self.bloqueoinferfaz(senal="Off", crear="Off")
        avance = 1
        etapas = 10
        self.progressBar.setTextVisible(True)
        self.progressBar.setMaximum(11)
        self.progressBar.setValue(avance)
        self.progressBar.setFormat("Trabajando...  %v/%m")
        for e in range(etapas):
            self.progressBar.setValue(run(self.dir_entrada, dir_coincidencias, self.par_sensor, dir_reconstruccion, self.sel1md, self.sel1ca, self.sel2mg,
                self.sel2mc, self.reldist, self.sel3rf, self.sel3mt, self.sel3mr, avance))
            avance += 1
        self.leerresultados()
        self.stackedtrabajo.setCurrentWidget(self.pgn_resultados)
        self.bloqueoinferfaz(senal="On", ir_resultados="On", crear="On")
        self.progressBar.setFormat("Finalizado")
    
    # ===== IMPORTAR IMAGENES =====
    # Importa cada una de las imagenes a procesar al directorio de trabajo creado o abierto anteriormente.
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
            self.bloqueoinferfaz(crear="On")
            self.BarraEstado.showMessage("Imagenes importadas correctamente")
        else:
            self.BarraEstado.showMessage("Seleccione las imagenes para continuar")

    # ===== ELIMINAR IMAGEN =====
    # Elimina la imagen seleccionada del directorio de trabajo.
    def eliminarimagen(self):
        try:    
            if self.selimagen:
                os.remove(str(self.selimagen))
                self.selimagen = []
                self.leerdirectorio()
        except AttributeError:
            self.BarraEstado.showMessage("No hay elementos selecionados o la carpeta esta vacía.")
        except FileNotFoundError:
            self.BarraEstado.showMessage("El archivo no existe.")

    # ===== LEER DIRECTORIO =====
    # Comprueba la existencia de las imagenes en el directorio de trabajo y se presentaran en pantalla según su
    # disponibilidad.
    def leerdirectorio(self):
        tituloproyecto = self.dir_imagenes.split('/')
        self.setWindowTitle("%s - Reconstruccion 3D" %tituloproyecto[len(tituloproyecto)-2])
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.listaimg.clear()
        self.leer_imagenes = sorted(os.listdir(self.dir_imagenes))
        if self.leer_imagenes:
            self.listaimg.addItems(self.leer_imagenes)
            self.visualimg.setPixmap(QPixmap(self.dir_imagenes+"/"+str(self.leer_imagenes[0])).scaledToWidth(440))
        else:
            self.listaimg.addItem("Aún no hay imagenes importadas!")
            self.visualimg.setPixmap(QPixmap("media/2130.png").scaledToWidth(440))
    
    # ===== MOSTRAR IMAGEN =====
    # Busca y muestra la imagen seleccionada de la lista desplegada al usuario, su presentación se reescala a 440px de ancho. El
    # usuario debera clickear sobre algun elemento de la lista para ver la imagen.
    def mostrarimagen(self):
        if self.listaimg.currentItem().text() == "Aún no hay imagenes importadas!":
            self.visualimg.setPixmap(QPixmap("media/2130.png").scaledToWidth(440))
        else:
            self.selimagen = self.dir_imagenes+"/"+self.listaimg.currentItem().text()
            self.visualimg.setPixmap(QPixmap(self.selimagen).scaledToWidth(440))

    # ===== BLOQUEO DE INTERFAZ =====
    # Habilita y deshabilita cada uno de los botones de la ventana y menu de trabajo dependiendo de ciertas condiciones.   
    def bloqueoinferfaz(self, **kwords):
        for k in kwords:
            if k == "ir_resultados":
                if kwords[k] == "On":
                    self.ir_resultados.setEnabled(True)
                    self.ir_resultados.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                elif kwords[k] == "Off":
                    self.ir_resultados.setEnabled(False)
                    self.ir_resultados.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
            elif k == "senal":
                if kwords[k] == "Off":
                    self.NuevoProyecto.setEnabled(False)
                    self.AbrirProyecto.setEnabled(False)
                    self.ImportarImagenes.setEnabled(False)
                    self.Salir.setEnabled(False)
                    self.Cargar.setEnabled(False)
                    self.Cargar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.agregar.setEnabled(False)
                    self.agregar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.eliminar.setEnabled(False)
                    self.eliminar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.ir_resultados.setEnabled(False)
                    self.ir_resultados.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                elif kwords[k] == "On":
                    self.NuevoProyecto.setEnabled(True)
                    self.AbrirProyecto.setEnabled(True)
                    self.ImportarImagenes.setEnabled(True)
                    self.Salir.setEnabled(True)
                    self.Cargar.setEnabled(True)
                    self.Cargar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.agregar.setEnabled(True)
                    self.agregar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.eliminar.setEnabled(True)
                    self.eliminar.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                    self.ir_resultados.setEnabled(True)
                    self.ir_resultados.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
            elif k == "crear":
                if kwords[k] == "On":
                    self.Crear3d.setEnabled(True)
                    self.Crear3d.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(46, 52, 54);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")
                elif kwords[k] == "Off":
                    self.Crear3d.setEnabled(False)
                    self.Crear3d.setStyleSheet("border-radius: 0px;\n"
                    "background-color: rgb(136, 138, 133);\n"
                    "color: rgb(255, 255, 255);\n"
                    "")

    # ===== CARGAR CONFIGURACION =====
    # Carga todos los paremetros configurados por el usuario. Los parametros por defecto ya se encuentran cargados para ejecutar.
    def cargarconfig(self):
        
        # ===== PARAMETROS DE CARACTERISTICAS =====
        
        # METODO DESCRIPTOR
        if self.sel1mda.isChecked():
            self.sel1md = "SIFT"
        elif self.sel1mdb.isChecked():
            self.sel1md = "AKAZE_FLOAT"
        elif self.sel1mdc.isChecked():
            self.sel1md = "AKAZE_MLDB"
        
        # DEFINICION
        if self.sel1caa.isChecked():
            self.sel1ca = "NORMAL"
        elif self.sel1cab.isChecked():
            self.sel1ca = "HIGH"
        elif self.sel1cac.isChecked():
            self.sel1ca = "ULTRA"
        
        # ===== PARAMETROS DE CORRESPONDENCIA =====

        # MODELO GEOMETRICO
        if self.sel2mga.isChecked():
            self.sel2mg = "f"
        elif self.sel2mgb.isChecked():
            self.sel2mg = "e"
        elif self.sel2mgc.isChecked():
            self.sel2mg = "h"
        elif self.sel2mgd.isChecked():
            self.sel2mg = "a"
        elif self.sel2mge.isChecked():
            self.sel2mg = "o"
        elif self.sel2mgf.isChecked():
            self.sel2mg = "u"

        # MODELO DE COINCIDENCIA
        if self.sel2mca.isChecked():
            self.sel2mc = "AUTO"
        elif self.sel2mcb.isChecked():
            self.sel2mc = "BRUTEFORCEL2"
        elif self.sel2mcc.isChecked():
            self.sel2mc = "ANNL2"
        elif self.sel2mcd.isChecked():
            self.sel2mc = "CASCADEHASHINGL2"
        elif self.sel2mce.isChecked():
            self.sel2mc = "FASTCASCADEHASHINGL2"
        elif self.sel2mcf.isChecked():
            self.sel2mc = "BRUTEFORCEHAMMING"
        
        # RELACION DE DISTANCIA
        self.reldist = str(round(self.numrel.value(), 2))
        
        # ===== PARAMETROS DE SFM INCREMENTAL =====

        # REFINAMIENTOS DE INTRINSECOS
        if self.sel3rfa.isChecked():
            self.sel3rf = "ADJUST_ALL"
        elif self.sel3rfb.isChecked():
            self.sel3rf = "NONE"
        elif self.sel3rfc.isChecked():
            self.sel3rf = "ADJUST_FOCAL_LENGTH"
        elif self.sel3rfd.isChecked():
            self.sel3rf = "ADJUST_PRINCIPAL_POINT"
        elif self.sel3rfe.isChecked():
            self.sel3rf = "ADJUST_DISTORTION"
        
        # METODO DE TRIANGULACION
        if self.sel3mta.isChecked():
            self.sel3mt = "0"
        elif self.sel3mtb.isChecked():
            self.sel3mt = "1"
        elif self.sel3mtc.isChecked():
            self.sel3mt = "2"
        elif self.sel3mtd.isChecked():
            self.sel3mt = "3"
        
        # METODO DE RECESION
        if self.sel3mra.isChecked():
            self.sel3mr = "0"
        elif self.sel3mrb.isChecked():
            self.sel3mr = "1"
        elif self.sel3mrc.isChecked():
            self.sel3mr = "2"
        elif self.sel3mrd.isChecked():
            self.sel3mr = "3"
        elif self.sel3mre.isChecked():
            self.sel3mr = "4"
        self.BarraEstado.showMessage("Configuración cargada correctamente", 2000)

    # ===== CONFIGURACION POR DEFECTO =====
    # Carga la configuracion por defecto para que el usuario no tenga ningun inconveniente al momento de ejecutar la reconstruccion.
    def configdefecto(self):
        self.progressBar.setTextVisible(False)
        self.dir_imagenes = ""
        self.sel1md = "SIFT"
        self.sel1ca = "NORMAL"
        self.sel2mg = "f"
        self.sel2mc = "FASTCASCADEHASHINGL2"
        self.reldist = "0.8"
        self.sel3rf = "ADJUST_ALL"
        self.sel3mt = "3"
        self.sel3mr = "3"
        self.par_sensor = database_sensor()
        self.leer_resultados = []
        self.ir_resultados.setEnabled(False)

    # ===== MOSTRAR RESULTADOS =====
    # Muestra al usuario los archivos resultantes del proceso de reconstruccion. Para su visualizacion se hace uso del softwarea MeshLab. 
    def leerresultados(self):
        self.listares.clear()
        self.dir_reconstruccion2 = os.path.join(self.dir_imagenes,"./../reconstruccion")
        if os.path.exists(self.dir_reconstruccion2):
            self.leer_resultados = sorted([file for file in os.listdir(self.dir_reconstruccion2) if '.ply' in file], reverse=True)
            try:
                self.leer_resultados
                self.listares.addItems(self.leer_resultados)
            except:
                self.listaimg.addItem("Sin reconstrucciones generadas!")

    # ===== VENTANA DE RESULTADOS =====
    def resultados(self):
        self.stackedtrabajo.setCurrentWidget(self.pgn_resultados)

    # ===== VENTANA DE IMAGENES IMPORTADAS =====
    def importadas(self):
        self.stackedtrabajo.setCurrentWidget(self.pgn_importadas)

    # ===== VISUALIZAR ARCHIVOS DE RECOSNTRUCCION =====
    def visualizar(self):
        selresultado = self.dir_reconstruccion2+"/"+self.listares.currentItem().text()
        meshlab(selresultado)
        #pVis = subprocess.Popen(["meshlab", selresultado])
        #pVis.wait()

        
# ============================== BUCLE DE TRABAJO ==============================
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()