from PySide2.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, 
    QVBoxLayout, QTabWidget, QListWidget,
    QListWidgetItem
)
from PySide2.QtGui import QPixmap, QIcon

from gui.widgets.FolderSyncRowWidget import FolderSyncRowWidget

class FoldersTab(QWidget):
    def __init__(self):
        super(FoldersTab, self).__init__()

        folder = FolderSyncRowWidget()


        foldersList = QListWidget()


        folderItem = QListWidgetItem()
        folderItem.setSizeHint(folder.sizeHint())

        foldersList.addItem(folderItem)
        foldersList.setItemWidget(folderItem, folder)

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(foldersList)
        self.setLayout(mainLayout)

    def icon(self):
        gearPixmap = QPixmap('assets/graphics/folder.png')
        gearIcon = QIcon(gearPixmap)
        return gearIcon