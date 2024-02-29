import sys

# Чтение содержимого текстового файла
with open("text.txt", "r") as f:
    text = f.read()

# Извлечение имени и даты рождения
firstName = text[0]
birthDate = ""
for char in text:
    if char.isdigit():
        birthDate += char

# Расчет суммы года рождения
birthYear = int(birthDate)
birthYearSum = 0
for i in range(4, len(birthDate)):
    birthYearSum += birthYear % 10
    birthYear //= 10

# Расчет номера символа
symbolNumber = ord(firstName) - 64

# Расчет конечного шестнадцатеричного кода
finalCode = birthYearSum * 64 + symbolNumber * 256
hexCode = ""
while finalCode != 0:
    digit = finalCode % 16
    hexCode += chr(digit + ord('0')) if digit <= 9 else chr(digit + ord('A') - 10)
    finalCode //= 16

# Удаление ведущих нулей при необходимости
if len(hexCode) > 3:
    hexCode = hexCode[1:]
elif len(hexCode) == 3:
    hexCode = "0" + hexCode

# Вывод шестнадцатеричного кода
print(hexCode)
