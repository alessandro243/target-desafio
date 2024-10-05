strin = 'Alessandro'
lista_ = []

for x in strin:
    lista_.append(x)

rang = len(lista_)
new_string = ''

while rang > 0:
    new_string += lista_[rang-1]
    rang -= 1

print(new_string)