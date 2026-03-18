# problem 1

name = ["yuvraj","mandeep","sharadha","apna college","hitesh"]
hero = ["thor","ironman","spiderman","captain america"]


def print_len(list):
    print(len(list))

print(len(hero))
print(len(name))

# problem 2
    
def print_list(list):
    for item in list:
        print(item,end=", ")
    print()
    
    
print_list(name)        
print_list(hero)        
    
    
# problem 3
    
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact) 

f = int(input("enter a number: "))
cal_fact(f)


# problem 4

def dollar(usd_val):
    inr_val = usd_val * 91
    print(f"${usd_val} = ₹{inr_val}")
    
s = int(input("enter a number to convert: "))
dollar(s)


# problem 5
def odd_even(n):
    if n % 2 == 0:
        return "even"
    elif n != 2 == 0:
        return "odd"
    
m = int(input("enter a number: "))
print(odd_even(m))
