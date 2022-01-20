
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QPushButton, QMainWindow, QVBoxLayout
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QIcon

from gui.MainWindowView import MainWindowView
from gui.systray import systray

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

window = MainWindowView()
systray(app, window)