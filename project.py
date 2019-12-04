if __name__ == "__main__":
    airport = UserInput()
    date, time = airport.datos()
    my_airport = Airport()
    my_airport.populated_airport()
    my_airport.generate_statistics(date, time)