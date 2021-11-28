# k=1
# i=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print(" ",end=" ")
#         b=b+1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j=j+1
#     print()
#     k=k+2
#     i=i+1


# i=1
# while i<=5:
#     b=0
#     while b<=4:
#             print(" ",end=" ")
#             b=b+1
#     j=1
#     while j<=i:
#             print("*",end=" ")
#             j=j+1
#     print()
#     i=i+1


# i=1
# while i<=100:
#     j=1
#     count=1
#     while j<=100:
#         if i==j:
#             if i%j==0 and i%1==0:
#              i=i+1
#                print(i)
#     i=i+1



# i=1
# while i<=4:
#     j=1
#     while j<=4:
#         print(i,end=" ")
#         j=j+1
#     print()
#     i=i+1

# k=65
# i=65
# while i<=73:
#     j=65
#     while j<=k:
#         print(chr(k),end=" ")
#         j=j+1
#     print()
#     k=k+1
#     i=i+1

# n=int(input("enter the number"))
i=1
while i<=100:
    j=1
    count=0
    while j<=100:
        if (i%j==0):
            count=count+1
        j=j+1
    i=i+1
if count==2:
    print(i,"is prime")
else:
    print(i,"is not prime")


# num=1
# while num<=100:
#     i=1
#     while i<=100:
#         if i==num and num%i==0 and num%1==0:
#             count=0
#             if num%(i+1)==0:
    #             count=count+1
    #             if count==2:
    #                 print(num,"is a prime")
    #             else:
    #                 print(num,"is not prime")
    #     i=i+1
    # num=num+1    











