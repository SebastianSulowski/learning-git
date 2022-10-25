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






