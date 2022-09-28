a=(input())
itog=0
b=list(a)
print(b)
lenth=len(a)
st=lenth-1
print(lenth)
print("\n")

for i in range(lenth):
    
    itog=itog+int(b[i])*8**st
    st=st-1
print(itog)


