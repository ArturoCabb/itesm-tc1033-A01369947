# -*- coding: utf-8 -*-
import csv

dic_data = {"Matrícula":{}, "Salida":{}, "Llegada":{}, "No. Pasajeros":{}}

with open("datos_vuelos.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dic_data = row
        print(row)