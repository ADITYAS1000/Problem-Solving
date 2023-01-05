input = "secret"

# T : O(N) | S : O(N)
def Caeser_Cypher_Encryptor(input, key):
    output = ''
    key = key % 26
    for index in range(len(input)):
        ordinal = ord(input[index])
        new_value = ordinal if ordinal <=122 else (ordinal % 122) + 96
        output += chr(new_value + key)
    return output

print(Caeser_Cypher_Encryptor(input, 5))