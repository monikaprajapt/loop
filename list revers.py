# a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# i=0
# j=(len(a))-1
# while i<j:
#     t=a[i]
#     a[i]=a[j]
#     a[j]=t
#     i=i+1
#     j=j-1
# print(a)



# n=int(input("enter the number"))
# rev=0
# x=n
# while n>0:
#     rev=(rev*10)+n%10
#     n=n//10
# if (x==rev):
#     print("it is palindrom number")
# else:
#     print("it is not plindrom number")





# a=[2,3,4,7,6]
# b=[5,4,7,2,4]
# i=0
# sum_list=[]
# while i<(len(a)):
#     sum_list.append(a[i]+b[i])
#     i=i+1
# print(sum_list)






num=[1,0,0,1,1,0,1,1]
i=0
sum=0
while i<len(num):
    a=num[-i-1]
    sum=sum+a*(2**i)
    i=i+1
print(sum)    



