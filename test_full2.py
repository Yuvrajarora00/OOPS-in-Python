# problem 5

a = int(input("enter a number to find factorial: "))
fact = 1
for i in range(1, a + 1):
    fact *= i

print(fact)


# problem 6
n = int(input("enter a number to find prime number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime number")
else:
    print("not prime")


# problem 7

k = input("enter a string: ")
vov = "aeiouAEIOU"
count = 0
print("vovels are:", end="")
for i in k:
    if i in vov:
        print(i, end="\n")
        count += 1


print(count)


# problem 8
c = int(input("enter a number: "))
for i in range(1, c + 1):
    print("*" * i, end="")
    print("")
