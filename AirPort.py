from editFile import *
class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        hour = str(input())

    def Track(self):
        pasajero = ReadPassenger()
        a, pasajero1 = pasajero.read()
        for x in a:
            z = a[x]
            if str(z[4]) == "security":
                print(z)
