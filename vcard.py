from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, tel_priv, email):
        self.name= name
        self.surname= name
        self.tel_priv= tel_priv
        self.email = email
    def conntact(self):
        return f"Wybieram numer: {self.tel_priv} i dzwonię do: {self.name} {self.surname}"

    def label_length(self):
        return ([len.(self.name), len(self.surname)])


class BusinessContact(BaseContact):
    def __init__(self, bussines, occupation, tel_office, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bussines = bussines
        self.occupation = occupation
        self.tel_office = tel_office
    def conntact(self):
        return f"Wybeiram numer tel: {self.tel_office} i dzwonię do {self.name} {self.surname}"
    def label_length(self):
        return ([len.(self.name), len.(self.surname)])

