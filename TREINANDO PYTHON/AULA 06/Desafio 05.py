algo = input("Digite algo: ")
print(type(algo))
print(f"Ele é Númerico?",algo.isnumeric())
print(f"Ele é alfabético?",algo.isalpha())
print(f"Ele é AlfaNúmerico?",algo.isalnum())
print(f"Ele está em maiúsculo?",algo.isupper())