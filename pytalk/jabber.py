# -*- coding: utf-8 -*-
from PyQt4.QtGui import QApplication
from enum import Enum

def tr(string):
	return QApplication.translate("Status", string, None, QApplication.UnicodeUTF8)

class STATUS:
	available = 0
	chat = 1
	dnd = 2
	away = 3
	xa = 4
	unavailable = 5
	invisible = 6

DEADSTATUS = Enum('available', 'chat', 'dnd', 'away', 'xa', 'unavailable', 'invisible')
STATUS_TEXT = ['available', 'chat', 'dnd', 'away', 'xa', 'unavailable', 'invisible']
DISPLAY_STATUS  = (tr('Available'), tr('Chat'), tr('Do not Disturb'), tr('Away'), tr('Unavailable'), tr('Offline'), tr('Invisible'))
STATUS_IMAGE    = ('available.png', 'chat.png', 'busy.png', 'away.png', 'extended-away.png', 'offline.png', 'offline.png')
