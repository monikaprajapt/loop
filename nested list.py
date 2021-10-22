from typing import SupportsComplex


number=30
# n=[10,11,12,13,14,17,18,19]
# i=0
# b=[]
# while i<len(n):
#     c=0
#     while c<len(n):
#         if  n[i]+n[c]==30:
#             k=n[i],n[c]
#             b.append(k)
#         c=c+1
#     i=i+1
# print(b)
    

# magic_square=[
#         [8,3,4],
#         [1,5,9],
#         [6,7,2]
# ]
# i=0
# while i<len(magic_square):
#     j=0
#     sum=0
#     while j<len(magic_square):
#         sum=sum+magic_square[i][j]
#         j=j+1
#     i=i+1     
# print(sum)
# r=0
# while r<len(magic_square):
#     k=0
#     sum1=0
#     while k<len(magic_square):
#         sum1=sum1+magic_square[r][k]
#         k=k+1
#     r=r+1
# print(sum1)
# p=0
# m=p
# sum=2
# while p<len(magic_square):
#     sum2=sum2+magic_square[p][m]
#     p=p+1
# print(sum2)





# elements=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# even=0
# odd=0
# a=[]
# b=[]
# length=len(elements)
# while i<len(elements):
#     if elements[i]%2==0:
#         a.append(elements[i])
#         even=even+1       
#     else:
#         odd=odd+1
#         b.append(elements[i])
#     i=i+1
# print("even count=",even,a,)
# print("odd= count",odd,b,)




# elements=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# count1=0
# count2=0
# a=[]
# b=[]
# sum1=0
# sum2=0
# avg1=0
# avg2=0
# while i<len(elements):
#     h=elements[i]
#     if h%2==0:
#         a.append(h)
#         count1=count1+1 
#         sum1=sum1+h  
#         avg1=sum1/count1    
#     else:
#         count2=count2+1
#         b.append(h)
#         sum2=sum2+h
#         avg2=sum2/count2
#     i=i+1

# print("even=",count1,a,sum1,avg1)
# print("odd=",count2,b,sum2,avg2)






# students=["rishabh","rahul","abhishek","faizal","monika","muskan"]
# marks=[10,20,56,45,36,20]
# length=len(students)
# length=len(marks)
# counter=0
# while counter<length:
#     print(students[counter]+str(marks[counter]))
#     counter=counter+1




# marks=[
#     [78,76,94,86,88],
#     [91,78,98,65,76],
#     [95,45,78,52,49]    
# ]
# i=0
# sum=0
# while i<len(marks):
#     a=0
#     b=0
#     while a<len(marks[i]):
#         b=b+marks[i][a]
#         a=a+1
#     sum=sum=b
#     i=i+1
# print("marks sum=",sum)




# marks=[
#     [78,76,94,86,88],
#     [91,78,98,65,76],
#     [95,45,78,52,49]    
# ]
# i=0
# count=0
# while i<len(marks):
#     a=0
#     sum=0
#     b=0
#     while a<len(marks[i]):
#         b=b+marks[i][a]
#         a=a+1
#     sum=sum+b
#     ave=sum/len(marks[i])
#     count=count+1
#     i=i+1
# print(count,"year age=",ave)





# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# d=[]
# while i<len(char_list):
#     j=0    
#     c=[]
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count=count+1
#         j=j+1
#     c.append(char_list[i])
#     c.append(count)
#     if c not in d:
#         d.append(c)
#     i=i+1
# print(d)










# kitana_pisa_hai=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# crorepati=[]
# lakhpati=[]
# dilwale=[]
# i=0
# while i<len("kitna_paisa_hai"):
#     if i<100000:
#         crorepati.append(kitana_pisa_hai[i])
#         # print("crorpati hai")
#     # if i>100000 and i<10000000:
#         # print("lakhpati hai")
#     if i<100000:
#         lakhpati.append(kitana_pisa_hai[i])
#         # print("lakhpati")
#         # break
#     else:
#         dilwale.append(kitana_pisa_hai[i])
#         # print("dilwale")
#     i=i+1
# print("crorepati hai",crorepati)
# print("lakhpati hai",lakhpati)
# print("dilwale hai",dilwale) 
# 
# 
# 
# 
# list=[[5,10,15],[2,4,9],[3,6,9]]
# i=0
# sum=0
# while i<len(list):
#         j=0
#         while j<len(list[i]):
#                 sum=sum+list[i][j]
#                 j=j+1
#                 # print(sum)
#         i=i+1
# print(sum)



# a=[1,2,3,[4,5,6,],23,[7,8,9]]
# i=0
# sum=0
# while i<len(a):
#     b=a[i]
#     if type(b) is list:
#         j=0
#         while j<len(b):
#             sum=sum+b[j]
#             j=j+1
#     else:
#         sum=sum+a[i]
#     i=i+1
# print(sum)


a=[1,2,3,[4,5,6,],[6,7,8],20]
i=0
sum=0
while i<len(a):
    b=a[i]
    if type(b) is list:
        j=0
        while j<len(b):
            sum=sum+b[j]
            j=j+1
    else:
        sum=sum+a[i]
    i=i+1
print(sum)




# a=[1,3,5,6,7,8,10]
# i=0
# while i<len(a):








    
