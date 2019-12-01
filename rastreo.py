from passenger import *
from editFile import ReadPassenger
class Rastreo(Passenger):
    def __init__(self):
        self.check_in
        self.security
        self.boarded

    def Track(self):
        pasajero = ReadPassenger()
        a = pasajero.read()
        b = ""
        for x in a:
            b = self.passport = x[4]
            print(b)
        
