sum=0
twodigit=0
i=0
while True:
    number=int(input("Enter a number:"))
    if number<0:
        if i==0:
            print("Nqma dani")
            exit()
        break
    check=0
    i=i+1
    sum=sum+number
    while number>0:
        number=number//10
        check=check+1
    if check==2:
        twodigit=twodigit+1
avarage=round(sum/i,2)
print(sum ,twodigit,avarage)
