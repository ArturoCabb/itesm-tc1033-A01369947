from editFile import *

class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        time = str(input())
        return date, time

class Airport:
    def __init__(self):
        self.tracks = None
        self.airplanes = None
        self.passengers = None
        self.pilots = None
        self.attendants = "vacío"
        self.travellers = None

    def populated_airport(self):
        self.pilots = ReadPilot().read()
        self.attendants = ReadAttendants().read()
        self.airplanes = ReadAirPlane().read()
        self.flights = ReadFlight().read()
        self.travellers = ReadTraveller().read()

    def generate_statistics(self, _date, _time):
        number_empty_tracks = 0 
        number_of_occupied_tracks = 0
        number_of_empty_gates = 0
        number_of_occupied_gates = 0
        number_in_check_in = 0
        number_of_passengers_in_security = 0 
        number_of_passengers_boarder = 0
        number_of_flights_landed = 0
        number_of_flights_departured = 0

        for flight in self.flights.values():
            # origin
            if flight.origin == "Ciudad de Mexico - MEXICO":
                date = flight.departure.split("_")[0]
                time = flight.departure.split("_")[1]
            else:
                date = flight.arriving.split("_")[0]
                time = flight.arriving.split("_")[1]

            if date == _date and int(time) == int(_time):
                # counting tracks
                if flight.status in ["boarded", "landing"]:
                    number_of_occupied_tracks += 1
                else:
                    number_empty_tracks += 1

                # counting gates
                if flight.status in ["boarded", "landing", "in transit"]:
                    number_of_empty_gates += 1
                else:
                    number_of_occupied_gates += 1
                if flight.status == "landed":
                    number_of_flights_landed += 1
                elif flight.status == "in transit" and flight.id == id:
                    number_of_flights_departured += 1

                for passenger in self.passengers.values():
                    if passenger.flight == flight.id:
                        if passenger.location == "check-in":
                            number_in_check_in += 1
                        elif passenger.location == "security" and passenger.flight == flight.id:
                            number_of_passengers_in_security += 1
                        elif passenger.location == "boarded" and passenger.flight == flight.id:
                            number_of_passengers_boarder += 1

        report = WriteTheFile(_date, _time, number_empty_tracks, 
                              number_of_occupied_tracks, number_in_check_in,
                              number_of_passengers_in_security, 
                              number_of_passengers_boarder, 
                              number_of_flights_landed, 
                              number_of_flights_departured, 
                              number_of_empty_gates, 
                              number_of_occupied_gates).writeFile()

    def modify_flight(self, _id, _plate, _origin, _destiny, _departure, _arriving, 
                      _status, _departure_gate, _take_off_track, _arriving_gate, 
                      _landing_track, _pilot, _co_pilot, _attendant):
        value = self.flights
        var = Flight(_id,_plate, _origin, _destiny, _departure, _arriving, _status, 
                             _departure_gate, _take_off_track, _arriving_gate, 
                             _landing_track, _pilot, _co_pilot, _attendant)
        value[_id+_plate] = var
        self.flights = value
        return self.flights

    def modify_traveller(self, _passport, _forename, _surname, _date_of_birth, 
                         _country, _gender, _marital_status):
        value = self.travellers
        var = Traveller(_passport, _forename, _surname, _date_of_birth, _country,
                        _gender, _marital_status)
        value[_passport] = var
        self.travellers == value
        return self.travellers

    def modify_passenger(self, _flight, _passport, _class, _seat, _location):
        value = self.passengers
        var = Passenger(_flight, _passport, _class, _location)
        value[_passport] = var
        self.passengers = value
        return self.passengers

        #--------------------------------------------------------------------

    def modify_pilot(self, _passport, _forename, _surname, _date_of_birth, 
                     _country, _gender, _marital_status):
        value = self.pilots
        for pilot in self.pilots.values():
            if pilot.passport == _passport:
                value[pilot.passport] = (_passport, _forename, _surname,
                                         _date_of_birth, _country, _gender,
                                         _marital_status)
                self.pilots = value
        return self.pilots
    
    def modify_attendants(self, _passport, _forename, _surname,
                         _date_of_birth, _country, _gender, _marital_status):
        value = self.attendants
        for attendant in self.attendants.values():
            if attendant.passport == _passport:
                value[attendant.passport] = (_passport, _forename, _surname,
                                             _date_of_birth, _country, _gender,
                                             _marital_status)
                self.attendants = value
        return self.attendants
    
    def modify_travellers(self,  _passport, _forename, _surname, 
                          _date_of_birth, _country, _gender, _marital_status):
        value = self.travellers
        for traveller in self.travellers.values():
            if traveller.passport == _passport:
                value[traveller.passport] = (_passport, _forename, _surname,
                                         _date_of_birth, _country, _gender,
                                         _marital_status)
                self.travellers = value
        return self.travllers
    
    def modify_passengers(self, _flight, _passport, _class, _seat, _location):
        value = self.passengers
        for passenger in self.passengers.values():
            if passenger.passport == _passport:
                value[passenger.passport] = (_flight, _passport, _class,
                                         _seat, _location)
                self.passengers = value
        return self.passengers
    
    def modify_flights(self, _id, _plate, _origin, _destiny, _departure, _arriving,
                       _status, _departure_gate, _take_off_track, _arriving_gate,
                       _landing_track, _pilot, _copilot, _attendants):
        value = self.flights
        for flight in self.flights.values():
            if flight.id == _id and flight.plate == _plate:
                value[flight.id+flight.plate] = (_id, _plate, _origin, _destiny,
                                                 _departure, _arriving, _status,
                                                 _departure_gate, _take_off_track,
                                                 _arriving_gate, _landing_track,
                                                 _pilot, _copilot, _attendants)
                self.flights = value
        return self.flights
