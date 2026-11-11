"""
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита.
Определите в прилагаемом файле минимальное количество идущих подряд символов,
среди которых пара символов «20» (в указанном порядке) встречается ровно 26 раз,
гласная буква встречается ровно один раз,
искомая последовательность заканчивается этой единственной гласной буквой.
В ответе запишите число - количество символов в найденной последовательности.
Для выполнения этого задания следует написать программу.
Примечание. гласные буквы латинского алфавита: A, E, I, O, U, Y.
"""

import re, sys

if 1:
    f = open("24_28943.txt")
    txt = f.read()
else:
    txt = "PAEZ8AX4DOEGPQM6QFUPUG2ACTD2OHOFCBURD4ODOFZCZ220IS2QRDPRDGFNR2IUXOFAFIBDXL20L2VEO8OAHKLTT420NIEVR420H1NH3HSAIX4I6U8IVM8QCITUI20BVLJXOAUJ20KO20"

N = 26

best = len(txt) + 1

for part in re.split(r"[AEIOUY]", txt)[:-1]:
    positions = [m.start() for m in re.finditer("20", part)]

    if len(positions) >= N:
        length = len(part) - positions[-N] + 1
        if length < best:
            best = length
            print (best)

print(best if best <= len(txt) else "Подходящей последовательности нет")

sys.exit()


# Позиции начала каждой пары «20».
lefts = [m.start() for m in re.finditer("20", txt)]

# -1 обозначает границу перед началом текста:
# благодаря ей обрабатывается и самая первая гласная.
rights = [-1] + [m.start() for m in re.finditer("[AEIOUY]", txt)]

i_left = 0
i_right = 1
best = len(txt) + 1

while i_left + N <= len(lefts) and i_right < len(rights):
    start = lefts[i_left]
    end = rights[i_right]
    previous_vowel = rights[i_right - 1]

    if start <= previous_vowel:
        # Внутрь попадает предыдущая гласная — сдвигаем начало.
        i_left += 1

    elif lefts[i_left + N - 1] > end:
        # До этой гласной ещё не набралось 26 пар — берём следующую.
        i_right += 1

    else:
        # Первые 26 пар уже перед гласной.
        # Проверяем, что следующей пары до неё нет.
        if i_left + N == len(lefts) or end < lefts[i_left + N]:
            best = min(best, end - start + 1)

        i_left += 1

if best <= len(txt):
    print(best)
else:
    print("Подходящей последовательности нет")

sys.exit()

best = 'a' * 1000

txts = re.sub(r"[AEIOUY]", " ", txt).split()

for txt in txts:

    n = re.findall(r"20{1}?", txt)
    if len(n) < N:
        continue

    matches = [match.span()[0] for match in re.finditer("20", txt)]
    left = matches[-26]

    found = txt[left:]

    if len(best) > len(found):
        best = found[:]
        print(len(best), best)



sys.exit()



letters = ['A', 'E', 'I', 'O', 'U', 'Y']

left = right = 0

best = 'a' * 1024

while left <= right < len(txt) - N * 2:
    if txt[right] not in letters:
        right += 1
        continue

    n = re.findall(r"20{1}?", txt[left: right])

    if len(n) < N:
        right += 1
        continue

    if re.search(r"[AEIOUY]+", txt[left: right]):
        left += 1
        continue

    found = txt[left: right + 1]
    if len(found) < len(best):
        best = found
        print(len (best), left, right, found)
    left += 1

print (len(best), best)

