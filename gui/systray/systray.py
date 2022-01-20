
from PySide2.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PySide2.QtGui import QIcon
def systray(qtapp, qtwindow):
    # Create the icon
    icon = QIcon("assets/graphics/icon.png")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()
    action = QAction("Open SyncBox")
    action.triggered.connect(qtwindow.show)
    menu.addAction(action)

    # Add a Quit option to the menu.
    quit = QAction("Quit")
    quit.triggered.connect(qtapp.quit)
    menu.addAction(quit)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    qtapp.exec_();
