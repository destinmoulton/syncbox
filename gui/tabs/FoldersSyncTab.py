from PySide2.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, 
    QVBoxLayout, QTabWidget, QListWidget,
    QListWidgetItem, QStackedLayout
)
from PySide2.QtGui import QPixmap, QIcon

from gui.widgets.FolderSyncRowWidget import FolderSyncRowWidget
from gui.widgets.SyncFoldersMenu import SyncFoldersMenu

class FoldersSyncTab(QWidget):
    def __init__(self):
        super(FoldersSyncTab, self).__init__()

        mainLayout = QVBoxLayout()

        mainLayout.addWidget()
        
        self.setLayout(mainLayout)

    def icon(self):
        gearPixmap = QPixmap('assets/graphics/folder.png')
        gearIcon = QIcon(gearPixmap)
        return gearIcon

    def viewList(self):

        folder = FolderSyncRowWidget()

        syncMenu = SyncFoldersMenu()
        syncMenu.setAddButtonHandler(self.viewForm)
        foldersList = QListWidget()

        folderItem = QListWidgetItem()
        folderItem.setSizeHint(folder.sizeHint())

        foldersList.addItem(folderItem)
        foldersList.setItemWidget(folderItem, folder)

        mainLayout = QVBoxLayout()

        mainLayout.addWidget(syncMenu)
        mainLayout.addWidget(foldersList)
        self.setLayout(mainLayout)

    def viewForm(self):
        print("viewForm called")
        layout = QVBoxLayout()

        testLabel = QLabel("Form")
        layout.addWidget(testLabel)
        self.setLayout(layout)
