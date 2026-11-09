N=int(input("Enter a number: "))
if N<=0:
    print("Nevliden broi")
    exit()
sum=0
biggestodd=None
for i in range(N):
    number=int(input("Enter another number:"))
    if number%2==0:
        sum=sum+number
    else:
        if biggestodd==None or biggestodd<number:
            biggestodd=number
if biggestodd==None:
    print("Nqma nechetni")
else:
    print(biggestodd)
print(sum)
