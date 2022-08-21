num =int(input("Enter  a Postive Number\n"))
s=0
temp=num
while temp >0:
    c=temp%10
    s+=c**3
    temp //=10
if num ==s:
    print(" Its a armstrong NUmber")
else:
    print(" Not  armstrong")        