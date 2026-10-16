number=int (input("Enter a number:"))
prime=1
if number<=1:
    prime=0
else:
    for i in range(2, number//2): # // rounds it to the nearest integer
        if number%i==0:
          prime=0
          break
if prime==0 or number==4:
    print(number, "isnt prime")
else:
    print(number, "is prime")
