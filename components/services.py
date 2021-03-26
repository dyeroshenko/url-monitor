import re
import socket
import requests
from ping3 import ping


class Services:
    def __init__(self, url: str):
        self.url = url


    def isValidUrl(self) -> bool:
        re_match = re.fullmatch(r'^https?://(www.)?\S*', self.url)
        
        return bool(re_match)


    def isExistingHost(self) -> bool: 
        try: 
            req = requests.get(self.url)
            return True
        except: 
            return False


    def getHostName(self) -> str:
        match = re.fullmatch(r'^https?://(www.)?(\S*?)\/\S*$', self.url)
        domain = match.group(2)

        return domain


    def getHostIP(self) -> str:
        host = self.getHostName()
        try:
            host_ip = socket.gethostbyname(host)
            return host_ip
        except: 
            return 'Invalid host'