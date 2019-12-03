class Crew:
    def __init__(self, _passport, _forename, _surname, 
                 _date_of_birth, _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Flight:
    def __init__(self, _id, _plate, _origin, _destiny, _departure,
                 _arriving,_status,_departure_gate, _take_off_track,
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

class Passenger:
    def __init__(self, _flight, _passport, _class, _seat, _location):
        self.flight = _flight
        self.passport = _passport
        self.clas = _class
        self.seat = _seat
        self.location = _location

class Plane:
    def __init__(self, _plate, _manufacturer, _model, _passenger_capacity, 
                 _luggage_capacity, _max_speed):
        self.plate = _plate
        self.manufacturer = _manufacturer
        self.model = _model
        self.passenger_capacity = _passenger_capacity
        self.luggage_capacity = _luggage_capacity
        self.max_speed = _max_speed

class Traveller:
    def __init__(self, _passport, _forename, _surname, 
                 _date_of_birth, _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status