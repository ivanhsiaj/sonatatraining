class singleaddress:
    def __init__(self,lastname,firstname,streetaddress,city,state,country,postalcode):
        self.lname=lastname
        self.fname=firstname
        self.stadd=streetaddress
        self.city=city
        self.state=state
        self.country=country
        self.postal=postalcode
    def get_details(self):
        return self.lname + + self.fname + + self.stadd + + self.city + + self.state + + self.country + + self.postal
    def set_detalis(self,x):
        self.lname=x


