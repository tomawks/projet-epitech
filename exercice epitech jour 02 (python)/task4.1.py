n = 10000000
total = 0
signe = 1

for i in range(1, n, 2):
    total += signe / i
    signe = -signe

pi = 4 * total
print(round(pi, 6))