
import os
from appdirs import user_config_dir

appname = "syncbox"

def create_path_if_does_not_exist(path):
    if os.path.isfile(path):
        return True

    return os.mkdir(path)


def get_db_dir():
    path = os.path.join(user_config_dir(), appname)
    create_path_if_does_not_exist(path)
    return path
