
from PySide2.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, 
    QTabWidget, QLayout, QPushButton
)
from PySide2.QtGui import QPixmap, QIcon
class SyncFoldersMenu(QWidget):

    def __init__(self):
        super(SyncFoldersMenu, self).__init__();

        widgetLayout = QHBoxLayout()

        addPixmap = QPixmap('assets/graphics/plus-sign.png')
        addIcon = QIcon(addPixmap)
        addButton = QPushButton(addIcon, " Sync Folder")
        self.addButton = addButton

        widgetLayout.addWidget(addButton)
        widgetLayout.addStretch()
        widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(widgetLayout)

    def setAddButtonHandler(self, handler):
        self.addButton.clicked.connect(handler)