class City:
    # Class variable containing the possible type elements
    cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', \
              'napoli', 'palermo', 'roma', 'torino', 'venezia']

    def __init__(self, city):
        city = city.strip().lower()
        self.city_type = None
        if City.check_cities(city):
            self.city_type = city
        else:
            return None

    # The following function returns a boolean parameter when it has been entered correctly
    @staticmethod
    def check_cities(city):
        city = city.strip().lower()
        if city in City.cities:
            return True
        else:
            print('Incorrect Value')
            return False

    def __str__(self):
        return self.city_type
    

# test
if __name__ == "__main__":
    city = City("VeneZiA  ")
    print(city)