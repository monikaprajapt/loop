question_list = ["1).how many continents are there?",              

                "2).What is the capital of India?",          

                "3).NG mei kaun se course padhaya jaata hai?"

]
options_list = [
    ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
    ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
    ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
]
solution=[3,4,1]
answer_list=[
    ["(1)foue","(3)seven"],
    ["(4)delhi","(2)bhupal"],
    ["(4)agriculture","(1)software engineering"]     
]
print("welcome to kon banega crocrepati")
i=0
s=0
count=0
while i<len(question_list):
    print(question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[b][a]
        print(a+1,k)
        a=a+1
    num1=input("do you want life lain")
    if num1=="yes":
        print("5050 life line")
        if count<1:
            print(answer_list[b])
            num2=int(input("enter the answer"))
            if num2==solution[i]:
                s=s+10000
                print("right your answer")
                print("you win rs/",s)
            else:
                print("your answer is rong")
                print("you can piay again")
                print("you win rs/",s)
                break
            count=count+1
        else:
            print("you already use lifeline")
            m=int(input("anter your answer"))
            if m==solution[i]:
                print("congres right answer")
                s=s+10000
                print("you win rs/",s)
            else:
                print("no chance")
                print("your answer is worng")
                print("you win rs/",s)
                break
    else:
        pass
        k=int(input("enter you won answer"))
        if k==solution[i]:
          print("congres right answer")
          s=s+10000
          print("you are win rs/",s)
        else:
          print("no chance")
          print("your answer is worng")
          print("you are win rs/",s)
          break
    i=i+1
print("congrescutionl you are big part kon banega crorrpati")
print("you are win rs/",s)
print("thank you are part of this aap jit gye")



 



