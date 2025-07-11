#takes a secert word as input (without space)

s=input("Enter a secert word: ")

#Then encodes the word using a custom cipher:

def is_encode(s):
    encoded=""
    for char in s:
        if char.isalpha():
            encoded+=chr(ord(char)+3)
        else:
            encoded+=char
    return encoded
print(is_encode("Hello"))

#replace all with vowels with *

def replace_vowels(s):
    vowels="AEIOUaeiou"
    for vowels in s:
        if vowels in vowels:
            s=s.replace(vowels,"*")
    return s
print(replace_vowels("Satyam"))


#reverse the entire string

#then shift each letter 2 place ahead in the aplhabet (wrap around if needed, eg., y-a, z-b)

# finally, print the resulting econded word



