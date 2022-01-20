
from PySide2.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QTabWidget
from PySide2.QtGui import QPixmap, QIcon
from gui.buttons.SettingsButton import SettingsButton
from gui.tabs.SettingsTab import SettingsTab
from gui.tabs.PowerTab import PowerTab
class MainWindowView(QMainWindow):

    def __init__(self):
        super(MainWindowView, self).__init__()

        self.setWindowTitle("SyncBox")
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)

        settingsTab = SettingsTab()
        powerTab = PowerTab()
        tabs.addTab(settingsTab, settingsTab.icon(), "")
        tabs.addTab(powerTab, powerTab.icon(), "")

        self.setCentralWidget(tabs)

    