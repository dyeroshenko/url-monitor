from dataclasses import dataclass
from ping3 import ping
from typing import Tuple
import requests

from .services import Services

@dataclass
class Responses:
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
    def __init__(self, url):
        self.url = url
        self.service = Services(self.url)
        

    def getUrlResponse(self) -> Tuple[int, str]: 
        req = requests.get(self.url)
        code = req.status_code
        status = self.statuses.get(str(code))

        if code != 200:
            message = f'Something wrong. Error: {code} {status}'
        else: 
            message = f'Looks good! Code: {code}'

        return code, message


    def checkRoundTripTime(self) -> str:
        host = self.service.getHostName()
        rtp = ping(host, unit = 'ms')

        try:
            return f'{str(round(rtp))} ms'
        except: 
            return 'Can not calculate RTT for this resource'