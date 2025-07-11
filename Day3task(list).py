l1=[1,8,7,9,5,6,21]

l1.sort()
print(l1)


l1.reverse()
print(l1)


l1.append(5)
print(l1)


l1.insert(5,4)
print(l1)


last_item=l1.pop() # pop ley chai index remove garney kaam garcha
print(l1)
print(last_item)

l1.remove(9)# remove ley chai value nai remove garney kaam garcha
print(l1)

third_item=l1.pop(2)
print(third_item)
print(l1)

# wap to store seven fruits in a list entered by the user
def store_fruits():
    fruits=[]
    for i in range(7):
        fruits.append(input("Enter the fruits name: "))
    return fruits
print(store_fruits())


#wap to accept marks of 6 students and display them in a sorted manner
def accept_marks():
    marks=[]
    for i in range(6):
        marks.append(input("Enter the mask:"))
        marks.sort()
    return marks
print(accept_marks())

#Wap to sum a list with 4 numbers
def sum_list():
    l1=[1,2,3,4]
    sum=0
    for i in l1:
        sum+=i
    return sum
print(sum_list())




