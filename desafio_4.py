SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

total = SP + RJ + MG + ES + outros
SP_per = f'{round((SP * 100) / total, 2)}%'
RJ_per = f'{round((RJ * 100) / total, 2)}%'
MG_per = f'{round((MG * 100) / total, 2)}%'
ES_per = f'{round((ES * 100) / total, 2)}%'
outros_per = f'{round((outros * 100) / total, 2)}%'

print(SP_per)
print(RJ_per)
print(MG_per)
print(ES_per)
print(outros_per)