from dataclasses import dataclass
from ping3 import ping
from typing import Tuple
import requests

from .services import Services

@dataclass
class Responses:
    '''
    Class to store code:description mapping for HTTP responses
    '''
    
    statuses = {
                        '200': 'OK!',

                        '400': 'Bad Request',

                        '401': 'Unauthorized',

                        '403': 'Forbidden',

                        '404': 'Not Found',

                        '405': 'Method Not Allowed',

                        '406': 'Not Acceptable',

                        '407': 'Proxy Authentication Required',

                        '408': 'Request Timeout',

                        '409': 'Conflict',

                        '410': 'Gone',

                        '411': 'Length Required',

                        '412': 'Precondition Failed',

                        '413': 'Payload Too Large',

                        '414': 'URI Too Long',

                        '415': 'Unsupported Media Type',

                        '416': 'Range Not Satisfiable',

                        '417': 'Expectation Failed',

                        '418': 'I\'m a teapot (WTF?)',

                        '422': 'Unprocessable Entity',

                        '425': 'Too Early',

                        '426': 'Upgrade Required',

                        '428': 'Precondition Required',

                        '429': 'Too Many Requests',

                        '431': 'Request Header Fields Too Large',

                        '451': 'Unavailable For Legal Reasons',

                        '500': 'Internal Server Error',

                        '501': 'Not Implemented',

                        '502': 'Bad Gateway',

                        '503': 'Service Unavailable',

                        '504': 'Gateway Timeout',

                        '505': 'HTTP Version Not Supported',

                        '511': 'Network Authentication Required'
                    }


class Status(Responses):
    ''' Class for getting URL stats (response code:description, round-trip-time) '''

    def __init__(self, url):
        self.url = url
        self.service = Services(self.url)
        

    def getUrlResponse(self) -> Tuple[int, str]: 
        ''' Takes [url] attribute and checks HTTP response with requests library.  Returns http code and custom message '''
        
        req = requests.get(self.url)
        code = req.status_code
        status = self.statuses.get(str(code))

        if code != 200:
            message = f'Something wrong. Error: {code} {status}'
        else: 
            message = f'Looks good! Code: {code}'

        return code, message


    def checkRoundTripTime(self) -> str:
        '''
        Takes hostname extracted by Services.getHostName() and pings IP address with ping3 library.
        Returns round-trip-time in ms (string) or customized error
        '''

        host = self.service.getHostName()
        rtp = ping(host, unit = 'ms')

        try:
            return f'{str(round(rtp))} ms'
        except: 
            return 'Can not calculate RTT for this resource'