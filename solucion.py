# -*- coding: utf-8 -*-
#Con base en estos datos deberás calcular por cada mes del año anterior 
#cuáles son los países que tengan 20% o más de los vuelos. 
import csv

dic_data = {}
dic_2 = {}

with open("datos_vuelos.csv") as csv_file:
    csv_reader = csv_file.readlines()
    for row in csv_reader:
        string = row.split(",")
        country = string[0][:5]
        departure = string[1][3:5]

        if departure not in dic_data:
            dic_data[departure] = 1
        else:
            dic_data[departure] += 1
        if departure not in dic_2:
            dic_2[departure] = {}
        elif country not in dic_2[departure]:
            dic_2[departure][country] = 1
        else:
            dic_2[departure][country] += 1

average = {}
file = open("resultados.csv","w+")
file.write("Mes,Pais,Porcentaje\n")
for month in dic_data:
    for country in dic_2[month]:
        average = dic_2[month][country]/dic_data[month]
        average = average * 100
        if average >= 20:
            average = str(average)
            file.write(month + "," + country + "," + average + "\n")
file.close()