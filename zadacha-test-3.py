while True:
    n=int(input("Enter number:"))
    if n>=0:
        break
sum=0
reversed=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit
    reversed=reversed*10+digit
    temp=temp//10
print(sum)
print(reversed)
if n==reversed:
    print("Palindrom")
else:
    print("Ne e palindrom")
