task=[]
status=[]
user=int(input("enter the how many task : "))
i=0
while i<user:
    t=input("enter the task : ")
    task.append(t)
    print(task)
    s=input("enter the status : ")
    status.append(s)
    print(status)
    i=i+1
c=0
p=len(task)
p=len(status)
while c<p:
    print(task[c],"=",status[c])
    c=c+1
user=input("what you want to do ? ")
if user=="add":
    task1=input("enter tha task u want to do : ")
    status2=input("enter the statu u want to do : ")
    task.append(task1)
    status.append(status2)
c=0
p=len(task)
p=len(status)
while c<p:
    print(task[c],"=",status[c])
    c=c+1
user1=input("what you want to do ? ")
if user1=="remove":
    task3=input("enter the task : ")
    status4=input("enter the status : ")
    task.remove(task3)
    status.remove(status4)
c=0
p=len(task)
p=len(status)
while c<p:
    print(task[c],"=",status[c])
    c=c+1
user=input("enter that what  you want to do ? ")
if user=="eadit":
    status5=input("enter the status : ")
    status.append(status5)
    print(status[c])
    c=c+1








    
    
