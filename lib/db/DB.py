import os
from tinydb import TinyDB, Query
from lib.dirs import get_db_dir
class DB():
    filename = 'config.json'
    foldersTable = 'syncfolders'

    def __init__(self):
        self.path = os.path.join(get_db_dir(),self.filename)
        self.db = TinyDB(self.path)
        return None

    def addSyncFolder(self,local,remote):
        table = self.db.table(self.foldersTable)
        table.insert({'local':local, 'remote':remote})

    def getAllSyncFolders(self):
        table = self.db.table(self.foldersTable)
        return table.all()