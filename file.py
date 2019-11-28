class Attendant():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)

        def open(self):
            attendants = open("attendants.csv","r").readlines()
            attendants.pop(0)
            return attendants

        def process_data(self):
            pass

class Flight():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)
        def open(self):
            flights = open("flights.csv","r").readlines()
            flights.pop(0)
            return flights

class Passenger():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)
        def open(self):
            passenger = open("passengers.csv","r").readlines()
            passenger.pop(0)
            return passenger

class Pilot():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)
        def open(self):
            pilots = open("pilots.csv","r").readlines()
            pilots.pop(0)
            return pilots

class Plane():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)
        def open(self):
            planes = open("planes.csv","r").readlines()
            planes.pop(0)
            return planes

class Traveler():
        def __init__(self, *args, **kwargs):
            return super().__init__(*args, **kwargs)
        def open(self):
            travelers = open("travelers.csv","r").readlines()
            travelers.pop(0)
            return travelers




