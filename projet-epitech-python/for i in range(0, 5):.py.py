n = 10000000
total = 0
signe = 1

for i in range(1, n, 2):
    total += signe / i
    signe = -signe   # inverse le signe pour le prochain tour

pi = 4 * total
print(pi)