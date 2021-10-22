user=input("enter the name")
string=list(user)
vowel=['a','e','i','o','u']
string.sort()
for i in string:
    if i in vowel:
        print("vowel")
    else:
        print("consident")