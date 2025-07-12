# Take a number from the user and print whether it's even or odd.
num=int(input("Enter A number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

# Write a program to count the number of vowels in a given string.

def num_vowels(s):
    count=0
    vowel="AEIOUaeiou"
    for char in vowel:
        if char in s:
            count+=1
    return count
print(num_vowels("Python is very effective"))

# Ask the user to input a sentence and print the number of words in it.
def num_word(s):
    s=s.replace(" ","")
    word=[]
    count=0
    for char in s:
        count+=1
    return count
print(num_word(input("Enter a sentence: ")))

# Take a number from the user and print its multiplication table from 1 to 10 using a function.

def is_multiply(s):
    base=int(input("Enter a number: "))
    for i in range(1,11):
        result=i*base
        print(f"{base}x{i}={result}")
is_multiply("")


# Write a program to accept 5 numbers from the user, 
# store them in a list, and print the maximum and minimum values.
def is_number():
    l1=[]
    for i in range(5):
        l1.append(int(input("Enter The Number: ")))
    return max(l1),min(l1)
max,min=is_number()
print("Max is:",max)
print('min is:',min)

# Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.
even_number=[]
for i in range(5):
    num=int(input("Enter a number: "))
    if num % 2 == 0:
        even_number.append(num)
print("Even Number Is",even_number)

#Accept a string and check whether it is a palindrome or not (same forward and backward).

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]
palindrome=input("Enter a string:")
if is_palindrome(palindrome):
    print("The word is palindrome")
else:
    print("The Word is not a palindrome")


# Accept a list of numbers and remove all duplicate values

def is_remove():
    number=[]
    for i in range (5):
        num=int(input("Enter a Number: "))
        number.append(num)

    unique_number=[]
    for num in number:
        if num not in unique_number:
            unique_number.append(num)
    print("list of Unique Number",unique_number)
is_remove()

# Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)

secret_number=7
while True:
    guess=int(input("Guess The Number: "))
    if guess==secret_number:
        print("Number Matched!!!!")
        break
    else:
        print("Try Again!!!!!")
    
    