# problem 6
s = int(input("enter a number: "))
i = 1
while i<11:
    print(s*i)    
    i += 1
    
# problem 7

li = [1,3,5,7,9,76,54,32,24,65]
i = 0
while i<len(li):
    print(li[i])
    i += 1

# problem 8
v = int(input("enter a numer: "))
li = (1,3,5,7,9,76,54,32,24,65,5)
i = 0
while i<len(li):
    if (li[i] == v):
        print("found at",i)
    else:
        print("not found")
    i+=1



# problems using for loop

list = [1,2,3,4,56,6,7,8,9]
for i in list:
    print(i)  