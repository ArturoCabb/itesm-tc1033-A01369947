from AirPort import *
# -*- coding: utf-8 -*-
#Arturo Caballero Ortega
#Erik Patricio Trujillo Barrientos

if __name__ == "__main__":
    airport = UserInput()
    date, time = airport.datos()
    my_airport = Airport()
    my_airport.populated_airport()
    my_airport.generate_statistics(date, time)
    my_airport.modify_flight("a","b","a","b","a","b","a","b","a","b","a","b","a","b")
    print(i)