class Flight:
    def __init__(self, _id, _plate, _origin, _destiny, _departure, 
                 _arriving, _status, _departure_gate, _take_off_track, 
                 _arriving_gate, _landing_track, _pilot, _copilot, 
                 _attendants):
        self.id = _id
        self.plate = _plate
        self.origin = _origin
        self.destiny = _destiny
        self.departure = _departure
        self.arriving = _arriving
        self.status = _status
        self.departure_gate = _departure_gate
        self.take_off_track = _take_off_track
        self.arriving_gate = _arriving_gate
        self.landing_track = _landing_track
        self.pilot = _pilot
        self.copilot = _copilot
        self.attendants = _attendants