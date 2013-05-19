# -*- coding: utf-8 -*-

import sys
import datetime

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL

from jabber import STATUS

from BuddyList import BuddyList

from ui.ConnectionDialog import ConnectionDialog
from ConnectorThread import ConnectorThread

class MainWindow(QtGui.QMainWindow):
	
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		
		self.connectorThread = None
		
		self.setObjectName("MainWindow")
		self.setMaximumWidth(300)
		self.setMaximumHeight(600)
		
		#self.resize(QtCore.QSize(QtCore.QRect(0,0,316,407).size()).expandedTo(MainWindow.minimumSizeHint()))
		self.setWindowIcon(QtGui.QIcon("images/im-jabber.png"))
		self.setUnifiedTitleAndToolBarOnMac(False)

		## Central Widget and Layout
		self.centralwidget = QtGui.QWidget()
		#self.centralwidget.setObjectName("centralwidget")

		self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
		#self.vboxlayout.setObjectName("vboxlayout")

		self.statusCombo = QtGui.QComboBox(self.centralwidget)
		#self.statusBox.setObjectName("statusBox")
		self.vboxlayout.addWidget(self.statusCombo)

		self.statusEdit = QtGui.QLineEdit(self.centralwidget)
		#self.statusEdit.setObjectName("statusEdit")
		self.vboxlayout.addWidget(self.statusEdit)
		self.setCentralWidget(self.centralwidget)

		self.menubar = QtGui.QMenuBar()
		self.menubar.setGeometry(QtCore.QRect(0,0,316,29))
		#self.menubar.setObjectName("menubar")

		self.menuContacts = QtGui.QMenu(self.menubar)
		#self.menuContacts.setObjectName("menuContacts")

		self.menuAffichage = QtGui.QMenu(self.menubar)
		#self.menuAffichage.setObjectName("menuAffichage")

		self.menuHelp = QtGui.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")

		self.menuBuddies = QtGui.QMenu(self.menubar)
		self.menuBuddies.setObjectName("menuBuddies")

		self.menuTools = QtGui.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")
		self.setMenuBar(self.menubar)

		self.actionConnection = QtGui.QAction(self)
		self.actionConnection.setIcon(QtGui.QIcon("images/status/log-in.png"))
		self.actionConnection.setObjectName("actionConnection")

		self.actionDeconnection = QtGui.QAction(self)
		self.actionDeconnection.setEnabled(False)
		self.actionDeconnection.setIcon(QtGui.QIcon("images/status/log-out.png"))
		self.actionDeconnection.setObjectName("actionDeconnection")

		self.actionOffline_buddies = QtGui.QAction(self)
		self.actionOffline_buddies.setCheckable(True)
		self.actionOffline_buddies.setObjectName("actionOffline_buddies")

		self.actionAway_buddies = QtGui.QAction(self)
		self.actionAway_buddies.setCheckable(True)
		self.actionAway_buddies.setChecked(True)
		self.actionAway_buddies.setObjectName("actionAway_buddies")

		self.actionAbout = QtGui.QAction(self)
		self.actionAbout.setIcon(QtGui.QIcon("images/about.png"))
		self.actionAbout.setObjectName("actionAbout")

		self.actionAboutQt = QtGui.QAction(self)
		self.actionAboutQt.setIcon(QtGui.QIcon("images/qt4.png"))
		self.actionAboutQt.setObjectName("actionAboutQt")

		self.actionQuit = QtGui.QAction(self)
		self.actionQuit.setIcon(QtGui.QIcon("images/exit.png"))
		self.actionQuit.setObjectName("actionQuit")

		self.actionAdd_a_buddy = QtGui.QAction(self)
		self.actionAdd_a_buddy.setIcon(QtGui.QIcon("images/plus.png"))
		self.actionAdd_a_buddy.setObjectName("actionAdd_a_buddy")

		self.actionAdd_a_group = QtGui.QAction(self)
		self.actionAdd_a_group.setIcon(QtGui.QIcon("images/plus.png"))
		self.actionAdd_a_group.setObjectName("actionAdd_a_group")

		self.actionPreferences = QtGui.QAction(self)
		self.actionPreferences.setIcon(QtGui.QIcon("images/preferences.png"))
		self.actionPreferences.setObjectName("actionPreferences")

		self.actionConsole = QtGui.QAction(self)
		self.actionConsole.setObjectName("actionConsole")
		self.menuContacts.addAction(self.actionConnection)
		self.menuContacts.addAction(self.actionDeconnection)
		self.menuContacts.addAction(self.actionQuit)
		self.menuAffichage.addAction(self.actionOffline_buddies)
		self.menuAffichage.addAction(self.actionAway_buddies)
		self.menuHelp.addAction(self.actionAbout)
		self.menuHelp.addAction(self.actionAboutQt)
		self.menuBuddies.addAction(self.actionAdd_a_buddy)
		self.menuBuddies.addAction(self.actionAdd_a_group)
		self.menuTools.addAction(self.actionPreferences)
		self.menuTools.addAction(self.actionConsole)
		self.menubar.addAction(self.menuContacts.menuAction())
		self.menubar.addAction(self.menuBuddies.menuAction())
		self.menubar.addAction(self.menuAffichage.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.console = QtGui.QDialog()
		self.te = QtGui.QTextEdit(self.console)
		self.te.setReadOnly(True)
		vl = QtGui.QVBoxLayout()
		vl.addWidget(self.te)
		self.console.setLayout(vl)
		
		# Set status Offline
		self.statusCombo.setCurrentIndex(5)
		self.statusEdit.hide()

		# Set connect
		self.connect(self.statusCombo, SIGNAL("currentIndexChanged(int)"), self.on_change_status)
		self.connect(self.statusEdit, SIGNAL("returnPressed()"), self.on_change_status)

		# Set BuddyList
		self.buddyList = BuddyList(self)
		self.vboxlayout.insertWidget(0, self.buddyList)
		self.connect(self.buddyList, SIGNAL("rename"), self.on_add_buddy)
		
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(self)



		# Connection
		"""
		connection = ConnectionDialog(self)
		self.connect(self.actionConnection, SIGNAL("triggered()"), connection, SLOT("exec()"))
		self.connect(self.actionDeconnection, SIGNAL("triggered()"), self.disconnect)
		self.connect(connection, SIGNAL("configured()"), self.on_connection)
		"""
		
		# Contacts
		self.connect(self.actionAdd_a_buddy, SIGNAL("triggered()"), self.on_add_buddy)
		self.connect(self.actionAdd_a_group, SIGNAL("triggered()"), self.on_add_group)

		# View
		self.connect(self.actionAway_buddies, SIGNAL("toogled()"), self.setAway)
		self.connect(self.actionOffline_buddies, SIGNAL("toogled()"), self.setOffline)
		self.connect(self.actionAway_buddies, SIGNAL("triggered()"), self.setAway)
		self.connect(self.actionOffline_buddies, SIGNAL("triggered()"), self.setOffline)

		# Tools
		self.connect(self.actionConsole, SIGNAL("triggered()"), self.swapConsole)
		
		# About Dialog
		"""
		about = AboutDialog(self)
		self.connect(self.actionAbout, SIGNAL("triggered()"), about, SLOT("exec()"))
		self.connect(self.actionAboutQt, SIGNAL("triggered()"), QApplication.instance(), SLOT("aboutQt()"))
		"""
		
		# Quit Signal connection
		self.connect(self.actionQuit, SIGNAL("triggered()"), self.quit)
		
		## Show the Connection dialog after a few moments
		QtCore.QTimer.singleShot(500, self.show_connection_dialog)
		
	def retranslateUi(self, MainWindow):
		self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyTalk", None, QtGui.QApplication.UnicodeUTF8))
		
		self.statusCombo.addItem(QtGui.QIcon("images/status/available.png"),QtGui.QApplication.translate("MainWindow", "Available", None, QtGui.QApplication.UnicodeUTF8))
		self.statusCombo.addItem(QtGui.QIcon("images/status/chat.png"),QtGui.QApplication.translate("MainWindow", "Chat", None, QtGui.QApplication.UnicodeUTF8))
		self.statusCombo.addItem(QtGui.QIcon("images/status/busy.png"),QtGui.QApplication.translate("MainWindow", "Do not disturb", None, QtGui.QApplication.UnicodeUTF8))
		self.statusCombo.addItem(QtGui.QIcon("images/status/away.png"),QtGui.QApplication.translate("MainWindow", "Away", None, QtGui.QApplication.UnicodeUTF8))
		self.statusCombo.addItem(QtGui.QIcon("images/status/extended-away.png"),QtGui.QApplication.translate("MainWindow", "Extended Away", None, QtGui.QApplication.UnicodeUTF8))
		self.statusCombo.addItem(QtGui.QIcon("images/status/offline.png"),QtGui.QApplication.translate("MainWindow", "Offline", None, QtGui.QApplication.UnicodeUTF8))
		
		self.menuContacts.setTitle(QtGui.QApplication.translate("MainWindow", "Account", None, QtGui.QApplication.UnicodeUTF8))
		self.menuAffichage.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
		self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
		self.menuBuddies.setTitle(QtGui.QApplication.translate("MainWindow", "Buddies", None, QtGui.QApplication.UnicodeUTF8))
		self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
		self.actionConnection.setText(QtGui.QApplication.translate("MainWindow", "L&og in", None, QtGui.QApplication.UnicodeUTF8))
		self.actionConnection.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
		self.actionDeconnection.setText(QtGui.QApplication.translate("MainWindow", "Log out", None, QtGui.QApplication.UnicodeUTF8))
		self.actionOffline_buddies.setText(QtGui.QApplication.translate("MainWindow", "Offline buddies", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAway_buddies.setText(QtGui.QApplication.translate("MainWindow", "Away buddies", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About pyTalk", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
		self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAdd_a_buddy.setText(QtGui.QApplication.translate("MainWindow", "Add a buddy", None, QtGui.QApplication.UnicodeUTF8))
		self.actionAdd_a_group.setText(QtGui.QApplication.translate("MainWindow", "Add a group", None, QtGui.QApplication.UnicodeUTF8))
		self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
		self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
		self.actionConsole.setText(QtGui.QApplication.translate("MainWindow", "XML Console", None, QtGui.QApplication.UnicodeUTF8))
		

		
	def show_connection_dialog(self):
		d = ConnectionDialog(self)
		if d.exec_():
			self.on_connection()
			self.on_change_status(0)
			#self.statusCombo.set

	def on_connection(self, status=STATUS.available):
		if not self.connectorThread:
			self.connectorThread = ConnectorThread(status)
			self.connectorThread.start()
			self.connect(self.connectorThread, SIGNAL("message"), self.buddyList.message)
			self.connect(self.connectorThread, SIGNAL("error"), self.error)
			self.connect(self.connectorThread, SIGNAL("connected()"), self.connected)
			self.connect(self.connectorThread, SIGNAL("disconnected()"), self.disconnect)
			self.connect(self.connectorThread, SIGNAL("presence"), self.buddyList.presence)
			self.connect(self.connectorThread, SIGNAL("debug"), self.debug)
			self.connect(self.connectorThread, SIGNAL("subscriptionRequest"), self.subscriptionRequest)
			self.connect(self.connectorThread, SIGNAL("addBuddy"), self.on_add_buddy)
			
		elif self.connectorThread.isConnected():
			self.connectorThread.change_status(status, self.statusEdit.text())
			self.statusEdit.clearFocus()

	def disconnect(self):
		self.actionConnection.setEnabled(True)
		self.actionDeconnection.setEnabled(False)
		self.statusEdit.hide()
		self.statusBox.setCurrentIndex(STATUS.unavailable.index)
		if self.connectorThread:
			self.connectorThread.disconnect()
			self.connectorThread = None
		self.BuddyList.clear()
		QtGui.QApplication.instance().quit()
		
			
	def connected(self):
		self.actionConnection.setEnabled(False)
		self.actionDeconnection.setEnabled(True)
		if self.statusCombo.currentIndex() == STATUS.unavailable:
			self.statusCombo.setCurrentIndex(STATUS.available)
		else:
			self.connectorThread.set_status(self.statusCombo.currentIndex(), self.statusEdit.text())
		self.statusEdit.show()
		self.statusEdit.setFocus()
		self.BuddyList.setConnection(self.connectorThread)
		self.getRoster()
		self.setAway()
		self.setOffline()

	def error(self, title, content):
		QtGui.QMessageBox.critical(self, title, content, QtGui.QMessageBox.Ok)

	def closeEvent(self, event):
		self.quit()

	def quit(self):
		self.disconnect()
		sys.exit(0)

	def on_change_status(self, index=-1):
		print "on_status", index
		if index == -1:
			index = self.statusBox.currentIndex()
		if index == STATUS.unavailable:
			self.statusEdit.hide()
			self.disconnect()
		#else:
		#	self.connection(index)

	def getRoster(self):
		roster = self.connectorThread.getRoster()
		for buddy in roster:
			self.buddyList.add_item(buddy)
		self.connect(self.buddyList, SIGNAL("itemDoubleClicked(QTreeWidgetItem *,int)"), self.on_send_message)

	def on_send_message(self, item, col):
		print "on_send_message", item, col
		if item and item.type() == QtGui.QTreeWidgetItem.UserType+1:
			item.sendMessage()
			
	def setAway(self, checked=-1):
		if checked == -1:
			checked = self.actionAway_buddies.isChecked()
		self.BuddyList.setAway(not checked)
			
	def setOffline(self, checked=-1):
		if checked == -1:
			checked = self.actionOffline_buddies.isChecked()
		self.BuddyList.setOffline(not checked)

	def subscriptionRequest(self, presence):
		request = RosterRequest(self, self.connectorThread.jabber, presence)
		request.show()

	def debug(self, message):
		self.te.append(datetime.datetime.now().strftime("[%H:%M:%S]")+" : \n"+message)

	def swapConsole(self):
		self.console.setWindowTitle("XML Console")
		self.console.resize(QtCore.QSize(1024, 500))
		self.console.show()
		self.console.raise_()

	def on_add_buddy(self, item=None):
		if self.connectorThread:
			if item:
				jid = item.jid
			else:
				jid = ""
			newBuddy = AddBuddyDialog(self, self.connectorThread.jabber, self.BuddyList.groups.keys(), jid)
			newBuddy.show()

	def on_add_group(self):
		newGroup = AddGroupDialog(self, self.BuddyList)
		newGroup.show()
