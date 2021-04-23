class City:
    # Class variable containing the possible type elements
    cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', \
              'napoli', 'palermo', 'roma', 'torino', 'venezia', "tutte"]

    def __init__(self, city=""):
        self.bet_city = City.check_cities()

    # The following function returns a form parameter when it has been entered correctly
    @staticmethod
    def check_cities():
        print("""
            List of the citys:
            - Bari 
            - Cagliari 
            - Firenze 
            - Genova 
            - Milano 
            - Napoli 
            - Palermo 
            - Roma 
            - Torino 
            - Venezia 
            - Tutte 
            """)
        while True:
            city = input("Enter the city for your bet: ")
            city = city.strip().lower()
            if city in City.cities:
                return city
                break
            else:
                print("City not Valid")
                continue
    
    def __str__(self):
        return self.bet_city

# test
if __name__ == "__main__":
    city = City()
    print(city)