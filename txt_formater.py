""" Keep only capitalized letters in txt file """


if __name__ == '__main__':
    with open('king-the_stand.txt', 'r') as file:
        text = file.read()
    
    text = text.upper()

    allowed = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    text = ''.join(filter(lambda char: char in allowed, text))

    with open('the_stand-formated.txt', 'w') as file:
        file.write(text)
    