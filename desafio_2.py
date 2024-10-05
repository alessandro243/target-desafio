def fun(x):
    try:
        o = int(x)
        return o
    except:
        print('digite um número')
        return -1

i = [0,1]
p = 0
x = input('qual número?')

while p < fun(x):

    i.append(i[p] + i[p+1])
    p+=1

if fun(x) in i:
    print('Está na sequência')

else:
    print('Não está na sequência')