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
        self.setFixedSize(1000, 700)
                
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
                if os.path.exists(self.dir_imagenes+"/../configuracion_cargada.txt"):
                    gl = "Leer"
                    self.guardarconfig(gl)
                self.ImportarImagenes.setEnabled(True)
                self.stackedWidget.setCurrentWidget(self.pgn_imagenes)
                self.importadas()
                self.leerdirectorio()
                self.leerresultados()
                if self.leer_resultados != []:
                    self.bloqueointerfaz(ir_resultados="On")
                else:
                    self.bloqueointerfaz(ir_resultados="Off")
                self.BarraEstado.showMessage("Proyecto '%s' abierto correctamente." %abrir_directorio, 2000)
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
        dir_cnd_geometricas = dir_salida+"coincidencias/coincidencias_geometricas"
        dir_pistas = dir_salida+"coincidencias/pistas"

        if not os.path.exists(dir_coincidencias):
            os.mkdir(dir_coincidencias)

        if not os.path.exists(dir_reconstruccion):
            os.mkdir(dir_reconstruccion)
        
        if not os.path.exists(dir_cnd_geometricas):
            os.mkdir(dir_cnd_geometricas)

        if not os.path.exists(dir_pistas):
            os.mkdir(dir_pistas)
        
        self.bloqueointerfaz(senal="Off", crear="Off")
        avance = 1
        etapas = 10
        self.progressBar.setTextVisible(True)
        self.progressBar.setMaximum(11)
        self.progressBar.setValue(avance)
        self.progressBar.setFormat("Trabajando...  %v/%m")
        for e in range(etapas):
            self.progressBar.setValue(run(self.dir_entrada, dir_coincidencias, self.par_sensor, dir_reconstruccion, self.sel1md, self.sel1ca, self.sel2mg, self.sel2mc, self.reldist, self.sel3rf, self.sel3mt, self.sel3mr, avance, dir_cnd_geometricas, dir_pistas, self.imagenparA, self.imagenparB))
            avance += 1
        self.leerresultados()
        self.stackedtrabajo.setCurrentWidget(self.pgn_resultados)
        self.bloqueointerfaz(senal="On", ir_resultados="On", crear="On")   
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
        if archivo[0]:
            for a in archivo[0]:
                shutil.copy2(a, self.dir_imagenes)
            self.leerdirectorio()
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
            self.bloqueointerfaz(crear="On")
            self.imagenparA = self.leer_imagenes[1]
            self.imagenparB = self.leer_imagenes[12]
        else:
            self.listaimg.addItem("Aún no hay imagenes importadas!")
            self.visualimg.setPixmap(QPixmap("media/2130.png").scaledToWidth(440))
            self.bloqueointerfaz(crear="Off")
    
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
    def bloqueointerfaz(self, **kwords):
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
        
        gl = "Guardar"
        self.guardarconfig(gl)
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
        self.cargaropciones()
        self.par_sensor = database_sensor()
        self.leer_resultados = []
        self.ir_resultados.setEnabled(False)
        self.bloqueointerfaz(ir_resultados="Off", crear="Off")

    # ===== ARCHIVO DE CONFIGURACION =====
    # Guarda la configuracion elegida una para la reconstruccion cuando se oprime le boton de cargar, creando un archivo en el directorio de trabajo. 
    # Asimismo permite leer este archivo una vez se abra cada proyecto, con el fin de registar las ultimas opciones elegidas. 
    def guardarconfig(self, gl):
        if gl == "Guardar":
            crear_archivo = open(self.dir_imagenes+"/../configuracion_cargada.txt", "w")
            crear_archivo.writelines([self.sel1md+'\n', self.sel1ca+'\n', self.sel2mg+'\n', self.sel2mc+'\n', self.reldist+'\n', self.sel3rf+'\n', self.sel3mt+'\n', self.sel3mr])
            crear_archivo.close()
            del(crear_archivo)
        else:
            leer_archivo = open(self.dir_imagenes+"/../configuracion_cargada.txt", "r")
            parametros = leer_archivo.readlines()
            leer_archivo.close()
            del(leer_archivo)
            self.sel1md = ''.join(x for x in parametros[0] if x not in "\n")
            self.sel1ca = ''.join(x for x in parametros[1] if x not in "\n")
            self.sel2mg = ''.join(x for x in parametros[2] if x not in "\n")
            self.sel2mc = ''.join(x for x in parametros[3] if x not in "\n")
            self.reldist = ''.join(x for x in parametros[4] if x not in "\n")
            self.sel3rf = ''.join(x for x in parametros[5] if x not in "\n")
            self.sel3mt = ''.join(x for x in parametros[6] if x not in "\n")
            self.sel3mr = parametros[7]
            self.cargaropciones()

    # ===== CARGAR ARCHIVO DE CONFIGURACION =====
    # Cambia la seleccion de cada checkbutton despues de que se ha leido el archivo de configuracion del directorio de trabajo.
    def cargaropciones(self):

        # ===== PARAMETROS DE CARACTERISTICAS =====

        # METODO DESCRIPTOR
        if self.sel1md == "SIFT":
            self.sel1mda.setChecked(True)
        elif self.sel1md == "AKAZE_FLOAT":
            self.sel1mdb.setChecked(True)
        elif self.sel1md == "AKAZE_MLDB":
            self.sel1mdc.setChecked(True)

        # DEFINICION
        if self.sel1ca == "NORMAL":
            self.sel1caa.setChecked(True)
        elif self.sel1ca == "HIGH":
            self.sel1cab.setChecked(True)
        elif self.sel1ca == "ULTRA":
            self.sel1cac.setChecked(True)

        # ===== PARAMETROS DE CORRESPONDENCIA =====

        # MODELO GEOMETRICO
        if self.sel2mg == "f":
            self.sel2mga.setChecked(True)
        elif self.sel2mg == "e":
            self.sel2mgb.setChecked(True)
        elif self.sel2mg == "h":
            self.sel2mgc.setChecked(True)
        elif self.sel2mg == "a":
            self.sel2mgd.setChecked(True)
        elif self.sel2mg == "o":
            self.sel2mge.setChecked(True)
        elif self.sel2mg == "u":
            self.sel2mgf.setChecked(True)
        
        # MODELO DE COINCIDENCIA
        if self.sel2mc == "AUTO":
            self.sel2mca.setChecked(True)
        elif self.sel2mc == "BRUTEFORCEL2":
            self.sel2mcb.setChecked(True)
        elif self.sel2mc == "ANNL2":
            self.sel2mcc.setChecked(True)
        elif self.sel2mc == "CASCADEHASHINGL2":
            self.sel2mcd.setChecked(True)
        elif self.sel2mc == "FASTCASCADEHASHINGL2":
            self.sel2mce.setChecked(True)
        elif self.sel2mc == "BRUTEFORCEHAMMING":
            self.sel2mcf.setChecked(True)
        
        # RELACION DE DISTANCIA
        self.numrel.setProperty("value", self.reldist)

        # ===== PARAMETROS DE SFM INCREMENTAL =====

        # REFINAMIENTOS DE INTRINSECOS
        if self.sel3rf == "ADJUST_ALL":
            self.sel3rfa.setChecked(True)
        elif self.sel3rf == "NONE":
            self.sel3rfb.setChecked(True)
        elif self.sel3rf == "ADJUST_FOCAL_LENGTH":
            self.sel3rfc.setChecked(True)
        elif self.sel3rf == "ADJUST_PRINCIPAL_POINT":
            self.sel3rfd.setChecked(True)
        elif self.sel3rf == "ADJUST_DISTORTION":
            self.sel3rfe.setChecked(True)
        
        # METODO DE TRIANGULACION
        if self.sel3mt == "0":
            self.sel3mta.setChecked(True)
        elif self.sel3mt == "1":
            self.sel3mtb.setChecked(True)
        elif self.sel3mt == "2":
            self.sel3mtc.setChecked(True)
        elif self.sel3mt == "3":
            self.sel3mtd.setChecked(True)
        
        # METODO DE RECESION
        if self.sel3mr == "0":
            self.sel3mra.setChecked(True)
        elif self.sel3mr == "1":
            self.sel3mrb.setChecked(True)
        elif self.sel3mr == "2":
            self.sel3mrc.setChecked(True)
        elif self.sel3mr == "3":
            self.sel3mrd.setChecked(True)
        elif self.sel3mr == "4":
            self.sel3mre.setChecked(True)

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
        
# ============================== BUCLE DE TRABAJO ==============================
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windows = MainWindows()
    windows.show()
    app.exec_()