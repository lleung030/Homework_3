# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’


# def rv(string_):
#     vowels= 'aeiou'
#     for v in vowels:
#         string_=string_.replace(v,'')
#     return string_
# print(rv('Dylan and Lucas are great teachers but i am not a suckup'))


def noVowels(str):
    vowels = ["a", "e", "i", "o", "u"]
    newName = [let for let in str if let not in vowels]
    return ''.join(newName)

print(noVowels("Joel"))