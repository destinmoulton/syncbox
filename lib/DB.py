import os
from appdirs import user_config_dir
from tinydb import TinyDB, Query
class DB():
    filename = 'config.json'
    foldersTable = 'folders'

    def __init__(self):
        self.path = os.path.join(user_config_dir(),self.filename)
        self.db = TinyDB(self.path)
        return None

    def addFolder(self,local,remote):
        table = self.db.table(self.foldersTable)
        table.insert({'local':local, 'remote':remote})

    def getAllFolders(self):
        table = self.db.table(self.foldersTable)
        return table.all()