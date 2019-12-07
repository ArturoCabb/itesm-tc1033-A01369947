from constructor import *

class ReadPilot:
    def read(self):
        pilots = {}
        lines = ""
        try:
            file = open("files/pilots.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error: ", e)

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            marital_status = fields[6]

            pilot = Crew(passport, forename, surname, date_of_birthday, country, 
                          gender, marital_status)

            pilots[passport] = pilot
        return pilots

class ReadAttendants:
    def read(self):
        attendants = {}
        lines = ""
        try:
            file = open("files/attendants.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error: ", e)

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birthday = fields[3]
            country = fields[4]
            gender = fields[5]
            maritial_status = fields[6]

            attendant = Crew(passport, forename, surname, date_of_birthday, 
                             country, gender, maritial_status)

            attendants[passport] = attendant
        return attendants

class ReadFlight:
    def read(self):
        lines = ""
        flights = {}

        try:
            file = open("files/flights.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error: ", e)

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

            flight = Flight(id, plate, origin, destiny, departure, arriving,
                            status, departure_gate, take_off_track, arriving_gate,
                            landing_track, pilot, co_pilot, attendant)

            flights[id+plate] = flight
        return flights

class ReadPassenger:
    def read(self):
        passengers = {}
        lines = ""

        try:
            file = open("files/passengers.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error: ", e)

        for l in lines:
            fields = l.split(",")
            flight = fields[0]
            passport = fields[1]
            clas = fields[2]
            seat = fields[3]
            location = fields[4]

            passenger = Passenger(flight,passport,clas,seat,location)

            passengers[passport] = passenger
        return passengers

class ReadAirPlane:
    def read(self):
        planes = {}
        lines = ""

        try:
            file = open("files/planes.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error: ", e)

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

            planes[plate] = plane
        return planes

class ReadTraveller:
    def read(self):
        travellers = {}
        lines = ""
        try:
            file = open("files/travellers.csv", "r")
            lines = file.readlines()
            file.close()
            lines.pop(0)
        except Exception as e:
            print("Error:", e)

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            forename = fields[1]
            surname = fields[2]
            date_of_birth = fields[3]
            country = fields[4]
            gender = fields[5]
            maritial_status = fields[6]

            traveller = Traveller(passport, forename, surname, 
                                  date_of_birth, country, gender, 
                                  maritial_status)

            travellers[passport] = traveller
        return travellers

class WriteTheFile:
    def __init__(self, _date, _time, _number_of_empty_tracks, _number_of_busy_tracks, 
              _number_in_check_in, _number_of_passengers_in_security, 
              _number_of_passengers_boarder, _number_of_flights_landed, 
              _number_of_flights_departured, _aviable_gates, _occupied_gates):
        self.date = _date
        self.time = _time
        self.empty_tracks = _number_of_empty_tracks
        self.number_in_check_in = _number_in_check_in
        self.passengers_in_security = _number_of_passengers_in_security
        self.passenger_in_boarder = _number_of_passengers_boarder
        self.flights_landed = _number_of_flights_landed
        self.flights_departured = _number_of_flights_departured
        self.aviable_gates = _aviable_gates
        self.occupied_gates = _occupied_gates

    def writeFile(self):
        try:
            file = open("files/statistics.csv", "w+")
            text = (str(self.date) + "," + str(self.time) + "," + str(self.empty_tracks) +
                     "," + str(self.number_in_check_in) + "," + str(self.passengers_in_security)
                    + "," + str(self.passenger_in_boarder) + "," + str(self.flights_landed)
                    + "," + str(self.flights_departured) + "," + str(self.aviable_gates) +
                    "," + str(self.occupied_gates))

            file.write("date,time,number of empty tracks,number of busy tracks," + 
                       "number in check in,number of passengers in security," +
                       "number of passengers boarder,number of flights landed," +
                       "numebr of flights departured,aviable gates,occupied gates\n" + text)
            file.close()
        except Exception as e:
            print("Error al crear archivo: ", e,)

    def writeFile(self, flight, traveller, passenger, m_pilot, m_attendant, 
                  m_traveller, m_passenger, m_flight):
        try:
            with open('flights.csv', 'w', newline='') as f:
                w = csv.writer(f)
                if fligth.items() == m_flight.items():
                    for value in fligth.items():
                        w.writerow(value)
            with open('travellers.csv', 'w', newline='') as f:
                w = csv.writer(f)
                if traveller.items() == m_traveller.items():
                    for value in traveller.items():
                        w.writerow(value)
            with open('passengers.csv', 'w', newline='') as f:
                w = csv.writer(f)
                for value in passenger.items():
                    w.writerow(value)
            with open('pilots.csv', 'w', newline='') as f:
                w = csv.writer(f)
                for value in m_pilot.items():
                    w.writerow(value)
            with open('attendants.csv', 'w', newline='') as f:
                w = csv.writer(f)
                for value in attendants.items():
                    w.writerow(value)
        except Exception as e:
            print(e)