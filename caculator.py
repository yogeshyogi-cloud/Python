def Addtion(a,b):
    return a+b
def Substartion(a,b):
    return a-b
def multipulation(a,b):
    return a*b
def divided(a,b):
    return a/b
def sI(a,b,c):
    return (a,b,c)/100
def cI(a,b,c):
    return a*pow((1+c/100),b)


print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"
        "5. Simple Interset\n"
        "6. Compound Interset\n")
user=int(input("Choice a Caluclation"))

a=int(input("Enter A value"))
b=int(input("Enter B value"))
if user==1:
    print(a,"+",b,"=",Addtion(a,b))
elif user==2:
    print(Substartion(a,b))
elif user==3:
    print(multipulation(a,b))
elif user==4:
    print(divided(a,b))
elif user==5:
    a=int(input("Enter A value"))
    b=int(input("Enter B value"))
    c=int(input("Enter C Value"))
    print("Thank for Enter a Advanced Option!!!")
    
    print(sI(a,b,c))

elif user==6:
    a=int(input("Enter A value"))
    b=int(input("Enter B value"))
    c=int(input("Enter C Value"))
    print("Thank for Enter a Advanced Option!!!")
    print( cI(a,b,c))
else:
    print("Invalid Option!!!1")

      