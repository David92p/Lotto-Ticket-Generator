class BasicGame:
    # Class variable containing the possible type elements
    cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', \
              'napoli', 'palermo', 'roma', 'torino', 'venezia', "tutte"]

    # Class variable containing the possible type elements:
    forms = ["ambata", "ambo", "terno", "quaterna", "cinquina"]

    #The class takes care of instantiating the city and form parameters when they are entered correctly.
    def __init__(self, city="", form=""):
        city = city.strip().lower()
        form = form.strip().lower()
        self.bet_city = BasicGame.check_cities()
        self.bet_form = BasicGame.check_form()

    #The following function returns a city parameter when it has been entered correctly
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
            if city in BasicGame.cities:
                return city
                break
            else:
                print("City not Valid")
                continue

    #The following function returns a form parameter when it has been entered correctly
    @staticmethod
    def check_form():
        print("""
            Choose the type of bet to be made:
            - Ambata
            - Ambo 
            - Terno 
            - Quaterna 
            - Cinquina 
            """)
        while True:
            form = input("Enter the type for your bet: ")
            form = form.strip().lower()
            if form in BasicGame.forms:
                return form
                break
            else:
                print("Form not Valid")
                continue

    def __str__(self):
        return f"{self.bet_city}, {self.bet_form}"


# test
if __name__ == "__main__":
    ticket = BasicGame()
    print(ticket)