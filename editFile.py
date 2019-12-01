from pilot import Pilot
from attendant import Attendant
from flight import Flight
from passenger import Passenger
from plane import Plane
from traveller import Traveller

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
        passenger1 = []

        for l in lines:
            fields = l.split(",")
            flight = fields[0]
            passport = fields[1]
            clas = fields[2]
            seat = fields[3]
            location = fields[4]

            passenger = Passenger(flight, passport, clas, seat, location)

            passenger1 = passenger
            passengers[flight] = fields

        return passengers, passenger1

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