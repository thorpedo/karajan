#!/usr/bin/python3

import socket
import yaml


class Karajan:
    def __init__(self,config_file):
        with open(config_file) as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
            print(self.config)

    def printServers(self):
        for nodo in self.config['servers']:
            print (nodo['ip']+":"+str(nodo['port']))

    def checkServers(self):
        result =[]
        for nodo in self.config['servers']:
            response = self.makeRequest(nodo['ip'],nodo['port'],'help') 
            print(response)
        return True

    def play(self,nodenumber):
        return True
    
    def stop(self,nodenumber):
        return True

    def pause(self,nodenumber):
        return True

    def add_to_playlist(self,nodenumber,media_file):
        return True

    def delete_from_playlist(self,nodenumber,media_file):
        return True

    def get_info(self,nodenumber):
        return True 

    def seek(self,nodenumer,percemt):
        return True

    def makeRequest(self,host,port,cmd):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
             s.connect((host, int(port) ))
             comando = cmd+"\r\n"
             s.sendall(b'cmd')
             data = s.recv(1024)
        return repr(data)





if __name__ == "__main__":
    k = Karajan('config.yml')
    k.checkServers()

