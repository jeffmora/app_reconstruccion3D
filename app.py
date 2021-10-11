# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Aplicacion(object):
    def setupUi(self, Aplicacion):
        Aplicacion.setObjectName("Aplicacion")
        Aplicacion.resize(1000, 700)
        Aplicacion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(Aplicacion)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pgn_inicio = QtWidgets.QWidget()
        self.pgn_inicio.setObjectName("pgn_inicio")
        self.logouts = QtWidgets.QLabel(self.pgn_inicio)
        self.logouts.setGeometry(QtCore.QRect(443, 560, 114, 68))
        self.logouts.setStyleSheet("border-image: url(:/logos/media/Logo-UTSrd.png);")
        self.logouts.setText("")
        self.logouts.setAlignment(QtCore.Qt.AlignCenter)
        self.logouts.setObjectName("logouts")
        self.logoapp = QtWidgets.QLabel(self.pgn_inicio)
        self.logoapp.setGeometry(QtCore.QRect(217, 80, 566, 401))
        self.logoapp.setStyleSheet("border-image: url(:/logos/media/ER.png);")
        self.logoapp.setText("")
        self.logoapp.setAlignment(QtCore.Qt.AlignCenter)
        self.logoapp.setObjectName("logoapp")
        self.stackedWidget.addWidget(self.pgn_inicio)
        self.pgn_imagenes = QtWidgets.QWidget()
        self.pgn_imagenes.setObjectName("pgn_imagenes")
        self.Crear3d = QtWidgets.QPushButton(self.pgn_imagenes)
        self.Crear3d.setEnabled(True)
        self.Crear3d.setGeometry(QtCore.QRect(535, 580, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Crear3d.setFont(font)
        self.Crear3d.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Crear3d.setObjectName("Crear3d")
        self.tabConfig = QtWidgets.QTabWidget(self.pgn_imagenes)
        self.tabConfig.setGeometry(QtCore.QRect(1, 1, 260, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabConfig.setFont(font)
        self.tabConfig.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabConfig.setObjectName("tabConfig")
        self.tabCar = QtWidgets.QWidget()
        self.tabCar.setObjectName("tabCar")
        self.infoCar1 = QtWidgets.QLabel(self.tabCar)
        self.infoCar1.setGeometry(QtCore.QRect(5, 0, 220, 80))
        self.infoCar1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCar1.setWordWrap(True)
        self.infoCar1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCar1.setObjectName("infoCar1")
        self.box1md = QtWidgets.QGroupBox(self.tabCar)
        self.box1md.setGeometry(QtCore.QRect(5, 160, 220, 85))
        self.box1md.setObjectName("box1md")
        self.sel1mda = QtWidgets.QRadioButton(self.box1md)
        self.sel1mda.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel1mda.setChecked(True)
        self.sel1mda.setObjectName("sel1mda")
        self.sel1mdb = QtWidgets.QRadioButton(self.box1md)
        self.sel1mdb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel1mdb.setChecked(False)
        self.sel1mdb.setObjectName("sel1mdb")
        self.sel1mdc = QtWidgets.QRadioButton(self.box1md)
        self.sel1mdc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel1mdc.setObjectName("sel1mdc")
        self.box1ca = QtWidgets.QGroupBox(self.tabCar)
        self.box1ca.setGeometry(QtCore.QRect(5, 360, 220, 85))
        self.box1ca.setObjectName("box1ca")
        self.sel1caa = QtWidgets.QRadioButton(self.box1ca)
        self.sel1caa.setGeometry(QtCore.QRect(5, 20, 170, 20))
        self.sel1caa.setChecked(True)
        self.sel1caa.setObjectName("sel1caa")
        self.sel1cab = QtWidgets.QRadioButton(self.box1ca)
        self.sel1cab.setGeometry(QtCore.QRect(5, 40, 170, 20))
        self.sel1cab.setObjectName("sel1cab")
        self.sel1cac = QtWidgets.QRadioButton(self.box1ca)
        self.sel1cac.setGeometry(QtCore.QRect(5, 60, 170, 20))
        self.sel1cac.setObjectName("sel1cac")
        self.infoCar2 = QtWidgets.QLabel(self.tabCar)
        self.infoCar2.setGeometry(QtCore.QRect(5, 90, 220, 65))
        self.infoCar2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCar2.setWordWrap(True)
        self.infoCar2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCar2.setObjectName("infoCar2")
        self.line = QtWidgets.QFrame(self.tabCar)
        self.line.setGeometry(QtCore.QRect(5, 80, 220, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tabCar)
        self.line_2.setGeometry(QtCore.QRect(5, 250, 220, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.infoCar3 = QtWidgets.QLabel(self.tabCar)
        self.infoCar3.setGeometry(QtCore.QRect(5, 260, 220, 95))
        self.infoCar3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCar3.setWordWrap(True)
        self.infoCar3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCar3.setObjectName("infoCar3")
        self.tabConfig.addTab(self.tabCar, "")
        self.tabCor = QtWidgets.QWidget()
        self.tabCor.setObjectName("tabCor")
        self.infoCor1 = QtWidgets.QLabel(self.tabCor)
        self.infoCor1.setGeometry(QtCore.QRect(5, 0, 220, 65))
        self.infoCor1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCor1.setWordWrap(True)
        self.infoCor1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCor1.setObjectName("infoCor1")
        self.line_3 = QtWidgets.QFrame(self.tabCor)
        self.line_3.setGeometry(QtCore.QRect(5, 65, 220, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.infoCor2 = QtWidgets.QLabel(self.tabCor)
        self.infoCor2.setGeometry(QtCore.QRect(5, 75, 220, 50))
        self.infoCor2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCor2.setWordWrap(True)
        self.infoCor2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCor2.setObjectName("infoCor2")
        self.numrel = QtWidgets.QDoubleSpinBox(self.tabCor)
        self.numrel.setGeometry(QtCore.QRect(5, 130, 220, 25))
        self.numrel.setDecimals(1)
        self.numrel.setMinimum(0.5)
        self.numrel.setMaximum(1.0)
        self.numrel.setSingleStep(0.1)
        self.numrel.setProperty("value", 0.8)
        self.numrel.setObjectName("numrel")
        self.line_4 = QtWidgets.QFrame(self.tabCor)
        self.line_4.setGeometry(QtCore.QRect(5, 160, 220, 10))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.infoCor3 = QtWidgets.QLabel(self.tabCor)
        self.infoCor3.setGeometry(QtCore.QRect(5, 170, 220, 65))
        self.infoCor3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoCor3.setWordWrap(True)
        self.infoCor3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoCor3.setObjectName("infoCor3")
        self.box2mg = QtWidgets.QGroupBox(self.tabCor)
        self.box2mg.setGeometry(QtCore.QRect(5, 240, 220, 145))
        self.box2mg.setObjectName("box2mg")
        self.sel2mga = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mga.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel2mga.setChecked(True)
        self.sel2mga.setObjectName("sel2mga")
        self.sel2mgb = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mgb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel2mgb.setObjectName("sel2mgb")
        self.sel2mgc = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mgc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel2mgc.setObjectName("sel2mgc")
        self.sel2mgd = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mgd.setGeometry(QtCore.QRect(5, 80, 210, 20))
        self.sel2mgd.setObjectName("sel2mgd")
        self.sel2mge = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mge.setGeometry(QtCore.QRect(5, 100, 210, 20))
        self.sel2mge.setObjectName("sel2mge")
        self.sel2mgf = QtWidgets.QRadioButton(self.box2mg)
        self.sel2mgf.setGeometry(QtCore.QRect(5, 120, 210, 20))
        self.sel2mgf.setObjectName("sel2mgf")
        self.box2mc = QtWidgets.QGroupBox(self.tabCor)
        self.box2mc.setGeometry(QtCore.QRect(5, 390, 220, 155))
        self.box2mc.setObjectName("box2mc")
        self.sel2mca = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mca.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel2mca.setObjectName("sel2mca")
        self.sel2mcb = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mcb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel2mcb.setObjectName("sel2mcb")
        self.sel2mcc = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mcc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel2mcc.setObjectName("sel2mcc")
        self.sel2mcd = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mcd.setGeometry(QtCore.QRect(5, 80, 210, 20))
        self.sel2mcd.setObjectName("sel2mcd")
        self.sel2mce = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mce.setGeometry(QtCore.QRect(5, 100, 210, 20))
        self.sel2mce.setChecked(True)
        self.sel2mce.setObjectName("sel2mce")
        self.sel2mcf = QtWidgets.QRadioButton(self.box2mc)
        self.sel2mcf.setGeometry(QtCore.QRect(5, 130, 210, 20))
        self.sel2mcf.setObjectName("sel2mcf")
        self.line_5 = QtWidgets.QFrame(self.box2mc)
        self.line_5.setGeometry(QtCore.QRect(5, 120, 210, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.tabConfig.addTab(self.tabCor, "")
        self.tabSfm = QtWidgets.QWidget()
        self.tabSfm.setObjectName("tabSfm")
        self.infoSfm1 = QtWidgets.QLabel(self.tabSfm)
        self.infoSfm1.setGeometry(QtCore.QRect(5, 0, 220, 50))
        self.infoSfm1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoSfm1.setWordWrap(True)
        self.infoSfm1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoSfm1.setObjectName("infoSfm1")
        self.line_6 = QtWidgets.QFrame(self.tabSfm)
        self.line_6.setGeometry(QtCore.QRect(5, 50, 220, 10))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.infoSfm2 = QtWidgets.QLabel(self.tabSfm)
        self.infoSfm2.setGeometry(QtCore.QRect(5, 60, 220, 80))
        self.infoSfm2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoSfm2.setWordWrap(True)
        self.infoSfm2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoSfm2.setObjectName("infoSfm2")
        self.box3rf = QtWidgets.QGroupBox(self.tabSfm)
        self.box3rf.setGeometry(QtCore.QRect(5, 140, 220, 125))
        self.box3rf.setObjectName("box3rf")
        self.sel3rfa = QtWidgets.QRadioButton(self.box3rf)
        self.sel3rfa.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel3rfa.setChecked(True)
        self.sel3rfa.setObjectName("sel3rfa")
        self.sel3rfb = QtWidgets.QRadioButton(self.box3rf)
        self.sel3rfb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel3rfb.setObjectName("sel3rfb")
        self.sel3rfc = QtWidgets.QRadioButton(self.box3rf)
        self.sel3rfc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel3rfc.setObjectName("sel3rfc")
        self.sel3rfd = QtWidgets.QRadioButton(self.box3rf)
        self.sel3rfd.setGeometry(QtCore.QRect(5, 80, 210, 20))
        self.sel3rfd.setObjectName("sel3rfd")
        self.sel3rfe = QtWidgets.QRadioButton(self.box3rf)
        self.sel3rfe.setGeometry(QtCore.QRect(5, 100, 210, 20))
        self.sel3rfe.setObjectName("sel3rfe")
        self.infoSfm3 = QtWidgets.QLabel(self.tabSfm)
        self.infoSfm3.setGeometry(QtCore.QRect(5, 280, 220, 80))
        self.infoSfm3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.infoSfm3.setWordWrap(True)
        self.infoSfm3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.infoSfm3.setObjectName("infoSfm3")
        self.line_7 = QtWidgets.QFrame(self.tabSfm)
        self.line_7.setGeometry(QtCore.QRect(5, 270, 220, 10))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.box3mt = QtWidgets.QGroupBox(self.tabSfm)
        self.box3mt.setGeometry(QtCore.QRect(5, 365, 220, 105))
        self.box3mt.setObjectName("box3mt")
        self.sel3mta = QtWidgets.QRadioButton(self.box3mt)
        self.sel3mta.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel3mta.setChecked(False)
        self.sel3mta.setObjectName("sel3mta")
        self.sel3mtb = QtWidgets.QRadioButton(self.box3mt)
        self.sel3mtb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel3mtb.setObjectName("sel3mtb")
        self.sel3mtc = QtWidgets.QRadioButton(self.box3mt)
        self.sel3mtc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel3mtc.setObjectName("sel3mtc")
        self.sel3mtd = QtWidgets.QRadioButton(self.box3mt)
        self.sel3mtd.setGeometry(QtCore.QRect(5, 80, 210, 20))
        self.sel3mtd.setChecked(True)
        self.sel3mtd.setObjectName("sel3mtd")
        self.box3mr = QtWidgets.QGroupBox(self.tabSfm)
        self.box3mr.setGeometry(QtCore.QRect(5, 475, 220, 125))
        self.box3mr.setObjectName("box3mr")
        self.sel3mra = QtWidgets.QRadioButton(self.box3mr)
        self.sel3mra.setGeometry(QtCore.QRect(5, 20, 210, 20))
        self.sel3mra.setChecked(False)
        self.sel3mra.setObjectName("sel3mra")
        self.sel3mrb = QtWidgets.QRadioButton(self.box3mr)
        self.sel3mrb.setGeometry(QtCore.QRect(5, 40, 210, 20))
        self.sel3mrb.setObjectName("sel3mrb")
        self.sel3mrc = QtWidgets.QRadioButton(self.box3mr)
        self.sel3mrc.setGeometry(QtCore.QRect(5, 60, 210, 20))
        self.sel3mrc.setObjectName("sel3mrc")
        self.sel3mrd = QtWidgets.QRadioButton(self.box3mr)
        self.sel3mrd.setGeometry(QtCore.QRect(5, 80, 210, 20))
        self.sel3mrd.setChecked(True)
        self.sel3mrd.setObjectName("sel3mrd")
        self.sel3mre = QtWidgets.QRadioButton(self.box3mr)
        self.sel3mre.setGeometry(QtCore.QRect(5, 100, 210, 20))
        self.sel3mre.setObjectName("sel3mre")
        self.tabConfig.addTab(self.tabSfm, "")
        self.Crear3d_2 = QtWidgets.QPushButton(self.pgn_imagenes)
        self.Crear3d_2.setGeometry(QtCore.QRect(27, 616, 234, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Crear3d_2.setFont(font)
        self.Crear3d_2.setStyleSheet("border-radius: 0px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Crear3d_2.setObjectName("Crear3d_2")
        self.line_8 = QtWidgets.QFrame(self.pgn_imagenes)
        self.line_8.setGeometry(QtCore.QRect(270, 0, 3, 650))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.pgn_imagenes)
        self.line_9.setGeometry(QtCore.QRect(0, 649, 1000, 3))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.stackedWidget.addWidget(self.pgn_imagenes)
        Aplicacion.setCentralWidget(self.centralwidget)
        self.BarraEstado = QtWidgets.QStatusBar(Aplicacion)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.BarraEstado.setFont(font)
        self.BarraEstado.setSizeGripEnabled(False)
        self.BarraEstado.setObjectName("BarraEstado")
        Aplicacion.setStatusBar(self.BarraEstado)
        self.BarraMenu = QtWidgets.QMenuBar(Aplicacion)
        self.BarraMenu.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.BarraMenu.setObjectName("BarraMenu")
        self.MenuArchivo = QtWidgets.QMenu(self.BarraMenu)
        self.MenuArchivo.setObjectName("MenuArchivo")
        Aplicacion.setMenuBar(self.BarraMenu)
        self.NuevoProyecto = QtWidgets.QAction(Aplicacion)
        self.NuevoProyecto.setObjectName("NuevoProyecto")
        self.AbrirProyecto = QtWidgets.QAction(Aplicacion)
        self.AbrirProyecto.setObjectName("AbrirProyecto")
        self.ImportarImagenes = QtWidgets.QAction(Aplicacion)
        self.ImportarImagenes.setEnabled(False)
        self.ImportarImagenes.setObjectName("ImportarImagenes")
        self.Salir = QtWidgets.QAction(Aplicacion)
        self.Salir.setObjectName("Salir")
        self.MenuArchivo.addAction(self.NuevoProyecto)
        self.MenuArchivo.addAction(self.AbrirProyecto)
        self.MenuArchivo.addSeparator()
        self.MenuArchivo.addAction(self.ImportarImagenes)
        self.MenuArchivo.addSeparator()
        self.MenuArchivo.addAction(self.Salir)
        self.BarraMenu.addAction(self.MenuArchivo.menuAction())

        self.retranslateUi(Aplicacion)
        self.stackedWidget.setCurrentIndex(1)
        self.tabConfig.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Aplicacion)

    def retranslateUi(self, Aplicacion):
        _translate = QtCore.QCoreApplication.translate
        Aplicacion.setWindowTitle(_translate("Aplicacion", "Reconstruccion 3D"))
        self.Crear3d.setText(_translate("Aplicacion", "Crear modelo 3D"))
        self.infoCar1.setText(_translate("Aplicacion", "Estos parámetros son requeridos para el cálculo y descripción de las características de cada vista o imagen que se han importado en el proyecto."))
        self.box1md.setTitle(_translate("Aplicacion", "Método descriptor:"))
        self.sel1mda.setText(_translate("Aplicacion", "SIFT"))
        self.sel1mdb.setText(_translate("Aplicacion", "AKAZE FLOAT"))
        self.sel1mdc.setText(_translate("Aplicacion", "AKAZE MLDB"))
        self.box1ca.setTitle(_translate("Aplicacion", "Definición:"))
        self.sel1caa.setText(_translate("Aplicacion", "Normal"))
        self.sel1cab.setText(_translate("Aplicacion", "Alta"))
        self.sel1cac.setText(_translate("Aplicacion", "Ultra"))
        self.infoCar2.setText(_translate("Aplicacion", "Seleccione el método descriptor de características que desea trabajar. Tenga presente que el método \"AKAZE MLDB\" es binario."))
        self.infoCar3.setText(_translate("Aplicacion", "Seleccione la definición que desea obtener, esto es proporcional a la cantidad de características que se hallaran por el método. \"Ultra\" requiere de mucho tiempo de ejecución."))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tabCar), _translate("Aplicacion", "1. Características"))
        self.infoCor1.setText(_translate("Aplicacion", "Estos parámetros son requeridos para el  filtrado geométrico de las características resultantes del método descriptor y la definición."))
        self.infoCor2.setText(_translate("Aplicacion", "Relación de distancia del punto vecino mas cercano. A menor valor tendrá menos puntos falsos."))
        self.infoCor3.setText(_translate("Aplicacion", "Modelo geométrico y método de coincidencia mas cercano son filtros para la estimación de las coincidencias fotométricas."))
        self.box2mg.setTitle(_translate("Aplicacion", "Modelo geométrico"))
        self.sel2mga.setText(_translate("Aplicacion", "Matriz fundamental"))
        self.sel2mgb.setText(_translate("Aplicacion", "Matriz esencial"))
        self.sel2mgc.setText(_translate("Aplicacion", "Matriz homográfica"))
        self.sel2mgd.setText(_translate("Aplicacion", "M.E. Par angular"))
        self.sel2mge.setText(_translate("Aplicacion", "M.E. Ortográfica"))
        self.sel2mgf.setText(_translate("Aplicacion", "M.E. Vertical"))
        self.box2mc.setTitle(_translate("Aplicacion", "Método de coincidencia"))
        self.sel2mca.setText(_translate("Aplicacion", "AUTO"))
        self.sel2mcb.setText(_translate("Aplicacion", "BRUTE FORCE L2"))
        self.sel2mcc.setText(_translate("Aplicacion", "ANN L2"))
        self.sel2mcd.setText(_translate("Aplicacion", "CASCADE HASHING L2"))
        self.sel2mce.setText(_translate("Aplicacion", "FAST CASCADE HASHING L2"))
        self.sel2mcf.setText(_translate("Aplicacion", "BRUTE FORCE HAMMING"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tabCor), _translate("Aplicacion", "2. Correspondencia"))
        self.infoSfm1.setText(_translate("Aplicacion", "Parámetros requeridos para la estimación de la estructura tridimensional."))
        self.infoSfm2.setText(_translate("Aplicacion", "La opción de refinamiento de parámetros intrínsecos, permite ajustar la longitud focal, la posición del punto principal y el coeficiente de distorsión de las imágenes."))
        self.box3rf.setTitle(_translate("Aplicacion", "Ref. intrínsecos"))
        self.sel3rfa.setText(_translate("Aplicacion", "Ajustar todo"))
        self.sel3rfb.setText(_translate("Aplicacion", "No ajustar"))
        self.sel3rfc.setText(_translate("Aplicacion", "Ajuste de longitud focal"))
        self.sel3rfd.setText(_translate("Aplicacion", "Ajuste de punto principal"))
        self.sel3rfe.setText(_translate("Aplicacion", "Ajuste de distorción"))
        self.infoSfm3.setText(_translate("Aplicacion", "Los métodos de triangulación y recesión permite definir como se llevara a cabo el proceso de estimación de la estructura tridimensional del puntos."))
        self.box3mt.setTitle(_translate("Aplicacion", "Método triangulación"))
        self.sel3mta.setText(_translate("Aplicacion", "Transf. Lineal directa"))
        self.sel3mtb.setText(_translate("Aplicacion", "Angular L1"))
        self.sel3mtc.setText(_translate("Aplicacion", "Angular infinito"))
        self.sel3mtd.setText(_translate("Aplicacion", "Profundidad inversa"))
        self.box3mr.setTitle(_translate("Aplicacion", "Método Recesión"))
        self.sel3mra.setText(_translate("Aplicacion", "Transf. Lineal directa"))
        self.sel3mrb.setText(_translate("Aplicacion", "P3P KE"))
        self.sel3mrc.setText(_translate("Aplicacion", "P3P KNEIP"))
        self.sel3mrd.setText(_translate("Aplicacion", "P3P NORDBERG"))
        self.sel3mre.setText(_translate("Aplicacion", "UP2P KUKELOVA"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tabSfm), _translate("Aplicacion", "3. SFM Incremental"))
        self.Crear3d_2.setText(_translate("Aplicacion", "Cargar"))
        self.MenuArchivo.setTitle(_translate("Aplicacion", "Archivo"))
        self.NuevoProyecto.setText(_translate("Aplicacion", "Nuevo proyecto"))
        self.NuevoProyecto.setShortcut(_translate("Aplicacion", "Ctrl+N"))
        self.AbrirProyecto.setText(_translate("Aplicacion", "Abrir proyecto"))
        self.AbrirProyecto.setShortcut(_translate("Aplicacion", "Ctrl+O"))
        self.ImportarImagenes.setText(_translate("Aplicacion", "Importar imagenes"))
        self.ImportarImagenes.setShortcut(_translate("Aplicacion", "Ctrl+I"))
        self.Salir.setText(_translate("Aplicacion", "Salir"))
        self.Salir.setShortcut(_translate("Aplicacion", "Ctrl+E"))
import logos_rc
