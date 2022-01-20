
from PySide2.QtWidgets import (
    QWidget, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget, QLayout
)

class FolderSyncRowWidget(QWidget):

    def __init__(self):
        super(FolderSyncRowWidget, self).__init__();

        widgetLayout = QHBoxLayout()

        detailsColumn = QVBoxLayout()

        remoteFolder = QLabel("Remote folder:")
        localFolder = QLabel("Local folder:")

        detailsColumn.addWidget(remoteFolder)
        detailsColumn.addWidget(localFolder)

        widgetLayout.addLayout(detailsColumn)
        widgetLayout.addStretch()
        widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(widgetLayout)