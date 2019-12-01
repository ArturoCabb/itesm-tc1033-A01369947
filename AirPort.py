import editFile

class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        hour = str(input())
        
        flight = editFile.ReadFlight()
        itemA, itemB = flight.read()

        passenger = editFile.ReadPassenger()
        itemC, itemD = passenger.read()
        
        for x in itemA:
            l = itemA[i]
            a = l[5][:6]
            b = l[5][7:10]
            if a == date and b == hour:
                for xx in itemC:
                    l = itemC[0]
                    print(l)