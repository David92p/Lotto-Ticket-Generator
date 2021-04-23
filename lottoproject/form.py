class Form:
     # Class variable containing the possible type elements:
    forms = ["ambata", "ambo", "terno", "quaterna", "cinquina"]

    def __init__(self, form=""):
        self.bet_form = Form.check_form()

    # The following function returns a form parameter when it has been entered correctly
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
            if form in Form.forms:
                return form
                break
            else:
                print("Form not Valid")
                continue

    def __str__(self):
        return self.bet_form

# test
if __name__ == "__main__":
    form = Form()
    print(form)