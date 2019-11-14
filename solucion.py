# -*- coding: utf-8 -*-
import csv

dic_data = []
suma = 0

with open("datos_vuelos.csv") as csv_file:
    csv_reader = csv_file.readlines()
    for row in csv_reader:
        dic_data = row
        print(dic_data)