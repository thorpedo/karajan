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
       return True

    def play(nodenumber):
        return True
    
    def stop(nodenumber):
        return True

    def pause(nodenumber):
        return True

    def add_to_playlist(nodenumber,media_file):
        return True

    def delete_from_playlist(nodenumber,media_file):
        return True

    def get_info(nodenumber):
        return True 

    def seek(nodenumer,percemt):
        return True



if __name__ == "__main__":
    k = Karajan('config.yml')
    k.printServers()