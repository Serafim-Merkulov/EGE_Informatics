"""
Текстовый файл состоит из заглавных букв латинского алфавита A, B, C, D, E и F.
Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых пара символов BC (в указанном порядке) встречается ровно 190 раз.
"""

import re
#txt = "CBBDFBBBCDCBCFCCBBCBBABBBAFFCBDCFCEABCBDAFCBCABFCCDACBCBCDCBFCBBFFCBDCBABECDDBECCFAACBBDBBACBACBCCBCACCCACBC"
f = open("24_29354.txt")
txt = f.read().strip()
N = 191
ls = []
for r in txt.split('BC'):
    ls.append(len(r))
#print(ls)
best = 0

for i in range (len(ls)-191):
    s = sum(ls[i: i + N])
    best = max(best, s)

print (best + N * 2)












