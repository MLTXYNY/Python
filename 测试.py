n = 0
for x in range(1, 1000, 1):
    if x % 5 == 2 and x % 7 == 3 and x % 3 == 1:
        n = x
print(n)