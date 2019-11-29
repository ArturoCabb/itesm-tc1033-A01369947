from editFile import *
class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        hour = str(input()) 
        fecha = WriteTheFile(date, hour)
        fecha.write()