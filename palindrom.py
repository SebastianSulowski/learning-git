word = "potop"
def palindrom(word):
    if word==word[::-1]:
        print(True)
    else:
        print("none")
palindrom("kura")
palindrom("potop")
