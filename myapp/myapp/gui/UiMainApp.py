# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiMainApp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 715)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplwidget = MPL_WIDGET(self.centralwidget)
        self.mplwidget.setObjectName("mplwidget")
        self.horizontalLayout.addWidget(self.mplwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.settings = QtWidgets.QDockWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.settings.setFont(font)
        self.settings.setObjectName("settings")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_vbus = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_vbus.setFont(font)
        self.label_vbus.setObjectName("label_vbus")
        self.verticalLayout.addWidget(self.label_vbus)
        self.SpinBox_vbus = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_vbus.setDecimals(1)
        self.SpinBox_vbus.setMinimum(0.0)
        self.SpinBox_vbus.setMaximum(50.0)
        self.SpinBox_vbus.setSingleStep(0.1)
        self.SpinBox_vbus.setProperty("value", 24.0)
        self.SpinBox_vbus.setObjectName("SpinBox_vbus")
        self.verticalLayout.addWidget(self.SpinBox_vbus)
        self.slider_vbus = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_vbus.setMinimum(0)
        self.slider_vbus.setMaximum(50)
        self.slider_vbus.setSingleStep(5)
        self.slider_vbus.setPageStep(5)
        self.slider_vbus.setProperty("value", 24)
        self.slider_vbus.setOrientation(QtCore.Qt.Horizontal)
        self.slider_vbus.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_vbus.setTickInterval(50)
        self.slider_vbus.setObjectName("slider_vbus")
        self.verticalLayout.addWidget(self.slider_vbus)
        self.label_irun = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_irun.setObjectName("label_irun")
        self.verticalLayout.addWidget(self.label_irun)
        self.SpinBox_irun = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_irun.setDecimals(1)
        self.SpinBox_irun.setMinimum(0.0)
        self.SpinBox_irun.setMaximum(4.0)
        self.SpinBox_irun.setSingleStep(0.1)
        self.SpinBox_irun.setProperty("value", 1.0)
        self.SpinBox_irun.setObjectName("SpinBox_irun")
        self.verticalLayout.addWidget(self.SpinBox_irun)
        self.slider_irun = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_irun.setMinimum(0)
        self.slider_irun.setMaximum(4)
        self.slider_irun.setPageStep(1)
        self.slider_irun.setProperty("value", 1)
        self.slider_irun.setSliderPosition(1)
        self.slider_irun.setOrientation(QtCore.Qt.Horizontal)
        self.slider_irun.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_irun.setTickInterval(10)
        self.slider_irun.setObjectName("slider_irun")
        self.verticalLayout.addWidget(self.slider_irun)
        self.label_spd_t = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_spd_t.setObjectName("label_spd_t")
        self.verticalLayout.addWidget(self.label_spd_t)
        self.SpinBox_spd_t = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_spd_t.setDecimals(0)
        self.SpinBox_spd_t.setMinimum(0.0)
        self.SpinBox_spd_t.setMaximum(1000.0)
        self.SpinBox_spd_t.setSingleStep(1.0)
        self.SpinBox_spd_t.setProperty("value", 500.0)
        self.SpinBox_spd_t.setObjectName("SpinBox_spd_t")
        self.verticalLayout.addWidget(self.SpinBox_spd_t)
        self.slider_spd_t = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_spd_t.setMinimum(0)
        self.slider_spd_t.setMaximum(1000)
        self.slider_spd_t.setSingleStep(10)
        self.slider_spd_t.setPageStep(100)
        self.slider_spd_t.setProperty("value", 500)
        self.slider_spd_t.setOrientation(QtCore.Qt.Horizontal)
        self.slider_spd_t.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_spd_t.setTickInterval(10)
        self.slider_spd_t.setObjectName("slider_spd_t")
        self.verticalLayout.addWidget(self.slider_spd_t)
        self.label_pitch = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_pitch.setObjectName("label_pitch")
        self.verticalLayout.addWidget(self.label_pitch)
        self.SpinBox_pitch = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_pitch.setDecimals(1)
        self.SpinBox_pitch.setMinimum(0.1)
        self.SpinBox_pitch.setMaximum(30.0)
        self.SpinBox_pitch.setSingleStep(0.1)
        self.SpinBox_pitch.setProperty("value", 25.4)
        self.SpinBox_pitch.setObjectName("SpinBox_pitch")
        self.verticalLayout.addWidget(self.SpinBox_pitch)
        self.slider_pitch = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_pitch.setMinimum(1)
        self.slider_pitch.setMaximum(30)
        self.slider_pitch.setProperty("value", 10)
        self.slider_pitch.setSliderPosition(10)
        self.slider_pitch.setOrientation(QtCore.Qt.Horizontal)
        self.slider_pitch.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_pitch.setTickInterval(10)
        self.slider_pitch.setObjectName("slider_pitch")
        self.verticalLayout.addWidget(self.slider_pitch)
        self.label_mu = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_mu.setObjectName("label_mu")
        self.verticalLayout.addWidget(self.label_mu)
        self.SpinBox_mu = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_mu.setDecimals(2)
        self.SpinBox_mu.setMinimum(0.0)
        self.SpinBox_mu.setMaximum(1.0)
        self.SpinBox_mu.setSingleStep(0.01)
        self.SpinBox_mu.setProperty("value", 0.1)
        self.SpinBox_mu.setObjectName("SpinBox_mu")
        self.verticalLayout.addWidget(self.SpinBox_mu)
        self.slider_mu = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_mu.setMinimum(0)
        self.slider_mu.setMaximum(1)
        self.slider_mu.setSingleStep(0)
        self.slider_mu.setPageStep(0)
        self.slider_mu.setProperty("value", 0)
        self.slider_mu.setOrientation(QtCore.Qt.Horizontal)
        self.slider_mu.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_mu.setTickInterval(10)
        self.slider_mu.setObjectName("slider_mu")
        self.verticalLayout.addWidget(self.slider_mu)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.SpinBox_sf = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.SpinBox_sf.setDecimals(1)
        self.SpinBox_sf.setMaximum(10.0)
        self.SpinBox_sf.setSingleStep(0.1)
        self.SpinBox_sf.setProperty("value", 3.0)
        self.SpinBox_sf.setObjectName("SpinBox_sf")
        self.verticalLayout.addWidget(self.SpinBox_sf)
        self.slider_sf = QtWidgets.QSlider(self.dockWidgetContents)
        self.slider_sf.setMaximum(10)
        self.slider_sf.setPageStep(5)
        self.slider_sf.setProperty("value", 3)
        self.slider_sf.setOrientation(QtCore.Qt.Horizontal)
        self.slider_sf.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_sf.setObjectName("slider_sf")
        self.verticalLayout.addWidget(self.slider_sf)
        self.settings.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.settings)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settings.setWindowTitle(_translate("MainWindow", "Parameters"))
        self.label_vbus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Vbus (V)</p></body></html>"))
        self.slider_vbus.setStatusTip(_translate("MainWindow", "Change the wave length of monochromatic light"))
        self.label_irun.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Irun (Arms)</p></body></html>"))
        self.SpinBox_irun.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.slider_irun.setStatusTip(_translate("MainWindow", "Change the width of the rectangular aperture"))
        self.label_spd_t.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">spd_t (mm/s)</p></body></html>"))
        self.SpinBox_spd_t.setStatusTip(_translate("MainWindow", "change the height of the recatangular aperture"))
        self.slider_spd_t.setStatusTip(_translate("MainWindow", "change the height of the recatangular aperture"))
        self.label_pitch.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">pitch (mm)</p></body></html>"))
        self.SpinBox_pitch.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.slider_pitch.setStatusTip(_translate("MainWindow", "Change the side of the square-shaped screen"))
        self.label_mu.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">nut factor mu</p></body></html>"))
        self.SpinBox_mu.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.slider_mu.setStatusTip(_translate("MainWindow", "Change the focal length f2 of the lens L2"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">sf</p></body></html>"))

from gui.mplwidget import MPL_WIDGET
