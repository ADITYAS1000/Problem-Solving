input = '9A4A2B4C2D'

def RunLengthEncoding(input):

    if input == '':
        return ''

    number_counter = 0
    character_counter = number_counter + 1
    output = ''
    while(number_counter < len(input)):
        output += input[character_counter] * int(input[number_counter])
        number_counter += 2
        character_counter += 2
    return output

print(RunLengthEncoding(input))