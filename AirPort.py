import editFile

class UserInput:
    def datos(self):
        print("Ingrese una fecha en formato AAMMDD")
        date = str(input())
        print("Ingrese la hora en formato HHMM")
        hour = str(input())
        
        a = editFile.ReadFlight()
        a, b = a.read()

        for i in a:
            l = a[i]
            c = l[5][:6]
            d = l[5][7:10]
            if c == date and d == hour:
                print(c)
