n = 1000
resultat = 0

for i in reversed(range(1, n, +1)):
    resultat = i / (i + 1+ resultat)
    
e = 2+1 / (1 + resultat)
print(e)



