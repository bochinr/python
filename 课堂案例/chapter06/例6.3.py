s = 'oh,python is my love'
t = ('l', 'i', 'k', 'e')
lst = [1, 2, 3, 2, 1]
b = b'Hi,Python!'

print('p' in s, end=' ')
print('P' not in s, end=' ')
print(s.count('o'), end=' ')
print(s.index('o', 8))

if 'i' in t:
    print(t.count('i'), end=' ')
print(t.index('i'))

for i in range(len(lst)):
    if lst[i] == 2:
        print(lst.index(i), ":yes", end=' ')
print('')

print(b'O' in b)
print(b.index(b't'))
