from faker import Faker
import random

fake = Faker()

class BaseContact:
    def __init__(self, imie, nazwisko, adres_email, telefon):
       self.imie = imie
       self.nazwisko = nazwisko
       self.adres_email = adres_email
       self.telefon  = telefon
    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.telefon}, {self.adres_email}"
    def contact(self):
        return f"Wybieram numer: {self.telefon} i dzwonie do {self.imie} {self.nazwisko}"
    @property
    def label_length (self):
        return len(self.imie), len(self.nazwisko)


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, telefon_służbowy,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko  = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon_służbowy = telefon_służbowy
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info} {self.stanowisko}, {self.nazwa_firmy}, {self.telefon_służbowy}"
    def contact(self):
        return f"Wybieram numer: {self.telefon_służbowy} i dzwonie do {self.imie} {self.nazwisko}"
    @property
    def label_length (self):
        return len(self.imie), len(self.nazwisko)
    
def create_contacts(contact_type, number):
    contacts= []

    for _ in range(number):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        adres_email = fake.email()
        telefon = fake.phone_number()

        if contact_type == "base":
            contacts.append(BaseContact(imie, nazwisko, adres_email, telefon))
        elif contact_type == "business":
            stanowisko = fake.job()
            nazwa_firmy = fake.company()
            telefon_służbowy = fake.phone_number()
            contacts.append(BusinessContact(stanowisko, nazwa_firmy, telefon_służbowy, imie=imie, nazwisko=nazwisko, adres_email=adres_email, telefon=telefon))
        else:
            raise ValueError("Zły typ danych, podaj 'base' lub 'business'.")
    
    return contacts


base_contacts = [
BaseContact(imie="Taylor", nazwisko="Cooley",telefon="732-374-2808", adres_email="TaylorDCooley@jourrapide.com"),
BaseContact(imie="Ray", nazwisko="Stein",telefon="765-324-1303", adres_email="RayBStein@armyspy.com"),
BaseContact(imie="Frank", nazwisko="Fitts",telefon="711-320-6003", adres_email="FrankHFitts@teleworm.us"),
BaseContact(imie="Javier", nazwisko="Jordan",telefon="455-124-9903", adres_email="JavierAJordan@dayrep.com"),
BaseContact(imie="Susan", nazwisko="Harrell",telefon="345-221-7634", adres_email="SusanTHarrell@armyspy.com"),
]


business_contacts = [
BusinessContact(imie="Taylor", nazwisko="Cooley",telefon="732-374-2808", adres_email="TaylorDCooley@jourrapide.com", telefon_służbowy="703-322-1312", nazwa_firmy="Pink Pig Tavern", stanowisko="Diesel Train engineer"),
BusinessContact(imie="Ray", nazwisko="Stein",telefon="765-324-1303", adres_email="RayBStein@armyspy.com", telefon_służbowy="421-421-4244", nazwa_firmy="John M. Smyth's Homemakers", stanowisko="Government auditor"),
BusinessContact(imie="Frank", nazwisko="Fitts",telefon="711-320-6003", adres_email="FrankHFitts@teleworm.us", telefon_służbowy="424-424-4444", nazwa_firmy="Monlinks", stanowisko="Licensed vocational nurse"),
BusinessContact(imie="Javier", nazwisko="Jordan",telefon="455-124-9903", adres_email="JavierAJordan@dayrep.com", telefon_służbowy="441-569-8852", nazwa_firmy="Liberal", stanowisko="Boatswain"),
BusinessContact(imie="Susan", nazwisko="Harrell",telefon="345-221-7634", adres_email="SusanTHarrell@armyspy.com", telefon_służbowy="468-225-4358", nazwa_firmy="Road Runner Lawn Services", stanowisko="Wellhead pumper"),
]


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
countdown(3)

print("\nBase Contacts:")
for i, contact in enumerate(base_contacts, start=1):
    print(f"{i}. {contact}")

print("\nBusiness Contacts:")
for i, contact in enumerate(business_contacts, start=1):
    print(f"{i}. {contact}")

print("\n")

for contact in base_contacts:
    print(contact.contact())

print("\n")

for contact in business_contacts:
    print(contact.contact())

print("\n")

for lenght in base_contacts:
    print(lenght.label_length)

print("\n")

for lenght in business_contacts:
    print(lenght.label_length)

print("\n")

random_contacts = create_contacts("business", 5)

for contact in random_contacts:
    print(contact)
    print(contact.contact())
    print(f"Label length: {contact.label_length}\n")
