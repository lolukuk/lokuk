with open('input.txt', 'r') as f:
    data = f.read()

    list_of_letters = []
    for letter in data:
        list_of_letters.append(letter)

    print(list_of_letters)