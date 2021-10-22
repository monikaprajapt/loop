num=int(input("enter the number"))
a=num
sum=0
i=1
while i<num:
    f=1
    r=num%10
    while i<=r:
        f=f*i
        i=i+1
    sum=sum+a
    num=num//10
if sum==a:
    print("hai")
else:
    ("nhi")