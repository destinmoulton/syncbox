import configparser

settingsfile = "settings.ini"
def get_setting(section,key):
    config = configparser.ConfigParser()
    config.read(settingsfile)
    return config.get(section,key)