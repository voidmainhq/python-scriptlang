num=int(input("enter a number: "))
while num<1:
    num=int(input("Please enter a positive number: "))
a=0
b=1
if num==1:
    print(0)
elif num==2:
    print(1)
else:
    for i in range(num-2):
        extra=a+b
        a=b
        b=extra
    print(b) 
# 0 1 1 2 3 5 8
# extra=5, a=3, b=5
# 1, 2, 3, 5 => skips first n second digit
