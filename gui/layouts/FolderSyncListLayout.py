

from PySide2.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, 
    QTabWidget, QLayout, QPushButton, QListWidgetItem, 
    QListWidget
)

from gui.widgets.FolderSyncRowWidget import FolderSyncRowWidget
from gui.widgets.SyncFoldersMenu import SyncFoldersMenu

class FolderSyncListLayout(QVBoxLayout):
    def __init__(self):
        super(FolderSyncListLayout, self).__init__()
        folder = FolderSyncRowWidget()

        syncMenu = SyncFoldersMenu()
        syncMenu.setAddButtonHandler(self.viewForm)
        foldersList = QListWidget()

        folderItem = QListWidgetItem()
        folderItem.setSizeHint(folder.sizeHint())

        foldersList.addItem(folderItem)
        foldersList.setItemWidget(folderItem, folder)

        self.addWidget(syncMenu)
        self.addWidget(foldersList)
