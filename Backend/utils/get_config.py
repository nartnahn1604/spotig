import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini', encoding='utf-8')

# Read the connection details from the config file
username = config.get('database', 'username')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.getint('database', 'port')
sid = config.get('database', 'sid')
role = config.get('database', 'role')

def getConfig():
    return {
        'username': username,
        'password': password,
        'host': host,
        'port': port,
        'sid': sid,
        'role': role
    }
