def my_sum(a, b, *c, **d):
    total = a + b
    for n in c:
        total = total + n
    for key in d:
        total = total + d[key]
    return total

print(my_sum(1, 2))
print(my_sum(1, 2, 3, 4, 5))
print(my_sum(1, 2, 3, 4, 5, num1=6, num2=7))