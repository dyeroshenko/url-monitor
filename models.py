from run import db 

class Records(db.Model):
    ''' SQL Alchemy database table schema with columns listed below:  '''

    _id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), unique=False)
    timestamp = db.Column(db.String(25), unique=False)
    host = db.Column(db.String(25), unique=False)
    ip = db.Column(db.String(25), unique=False)
    rtt = db.Column(db.String(10), unique=False)
    http_code = db.Column(db.Integer, unique=False)

    def __init__(self, url, timestamp, host, ip, rtt, http_code): 
        ''' Initializes attributes from schema '''

        self.url = url
        self.timestamp = timestamp
        self.host = host
        self.ip = ip
        self.rtt = rtt
        self.http_code = http_code

    def __str__(self) -> str:
        ''' Overloads string operator while using DB results for debugging / testing '''
        
        return f'{self.url}, {self.timestamp}, {self.host}, {self.ip}, {self.rtt}, {self.http_code}'