# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ConnectionDialog.ui'
#
# Created: Sun Jan 20 13:55:46 2008
#      by: PyQt4 UI code generator 4.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT

class ConnectionDialog(QtGui.QDialog):
	
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		
		#self.setObjectName("ConnectionDialog")
		#ConnectionDialog.resize(QtCore.QSize(QtCore.QRect(0,0,289,277).size()).expandedTo(ConnectionDialog.minimumSizeHint()))
		
		self.vboxlayout = QtGui.QVBoxLayout(self)		
		self.groupBox = QtGui.QGroupBox()

		self.gridlayout = QtGui.QGridLayout(self.groupBox)
		
		self.label = QtGui.QLabel(self.groupBox)
		self.gridlayout.addWidget(self.label,0,0,1,1)
		
		self.userID = QtGui.QLineEdit(self.groupBox)
		self.userID.setObjectName("userID")
		self.gridlayout.addWidget(self.userID,0,1,1,1)
		
		self.label_2 = QtGui.QLabel(self.groupBox)
		self.label_2.setObjectName("label_2")
		self.gridlayout.addWidget(self.label_2,1,0,1,1)
		
		self.password = QtGui.QLineEdit(self.groupBox)
		self.password.setEchoMode(QtGui.QLineEdit.Password)
		self.password.setObjectName("password")
		self.gridlayout.addWidget(self.password,1,1,1,1)
		self.vboxlayout.addWidget(self.groupBox)
		
		self.groupBox_2 = QtGui.QGroupBox()
		self.groupBox_2.setObjectName("groupBox_2")
		
		self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
		self.gridlayout1.setObjectName("gridlayout1")
		
		self.label_3 = QtGui.QLabel(self.groupBox_2)
		self.label_3.setObjectName("label_3")
		self.gridlayout1.addWidget(self.label_3,0,0,1,1)
		
		self.server = QtGui.QLineEdit(self.groupBox_2)
		self.server.setObjectName("server")
		self.gridlayout1.addWidget(self.server,0,1,1,2)
		
		self.label_4 = QtGui.QLabel(self.groupBox_2)
		self.label_4.setObjectName("label_4")
		self.gridlayout1.addWidget(self.label_4,1,0,1,1)
		
		self.port = QtGui.QLineEdit(self.groupBox_2)
		self.port.setObjectName("port")
		self.gridlayout1.addWidget(self.port,1,1,1,1)
		
		self.label_5 = QtGui.QLabel(self.groupBox_2)
		self.label_5.setObjectName("label_5")
		self.gridlayout1.addWidget(self.label_5,2,0,1,1)
		
		self.ressource = QtGui.QLineEdit(self.groupBox_2)
		self.ressource.setObjectName("ressource")
		self.gridlayout1.addWidget(self.ressource,2,1,1,2)
		
		self.useSSL = QtGui.QCheckBox(self.groupBox_2)
		self.useSSL.setObjectName("useSSL")
		self.gridlayout1.addWidget(self.useSSL,1,2,1,1)
		self.vboxlayout.addWidget(self.groupBox_2)
		
		self.buttonBox = QtGui.QDialogButtonBox()
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.vboxlayout.addWidget(self.buttonBox)
		
		self.retranslateUi()
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.on_accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)
		#QtCore.QMetaObject.connectSlotsByName()
		#self.connect(self, SIGNAL("accepted()"), self.saveSettings)
		self.readSettings()
		
		
	def on_accept(self):
		self.saveSettings()
		self.accept()

	def readSettings(self):
		settings = QtCore.QSettings("Trunat", "PyTalk")
		settings.beginGroup("Connection")
		self.userID.setText(settings.value("userID").toString())
		self.password.setText(settings.value("password").toString())
		self.server.setText(settings.value("server").toString())
		self.useSSL.setChecked(settings.value("useSSL", QtCore.QVariant(True)).toBool())

		if self.useSSL.isChecked():
			self.port.setText(settings.value("port", QtCore.QVariant("5223")).toString())
		else:
			self.port.setText(settings.value("port", QtCore.QVariant("5222")).toString())

		self.ressource.setText(settings.value("ressource", QtCore.QVariant("PyTalk")).toString())
		settings.endGroup()

	def saveSettings(self):
		settings = QtCore.QSettings("Trunat", "PyTalk")
		settings.beginGroup("Connection")
		settings.setValue("userID", QtCore.QVariant(self.userID.text()))
		settings.setValue("password", QtCore.QVariant(self.password.text()))
		settings.setValue("server", QtCore.QVariant(self.server.text()))
		settings.setValue("port", QtCore.QVariant(int(self.port.text())))
		settings.setValue("ressource", QtCore.QVariant(self.ressource.text()))
		settings.setValue("useSSL", QtCore.QVariant(self.useSSL.isChecked()))
		settings.endGroup()
		self.emit( SIGNAL("configured()") )
		
	def retranslateUi(self):
		self.setWindowTitle(QtGui.QApplication.translate("ConnectionDialog", "Connection Dialog", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setTitle(QtGui.QApplication.translate("ConnectionDialog", "Login\'s informations", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("ConnectionDialog", "Jabber ID:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("ConnectionDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_2.setTitle(QtGui.QApplication.translate("ConnectionDialog", "Server's informations", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("ConnectionDialog", "Server:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("ConnectionDialog", "Port:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate("ConnectionDialog", "Ressource:", None, QtGui.QApplication.UnicodeUTF8))
		self.ressource.setText(QtGui.QApplication.translate("ConnectionDialog", "PyTalk", None, QtGui.QApplication.UnicodeUTF8))
		self.useSSL.setText(QtGui.QApplication.translate("ConnectionDialog", "Using SSL", None, QtGui.QApplication.UnicodeUTF8))
		
