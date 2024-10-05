import json

def max_searcher(x):
    print(max(x))

def min_searcher(x):
    new_list = []
    for n in x:
        if n == 0:
            continue
        new_list.append(n)
    print(min(new_list))

def med_searcher(x):
    vari = 0
    indice = 0
    for y in x:
        if y == 0:
            continue
        vari += y
        indice += 1
    
    print(round(vari / indice, 2))
    


with open('arq.json', 'r') as file:
    dados = json.load(file)
    med_searcher(dados)
    max_searcher(dados)
    min_searcher(dados)