# testing 1
def recursion(n):
    if n == 0:
        return
    print(n)
    recursion(n-1)

m = int(input("enter a number: "))
recursion(m)



# sum 2 
def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n-1) + n

k = int(input("enter a number: "))
print(sum(k))   


# sum 3

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx],end=",")
    print_list(list, idx+1)
    
superman = ["ironman","thor","spiderman","thanos"]
print_list(superman)