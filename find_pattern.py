
def pattern_sum(dictionary) -> int:
    suma = 0
    for key in list(dictionary.keys()):
        suma += dictionary[key]
    return suma



if __name__ == '__main__':
    searched_text = "HCNOAUMBTMESOITAMBHTBEEBUBSTNYNXWWNGEXHOFMNXFOEVPEODNDNEIMOACNDHDOUESUUSYMATHDOEXETIYEXEFTADXRWSEAGLTDEINAANLAOTECNTATMPECSDEAEURXLUNOVXMHHNGXONSRIOUHITOTSDDBLNHAOTBLOIWCAIXANVDSXLNGUEXAIENOXMAIMDTMAAHNIAEHUETALMHABONIONNXDEEILXTEORAXNSSETX"

    x_count = 0
    for char in searched_text:
        if char == 'X':
            x_count += 1

    possible_letters = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'

    searched_no_x = searched_text.replace('X', '')
    searched_pattern = {}
    for char in searched_no_x:
        if char not in list(searched_pattern.keys()):
            searched_pattern[char] = 1
        else:
            searched_pattern[char] += 1
    
    # find chars that does not appear in the searched pattern
    not_used = ''
    for char in possible_letters:
        if char not in list(searched_pattern.keys()):
            not_used += char
    print(f"Not used chars: {not_used}")

    # load book text
    with open('the_stand-formated.txt', 'r') as file:
        text = file.read()

    # remove not used chars from book text
    for char in not_used:
        text = text.replace(char, '')

    print(f"Text length is {len(text)}")

    pattern_len = len(searched_no_x)


    current_pattern = {}
    for key in list(searched_pattern.keys()):
        current_pattern[key] = 0

    for i in range(len(text)):
        char_i = text[i]

        # add new char to current pattern
        current_pattern[char_i] += 1

        # remove char from current pattern
        if i-pattern_len >= 0:
            char_old = text[i-pattern_len]
            current_pattern[char_old] -= 1

        # check if current_pattern is the same as searched pattern
        if current_pattern == searched_pattern:
            start = i-pattern_len + 1
            end = i+1
            print(text[start:end] + x_count*'X')
