# n=int(input("Enter a Number:"))
# x=str(n)
# y=len(x)
# count=1
# sum=0
# while count<=y:
#     n=n%10
# 

# n=input("Enter Your Name:")
# i=0
# while i<len(n):
#     j=n.upper()
#     print (j[i]+n[i],end="__")
#     i=i+1

# n=input("Enter Your Name:")
# i=0
# while i<len(n):
#     j=n.upper()
#     print (j[i]+i*n[i],end="__")
#     i=i+1
# print()


k=1
while k<=7:
    space=2
    while space<=4:
        print(" ",end="")
        space=space+1
    star=8-k
    while star>=1:
        print("*",end=" ")
        star=star-1
    print()
    k=k+1


