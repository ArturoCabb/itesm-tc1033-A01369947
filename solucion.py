# -*- coding: utf-8 -*-
#Con base en estos datos deberás calcular por cada mes del año anterior 
#cuáles son los países que tengan 20% o más de los vuelos. 
import csv

dic_data = {}

with open("datos_vuelos.csv") as csv_file:
    csv_reader = csv_file.readlines()
    for row in csv_reader:
        string = row.split(",")
        country = string[0][:5]
        departure = string[1][3:5]
        print(country)
        print(departure)