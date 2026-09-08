print(1 + 1)
print(30 + 12)
print(777 + (-735))
print(1 + 2 + 3 + 5 + 7 + 11 + 13)

print(84 < 42)
print(0 == -( -(0) ))
print(666 != 42)
print(2 ** 21)
print(pow(10, 3))
print(9 % 2)

total = 0
terme = "1"
for i in range(1, 10): 
    total += int(terme)
    terme += "1"

print(total)
print(total ** 2)
print (total ** 3)
print(total ** 4)
print (total ** 5)

total = 0
terme = "1"
for i in range(1, 11): 
    total += int(terme)
    terme += "1"

print(total)
print(total ** 2)
print (total ** 3)
print(total ** 4)
print (total ** 5)

total = 0
terme = "1"
for i in range(1, 12): 
    total += int(terme)
    terme += "1"

print(total)
print(total ** 2)
print (total ** 3)
print(total ** 4)
print (total ** 5)


for n in (9, 10, 11):
    total = sum(int('1' * i) for i in range(1, n + 1))
    print(f"Série jusqu'à {n} chiffres : {total}")
    for p in range(2, 6):
        print(f"  ^{p} = {total ** p}")