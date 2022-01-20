
from PySide2.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget
from PySide2.QtGui import QPixmap, QIcon
class PowerTab(QWidget):
    def __init__(self):
        super(PowerTab, self).__init__()
        testLabel = QLabel("Power")
        mainLayout = QVBoxLayout()

        mainLayout.addWidget(testLabel)
        self.setLayout(mainLayout)

    def icon(self):
        powerPixmap = QPixmap('assets/graphics/power.png')
        powerIcon = QIcon(powerPixmap)
        return powerIcon