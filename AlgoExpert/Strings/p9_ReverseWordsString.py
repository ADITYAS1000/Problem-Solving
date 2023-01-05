# def ReverseWordsString(string):
#     startOfWord = 0
#     words = []
#     for index in range(len(string)):
#         character = string[index]

#         if character == " ":
#             words.append(string[startOfWord:index])
#             startOfWord = index
#         elif string[startOfWord] == " ":
#             words.append(" ")
#             startOfWord = index
    
#     words.append(string[startOfWord:])

#     reversedWords(words)

#     return "".join(words)

# def reversedWords(words):
#     start, end = 0, len(words) - 1

#     while start < end:
#         words[start], words[end] = words[end], words[start]
#         start += 1
#         end -= 1

# print(ReverseWordsString("AlggoExpet is the best!"))

def ReverseWordsString(string):
    startOfWord, endOfWord = 0, 0
    characters = [char for char in string]
    while True:
        endOfWord = startOfWord

        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1
        
        if endOfWord == len(characters):
            reversedWords(characters, 0, endOfWord - 1)
            break;
        
        reversedWords(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1

    return "".join(characters)

def reversedWords(words, start, end):
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1

print(ReverseWordsString("AlgoExpert is the best!"))