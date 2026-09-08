num = 123456789
texte = str(num)

total = 0
for caractere in texte:
    chiffre = int(caractere)
    total += chiffre

print (total)

num = 112233445566778899
texte = str(num)

total = 0
for caractere in texte:
    chiffre = int(caractere)
    total += chiffre

print (total)

num = 123456789 * 987654321
texte = str(num)

total = 0
for caractere in texte:
    chiffre = int(caractere)
    total += chiffre

print (total)



def somme_chiffres(num):
    total = 0
    for caractere in str(num):
        chiffre = int(caractere)
        total += chiffre
    return total

print(somme_chiffres(123456789))
print(somme_chiffres(112233445566778899))
print(somme_chiffres(123456789 * 987654321))