import ConfigParser

class Server():
    def __init__(self, config):
       self.port = config.getint('Server', 'port')
       self.host = config.get('Server', 'host')
       self.maxWorkers = config.getint('Server', 'maxWorkers')

class Config:

    def __init__(self):    
        config = ConfigParser.ConfigParser()
        config.read('../conf/config.conf')

        self.server = Server(config)

c = Config()