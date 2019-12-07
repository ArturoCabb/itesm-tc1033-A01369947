from AirPort import *
# -*- coding: utf-8 -*-
#Arturo Caballero Ortega
#Erik Patricio Trujillo Barrientos

if __name__ == "__main__":
    while 1:
        print("¿Qué desea hacer?\n\r1.Hacer consulta\n\r2.Editar\n\r3.Modificar\n\r4.Salir")
        i = input()
        if i == 1:
            airport = UserInput()
            date, time = airport.datos()
            my_airport = Airport()
            my_airport.populated_airport()
            my_airport.generate_statistics(date, time)
        elif i == 2:
            id = input("Ingrese el id: ")
            pate = input("Ingrese el pate: ")
            origin = input("Ingrese el origin: ")
            destiny = input("Ingrese el destiny: ")
            departure = input("Ingrese el departure: ")
            arriving = input("Ingrese el arriving: ")
            status = input("Ingrese el status: ")
            departure_gate = input("Ingrese el departure gate: ")
            take_off_track = input("Ingrese el take of track: ")
            arriving_gate = input("Ingrese el arriving gate: ")
            landing_track = input("Ingrese el landing track: ")
            pilot = input("Ingrese el pilot: ")
            co_pilot = input("Ingrese el copilot: ")
            attendant = input("Ingrese el attendant")
            x = my_airport.modify_flight(id,pate,origin,destiny,departure,
                                         arriving,status,departure_gate,take_off_track
                                         ,arriving_gate,landing_track,pilot,co_pilot,attendant)
            passport = input("Ingrese el passport: ")
            forename = input("Ingrese el forename: ")
            surname = input("Ingrese el surname: ")
            date_of_birth = input("Ingrese el date of birth: ")
            country = input("Ingrese el country: ")
            gender = input("Ingrese el gender: ")
            marital_status = input("Ingrese el marital status: ")
            y = my_airport.modify_traveller(passport,forename,surname,date_of_birth,country,
                                            gender,marital_status)
            flight = input("Ingrese el flight: ")
            passport = input("Ingrese el passport: ")
            clas = input("Ingrese el clas: ")
            seat = input("Ingrese el seat: ")
            location = input("Ingrese el location: ")
            z = my_airport.modify_passenger(fligth,passport,clas,seat,location)
        elif i == 3:
            passport = input("Ingrese passport: ")
            forename = input("Ingrese forename: ")
            surname = input("Ingrese surname: ")
            date_of_birth = input("Ingrese date of birth: ")
            country = input("Ingrese date of country: ")
            gender = input("Ingrese date of gender: ")
            marital_status = input("Ingrese date of marital status: ")
            a = my_airport.modify_pilot(passport, forename, surname, date_of_birth, 
                     country, gender, marital_status)
            passport = input("Ingrese passport: ")
            forename = input("Ingrese forename: ")
            surname = input("Ingrese surname: ")
            date_of_birth = input("Ingrese date of birth: ")
            country = input("Ingrese date of country: ")
            gender = input("Ingrese date of gender: ")
            marital_status = input("Ingrese date of marital status: ")
            b = my_airport.modify_attendants(passport, forename, surname, date_of_birth, 
                     country, gender, marital_status)
            passport = input("Ingrese el passport: ")
            forename = input("Ingrese el forename: ")
            surname = input("Ingrese el surname: ")
            date_of_birth = input("Ingrese el date of birth: ")
            country = input("Ingrese el country: ")
            gender = input("Ingrese el gender: ")
            marital_status = input("Ingrese el marital status: ")
            c = my_airport.modify_travellers(passport,forename,surname,date_of_birth,country,
                                            gender,marital_status)
            flight = input("Ingrese el flight: ")
            passport = input("Ingrese el passport: ")
            clas = input("Ingrese el clas: ")
            seat = input("Ingrese el seat: ")
            location = input("Ingrese el location: ")
            d = my_airport.modify_passengers(fligth,passport,clas,seat,location)
            id = input("Ingrese el id: ")
            pate = input("Ingrese el pate: ")
            origin = input("Ingrese el origin: ")
            destiny = input("Ingrese el destiny: ")
            departure = input("Ingrese el departure: ")
            arriving = input("Ingrese el arriving: ")
            status = input("Ingrese el status: ")
            departure_gate = input("Ingrese el departure gate: ")
            take_off_track = input("Ingrese el take of track: ")
            arriving_gate = input("Ingrese el arriving gate: ")
            landing_track = input("Ingrese el landing track: ")
            pilot = input("Ingrese el pilot: ")
            co_pilot = input("Ingrese el copilot: ")
            attendant = input("Ingrese el attendant")
            e = my_airport.modify_flights(id,pate,origin,destiny,departure,
                                         arriving,status,departure_gate,take_off_track
                                         ,arriving_gate,landing_track,pilot,co_pilot,attendant)
        elif i == 4:
            break