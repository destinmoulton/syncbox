
from PySide2.QtWidgets import QPushButton 
from PySide2.QtGui import QPixmap, QIcon
class SettingsButton():

    def __init__(self):
        return None

    def get(self):
        gearPixmap = QPixmap('assets/graphics/gear.png')
        gearIcon = QIcon(gearPixmap)
        settingsButton = QPushButton()
        settingsButton.setIcon(gearIcon);
        return settingsButton