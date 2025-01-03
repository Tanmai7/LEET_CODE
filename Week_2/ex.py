def reverse(x):
    sum=0
    while x!=0:
        rem=x%10
        sum=sum*10+rem
        x=x//10
    return sum
input=int(input("enter an num:"))
reversed_input=reverse(input)
print(reversed_input)
