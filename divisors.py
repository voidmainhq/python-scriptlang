number=int(input("Enter number:"))
i=1
if number<0:
    print("-1 is a divisor")
    number=-number
if number==0:
    print("Every digit is a divisor for 0")
else:
    while i<=number//2:
        if number%i==0:
            print(i, "is a divisor")
        i=i+1
    print(number, "is a divisor")
