n = 1000
resultat = 0


for i in reversed(range(1, n, 2)):
    carre = i ** 2
    resultat = carre / (6 + resultat)

pi = resultat + 3
print(round(pi, 6))