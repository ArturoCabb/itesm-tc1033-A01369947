from pilot import Pilot
from attendant import Attendant
from flight import Flight
from passenger import Passenger
from plane import Plane
from traveller import Traveller

class ReadPilot:
    def read(self):
        file = open("pilots.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        pilots = {}

        for l in lines:
            fields = lines.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            marital_status = fields[6]

            pilot = Pilot(passport, forename, surname, 
                          date_of_birthday, country, gender, marital_status)
            pilots[passport] = pilot
        return pilots

class ReadAttendants:
    def read(self):
        file = open("attendants.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        attendants = {}

        for l in lines:
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            maritial_status = fields[6]

            attendant = Attendant(passport, forename, surname, 
                          date_of_birthday, country, gender, marital_status)
            attendants[passport] = attendant
        return attendants

class ReadFlight:
    def read(self):
        file = open("flights.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        flights = {}

        for l in lines:
            id = flights[0]
            plate = flights[1]
            origin = flights[2]
            destiny = flights[3]
            departure = flights[4]
            arriving = flights[5]
            status = flights[6]
            departure_gate = flights[7]
            take_off_track = flights[8]
            arriving_gate = flights[9]
            landing_track = flights[10]
            pilot = flights[11]
            co_pilot = flights[12]
            attendant = flights[13]

            flight = Flight(id, plate, origin, destiny, departure, 
                            arriving, status, departure_gate, take_off_track, 
                            arriving_gate, landing_track, arriving_gate, 
                            landing_track, pilot, co_pilot, attendant)

            flights[id] = flight
            return flights

class ReadPassenger:
    def read(self):
        file = open("passengers.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        passengers = {}

        for l in lines:
            flight = passengers[0]
            passport = passengers[1]
            clas = passengers[2]
            seat = passengers[3]
            location = passengers[4]

            passenger = Passenger(flight, paspassport, clas, seat, location)

            passengers[flight] = passenger
            return passengers

class ReadPlane:
    def read(self):
        file = open("planes.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        planes = {}

        for l in lines:
            plate = palnes[0]
            manufacturer = planes[1]
            model = planes[2]
            passenger_capacity = planes[3]
            luggage_capacity = planes[4]
            max_speed = planes[5]

            plane = Plane(plate, manufacturer, model, passenger_capacity, 
                          luggage_capacity, max_speed)

            planes[plate] = plane
            return planes

class ReadTraveller:
    def read(self):
        file = open("travellers.csv", "r")
        lines = file.readlines
        lines.pop(0)
        file.close

        travellers = {}

        for l in lines:
            passport = travellers[0]
            forename = travellers[1]
            surname = travellers[2]
            date_of_birth = travellers[3]
            country = travellers[4]
            gender = traveller[5]
            maritial_status = travellers[6]

            traveller = Traveller(paspassport, forename, surname, 
                                  date_of_birth, country, gender, 
                                  maritial_status)

            travellers[passport] = traveller
            return travellers

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