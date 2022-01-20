
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget
from PySide2.QtGui import QPixmap, QIcon
class SettingsTab(QWidget):
    def __init__(self):
        super(SettingsTab, self).__init__()
        testLabel = QLabel("TEST")
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(testLabel)
        self.setLayout(mainLayout)

    def icon(self):
        gearPixmap = QPixmap('assets/graphics/gear.png')
        gearIcon = QIcon(gearPixmap)
        return gearIcon