def sumNums(a, b, *c):
    total = a + b
    for j in c:
        total = total + j
    return total

print(sumNums(1, 2))
print(sumNums(1, 2, 3, 4, 5))
print(sumNums(1, 2, 3, 4, 5, 6, 7))