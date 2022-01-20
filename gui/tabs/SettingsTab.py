
from appdirs import user_config_dir, user_log_dir
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget
from PySide2.QtGui import QPixmap, QIcon


class SettingsTab(QWidget):
    def __init__(self):
        super(SettingsTab, self).__init__()


        configDirLabel = QLabel("Config directory: " + user_config_dir("syncbox"))
        logDirLabel = QLabel("Log directory: "+user_log_dir("syncbox"))
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(configDirLabel)
        mainLayout.addWidget(logDirLabel)
        self.setLayout(mainLayout)

    def icon(self):
        gearPixmap = QPixmap('assets/graphics/gear.png')
        gearIcon = QIcon(gearPixmap)
        return gearIcon