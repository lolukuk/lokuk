def upper(text):
  return text.upper()
def pop():
    spisok.pop(2)
    spisok.pop(1)
    spisok.pop(0)
with open('input.txt', 'r', encoding='utf-8-sig') as f:
    spisok = f.read().replace('\n', ',').split(',')
    first = range(0, int(spisok[0]))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    spisok.pop(0)
    result = []
    for i in first:
        for word in spisok:
            if word == spisok[2]:
                break
            if word.isnumeric():
                if int(spisok[0]) % 10 != 0:
                    summa = int(spisok[0]) % 10 + int(spisok[0]) // 10 + int(spisok[1])
                    pop()
                    pep = lens + summa * 64 + position * 256
                    if (int(pep) < 3600):
                        pep = upper(hex(pep))
                        result.append(pep[2:])
                    else:
                        pep = upper(hex(pep))
                        result.append(pep[3:])
            else:
                lens = set(spisok[0] + spisok[1] + spisok[2])
                lens = int(len(lens))
                for letter in set(spisok[0]):
                    if letter.isupper():
                        position = alphabet.find(letter.lower())
                position = (position+1)
                pop()
result = " ".join(result)
print(result)