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

        for attendant in self.attendants.values():
            pass

        for pilot in self.pilots.values():
            pass

        for airplane in self.airplanes.values():
            pass

        for traveller in self.travellers.values():
            pass

        report = WriteTheFile(_date, _time, number_empty_tracks, 
                              number_of_occupied_tracks, number_in_check_in,
                              number_of_passengers_in_security, 
                              number_of_passengers_boarder, 
                              number_of_flights_landed, 
                              number_of_flights_departured, 
                              number_of_empty_gates, 
                              number_of_occupied_gates).writeFile()
