print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

import logging
logging.basicConfig(format = '%(message)s', level=logging.INFO)

answer = input("Wpisz numer: ")
if answer == "1":

    number1 = int(input("Podaj składnik 1. "))
    number2 = int(input("Podaj składnik 2. "))
    print(f"Wynik to: %s" %(number1+number2))
    logging.info("Dodawanie %s i %s" % (number1, number2))

elif answer == "2":
    number1 = int(input("Podaj składnik 1. "))
    number2 = int(input("Podaj składnik 2. "))
    print(f"Wynik to: %s" %(number1-number2))
    logging.info("Odejmowanie %s i %s" % (number1, number2))
elif answer == "3":
    number1 = int(input("Podaj składnik 1. "))
    number2 = int(input("Podaj składnik 2. "))
    print(f"Wynik to: %s" %(number1*number2))
    logging.info("Mnożenie %s i %s" % (number1, number2))
elif answer == "4":
    number1 = int(input("Podaj składnik 1. "))
    number2 = int(input("Podaj składnik 2. "))
    print(f"Wynik to: %s" %(number1/number2))
    logging.info("Dzielenie %s i %s" % (number1, number2))