# num=int(input("enter the number"))
# i=num
# fac=1
# while i>=0:
#     fac=fac*i
#     i=i-1
#     print("factorial=","*",fac)



# i=int(input("enter the number"))
# orig=i
# sum=0
# while i>0:
#     sum=sum+(i%10)*(i%10)*(i%10)
#     i=i//10
# if orig==sum:
#     print("number is armstrang")
# else:
#     print("number is not armstrang")




# i=int(input("enter the number"))
# rew= 0
# while i>0:
#     rew=(rew*10)+i%10
#     i=i//10
# print("revers=",rew)







# num=int(input("enter the factor number"))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i)
#     i=i+1



    
# num=int(input("enter the number"))
# i=num
# sum=0
# while i<=num:
#     r=i%10
#     sum=sum+r
#     r=r//10
# i=i+1
# if  sum==num:     
#     print(num,"harsad number hai")
# else:
#     print(num,"harsad number nhi hai")

                


    
# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while z<n:
#     print(z)
#     x=y
#     y=z
#     z=x+y





a=[1,2,3,1,2,3,1,2,3,1,3,3,3]
i=0
b=[]
count=0
while i<len(a):
    c=a[i]
    count=count+1
    if count%2==0:
        b.append(c)
    i=i+1
print(b)
    


