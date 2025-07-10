# Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]

s="PythonPractice"
print(s[1])
print(s[-3:])
print(s[2:7])


# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.

d="developer"
print(d[::-1])

# Count Vowels
#    Write a function that counts the number of vowels in a given string.

def count_vowels(s):
    vowels="AEIOUaeiou"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("PythonPractice Hw is very effective"))
print(count_vowels("I have done all python practice hw and i am very happy"))


# Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
def is_palindrome(s):
    s=s.replace(" ","")
    s=s.lower()
    return s==s[::-1]
      
print(is_palindrome("satyam Is a good boy"))
print(is_palindrome("Racecar"))

# Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"

text=" Hello world! welcome to python.  "
text=text.strip()
text=text.capitalize()
text=text.replace("python","programming")
print(text)


# Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
def longest_word(s):
    word=s.split()
    longest=" "
    for word in word:
        if len(word)>len(longest):
            longest=word
    return longest
print(longest_word("hello python is fun language to learn"))

# String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

s1="py"
s2="thon"
print(s1+s2)
print(s1*3)
print("y"in s1)
           

# Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicates(s):
    result=""
    for char in s:
        if char not in result:
            result+=char
    return result
print(remove_duplicates("hello world"))


# Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.

def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)
print(is_anagram("Care","Race"))
print(is_anagram("Satyam","Sapkota"))


# Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.

def word_frequency(s):
    words=s.split()
    frequency={}
    for word in words:
        frequency[word]=frequency.get(word,0)+1
    return frequency
print(word_frequency("hello world I am learning python & I am happy to learn python"))