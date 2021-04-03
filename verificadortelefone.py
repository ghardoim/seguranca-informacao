import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o número no formato +551100000000: ")
phone_number = (phonenumbers.parse(phone))

print(geocoder.description_for_number(phone_number, "pt"))