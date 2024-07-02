import random

from faker import Faker
fake = Faker()
def random_first_name():
    randomFirstName = fake.first_name()
    return randomFirstName

def random_last_name():
    randomLastName = fake.last_name()
    return randomLastName

def random_zip_code():
    zip = str(random.randint(11111,99999))
    return zip

def random_city():
    random_city = fake.city()
    return random_city

def random_state():
    random_state = fake.state()
    return random_state

def random_address():
    random_address = fake.street_address()
    return random_address

def random_phone_number():
    unq_phone_number = str(random.randint(1111111111,9999999999))
    return unq_phone_number

def random_country():
    country = fake.country()
    return country


