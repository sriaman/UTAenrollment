import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x9f\x8b\xfb)=\xc3\x97;\xf7\x00\xb1h\x9av\x85\x08'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' } 

