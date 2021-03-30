import re
import socket
import requests
from ping3 import ping


class Services:
    '''
    Supportive class to validate incoming url and extract it's attributes

    _____________
    Attributes:
        url: str

    _____________
    Methods:
        isValidUrl()
        isExistingHost()
        getHostName()
        getHostIp())
    '''
    
    def __init__(self, url: str):
        self.url = url


    def isValidUrl(self) -> bool:
        ''' Takes self.url attribute:str and checks if format is correct with Regex expression '''

        re_match = re.fullmatch(r'^https?://(www.)?\S*', self.url)
        
        return bool(re_match)


    def isExistingHost(self) -> bool: 
        '''
        Takes self.url attribute:str and checks if get() method of requests returns a response
        If correct -> True
        Else -> False 
        '''

        try: 
            requests.get(self.url)
            return True
            
        except: 
            return False


    def getHostName(self) -> str:
        ''' Takes self.url attribute:str and extracts a domain (abc.xyz) from the URL '''

        match = re.fullmatch(r'^https?://(www.)?(\S*?)\/\S*$', self.url)
        domain = match.group(2)

        return domain


    def getHostIP(self) -> str:
        ''' Based on getHostname() method uses host of the URL to lookup an IP address'''

        host = self.getHostName()
        try:
            host_ip = socket.gethostbyname(host)
            return host_ip
        except: 
            return 'Invalid host'