class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        hour = str(input())
        hola = Track()
        print(hola)

class ReadPilot:
    def read(self):
        file = open("sources\pilots.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        pilots = {}
        pilot1 = []

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            marital_status = fields[6]

            pilot = Pilot(passport, forename, surname, 
                          date_of_birthday, country, gender, marital_status)
            
            pilot1 = pilot
            pilots[passport] = fields

        return pilots, pilot1

class ReadAttendants:
    def read(self):
        file = open("sources\attendants.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        attendants = {}
        attendant1 = []

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            maritial_status = fields[6]

            attendant = Attendant(passport, forename, surname, 
                          date_of_birthday, country, gender, marital_status)

            attendants[passport] = fields
            attendant1 = attendant

        return attendants, attendant1

class ReadFlight:
    def read(self):
        file = open("flights.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        flights = {}
        flight1 = []

        for l in lines:
            fields = l.split(",")
            id = fields[0]
            plate = fields[1]
            origin = fields[2]
            destiny = fields[3]
            departure = fields[4]
            arriving = fields[5]
            status = fields[6]
            departure_gate = fields[7]
            take_off_track = fields[8]
            arriving_gate = fields[9]
            landing_track = fields[10]
            pilot = fields[11]
            co_pilot = fields[12]
            attendant = fields[13]

            flight = Flight(id, plate, origin, destiny, departure, 
                            arriving, status, departure_gate, take_off_track, 
                            arriving_gate, landing_track, arriving_gate, 
                            landing_track, pilot, co_pilot, attendant)

            flight1 = flight
            flights[id] = fields

            return flights, flight1

class ReadPassenger:
    def read(self):
        file = open("sources\passengers.csv", "r")
        lines = file.readlines()
        lines.pop(0)
        file.close

        passengers = {}

        for l in lines:
            fields = l.split(",")
            flight = fields[0]
            passport = fields[1]
            clas = fields[2]
            seat = fields[3]
            location = fields[4]

            passengers[passport] = fields

        return passengers

class ReadPlane:
    def read(self):
        file = open("planes.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        planes = {}

        for l in lines:
            fields = l.split(",")
            plate = fields[0]
            manufacturer = fields[1]
            model = fields[2]
            passenger_capacity = fields[3]
            luggage_capacity = fields[4]
            max_speed = fields[5]

            plane = Plane(plate, manufacturer, model, passenger_capacity, 
                          luggage_capacity, max_speed)

            planes[plate] = fileds
            plane1 = plane

            return planes, plane1

class ReadTraveller:
    def read(self):
        file = open("travellers.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        travellers = {}
        traveller1 = []

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birth = fields[3]
            country = fields[4]
            gender = fields[5]
            maritial_status = fields[6]

            traveller = Traveller(paspassport, forename, surname, date_of_birth, 
                                  country, gender, maritial_status)

            travellers[passport] = fields
            traveller1 = traveller

            return travellers, traveller1

class WriteTheFile:
    def __init__(self, _date, _time):
        self.date = _date
        self.time = _time

    def write(self, _number_of_empty_tracks, _number_of_busy_tracks, 
              _number_in_check_in, _number_of_passengers_in_security, 
              _number_of_passengers_boarder, _number_of_flights_landed, 
              _number_of_flights_departured, _aviable_gates = [], _occupied_gates = []):
        file = open("statistics.csv", "w+")
        text = (self.date + "," + self.time + "," + _number_of_empty_tracks + 
                "," + _number_of_busy_tracks + "," + _number_in_check_in + 
                "," + _number_of_passengers_in_security + "," + _number_of_passengers_boarder
                + "," + _number_of_flights_landed + "," + _number_of_flights_departured +
                "," + _aviable_gates + "," + _occupied_gates)

        file = file.write("date,time,number of empty tracks,number of busy tracks," + 
                   "number in check in,number of passengers in security," +
                   "number of passengers boarder,number of flights landed," +
                   "numebr of flights departured,aviable gates,occupied gates\n")
        file = file.write(text)
        file.close

class Traveller:
    def __init__(self, _passport, _forename, _surname, 
                 _date_of_birth, _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birtth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Plane:
    def __init__(self, _plate, _manufacturer, _model, _passenger_capacity, 
                 _luggage_capacity, _max_speed):
        self.plate = _plate
        self.manufacturer = _manufacturer
        self.model = _model
        self.passenger_capacity = _passenger_capacity
        self.luggage_capacity = _luggage_capacity
        self.max_speed = _max_speed

class Pilot:
    def __init__(self, _passport, _forename, _surname, _date_of_birth, 
                 _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Passenger:
    def __init__(self):
        self.flight = _flight
        self.passport = _passport
        self.clas = _class
        self.seat = _seat
        self.location = _location

class Flight:
    def __init__(self, _id, _plate, _origin, _destiny, _departure, 
                 _arriving, _status, _departure_gate, _take_off_track, 
                 _arriving_gate, _landing_track, _pilot, _copilot, 
                 _attendants):
        self.id = _id
        self.plate = _plate
        self.origin = _origin
        self.destiny = _destiny
        self.departure = _departure
        self.arriving = _arriving
        self.status = _status
        self.departure_gate = _departure_gate
        self.take_off_track = _take_off_track
        self.arriving_gate = _arriving_gate
        self.landing_track = _landing_track
        self.pilot = _pilot
        self.copilot = _copilot
        self.attendants = _attendants

class Attendant:
    def __init__(self, _passport, _forename, _surname, 
                 _date_of_birth, _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status