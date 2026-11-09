a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a<=0 or b<=0:
    print("invalid nums")
    exit()
originala=a
originalb=b
x=a
y=b
while y!=0:
    x,y=y,x%y
nod=x
nok=int((originala*originalb)/nod)
print("NOD:",nod)
print("NOK:",nok)
if nod==1:
    print("prosti sa")
else:
    print("Ne sa prosti i dvete")
