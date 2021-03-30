from datetime import datetime
from typing import Dict

from .services import Services
from .status import Status
from run import db 
from models import Records

class Handler:
    '''
    A class managing connection between app routes and functionality.
    ____________
    Attributes:
        url: str
        timestamp: str
        services: class
        status: class 
    __________
    Methods:
        checkStatusAndSaveToDB()
        addRecordToDB(url: str, timestamp: str, host: str, ip: str, rtt: str, http_code: int)
        getRecordsFromDB()
    '''

    def __init__(self, url: str = ''):
        self.url = url
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.services = Services(self.url)
        self.status = Status(self.url)


    def checkStatusAndSaveToDB(self) -> Dict[str, int]:
        ''' 1. Validates incoming URL for format and duplicates and save to connected DB. 
            2. Runs underlying checks
           
           If URL is invalid or a duplicate - returns dict with error 
        '''

        if self.services.isValidUrl() and self.services.isExistingHost():
            host_name = self.services.getHostName()
            host_ip = self.services.getHostIP()
            code, message = self.status.getUrlResponse()
            round_trip_time = self.status.checkRoundTripTime()

            self.addRecordToDB(
                               url = self.url.rstrip('/'),
                               timestamp = self.timestamp, 
                               host = host_name, 
                               ip = host_ip, 
                               rtt = round_trip_time,
                               http_code = code
                            )

            data = {
                    'url': self.url.rstrip('/'),
                    'host': host_name, 
                    'ip': host_ip, 
                    'code': code, 
                    'message': message,
                    'round-trip-time': round_trip_time, 
                    'checked': self.timestamp
                    }

            return data
        
        else:
            return {'error': 'Can not scan this URL. Either URL address is malformed or host (domain) name is invalid'}


    def addRecordToDB(self, url: str, timestamp: str, host: str, ip: str, rtt: str, http_code: int) -> None:
        ''' Supportive method to add handled URL to DB along with attributes '''

        newRecord = Records(url, timestamp, host, ip, rtt, http_code)

        db.session.add(newRecord)
        db.session.commit()


    def getRecordsFromDB(self) -> object:
        '''Get all processed URLs from DB and returns SQLAlchemy object with accessible attributes: 
            records.url, 
            records.message,
            etc
        '''

        records = Records.query.order_by(Records._id.desc()).all()
        db.session.commit()

        return records