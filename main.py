print("lista zakupów")
lista_zakupow = {
    "piekarnia": ["chleb", "pączek", "bułka"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
counter = 0
for shop,products in lista_zakupow.items():
print()
    counter += len(lista_zakupow.get(shop))
    print(f"Idę do: {shop.capitalize()} i kupuję tam: {products}")
print(f"kupię {counter} produkty".capitalize())
print()

print()
numbers = []
for numb in range(1,101):
    numbers.append(numb)
numbers_5 = [numb for numb in numbers if numb % 5  == 0]
numbers_3 = [numb*numb*numb for numb in numbers if numb % 5  == 0]
print(f"liczb od 1 do 100, które są podzielne przez 5: {numbers_5}")
print(f"Licby od 1 do 100, które są podzielne przez 5 po podniesienieu do sześcianu: {numbers_3}")
print()






