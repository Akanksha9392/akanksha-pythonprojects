# #NA from 1 to 100
# for x in range(1,101):
#     print(x,end=" ")
# print()
# print()
# #NA from 35 to 50
# for x in range(35,51):
#     print(x,end=" ")
# print()
# print()
# #NA from 100 to 80
# for i in range(100,79,-1):
#     print(i,end=" ")
# print()
# print()

# for i in range(100,79,-2):
#     print(i,end=" ")
# print()
# print()
# #Capital letters from A-Z
# for i in range(65,91):
#     print(chr(i),end=" ")
# print()
# print()
# #small letters from a-z 
# for x in range(122,96,-1):
#     print(chr(x),end=" ")
# print()
# print()

# #NA from 1-10 except 6
# for a in range(1,11):
#     if a==6:
#         continue
#     print(a, end=" ")
# print()
# print()

# #NA  from 1-10 except 3,7
# for x in range(1,11):
#     if x==3 or x==7:
#         continue
#     print(x,end=" ")
# print()
# print()

# #NN in given range
# x=int(input("Enter the starting number:"))
# y=int(input("Enter the ending number"))
# for i in range(x,y+1):
#     print(i,end=" ")
# print()
# print()

# # Even NN in a given range
# x=int(input("Enter the starting number:"))
# y=int(input("Enter the ending number"))
# for i in range(x,y+1):
#     if(i % 2 == 0):
#         print(i,end=" ")
# print()
# print()

# #Multiples of 4
# for x in range(1,101):
#     if x%4==0:
#         print(x,end=" ")
# print()
# print()

# for x in range(1,81):
#     if x%8==0:
#         print(x,end=" ")
# print()
# print()

# #factors of 12
# num=12
# for x in range(1,num+1):
#     if num%x==0:
#         print(x,end=" ")
# print()
# print()

# #multiples of 5 in a range
# x=int(input("Enter the first number:"))
# y=int(input("Enter second number:"))
# for i in range(x,y+1):
#     if i%5==0:
#         print(i,end=" ")
# print()
# print()

# #multiples of a given number in a range
# num=int(input("Enter a number:"))
# x=int(input("Enter the first number:"))
# y=int(input("Enter second number:"))
# for i in range(x,y+1):
#     if i%num==0:
#         print(i,end=" ")
# print()
# print()

# #Sum of NN from 1-10
# total=0
# for i in range(1,11):
#     total += i
# print("Sum of natural num is:",total)
# print()
# print()

# #sum of natural numbers in a given range

# x=int(input("Enter the starting number:"))
# y=int(input("Enter the ending number:"))
# total=0
# for i in range(x,y+1):
#     total += i
# print("Sum of given natural numbers is:",total)
# print()
# print()
# #product of NN in a given range

# x=int(input("Enter the starting number:"))
# y=int(input("Enter the ending number:"))
# total=1
# for i in range(x,y+1):
#     total *= i
# print("Product of given natural numbers is:",total)
# print()
# print()

# #count multiplies of given number
# num=int(input("Enter a number:"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count += 1
# print("Number of factors:",count)
# print()
# print()

# #19.factorial of a number
# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact *= i
# print("Factorial of a number is:",fact)
# print()
# print()

# #check whether the number is prime or not

# num=int(input("Enter a number:"))
# if num > 1:
#     for x in range(2,num):
#         if num%x==0:
#             print("It is not a prime number")
#             break
#     else:
#         print("It is a prime number")
# else:
#     print("It is not a prime ")
# print()
# print()

# # prime numbers from 1-100
# for x in range(2,101):
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         print(x,end=" ")
# print()

# # Prime numbers in a given range
# import math
# x=int(input("Enter the starting number:"))
# y=int(input("Enter the ending number:"))
# print("Prime numbers in the given range:")
# for num in range(x,y+1):
#     if(num>1):
#         for i in range(2,int(math.sqrt(num)) + 1):
#             if num%i==0:
#                 break
#         else:
#             print(num,end=" ")
# #Multiples in a given range
# num=int(input("Enter a number:"))
# x=(int(input("Enter the starting number:")))
# y=(int(input("Enter the ending number:")))
# for i in range(x,y+1):
#     if i%num==0 and i!=0:
#          print(i,end=" ")

# Check whether the given number is perfect number or not.
# num=int(input("Enter a number:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if num==sum:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")

# #Count prime numbers in a given range
# import math
# num=int(input("Enter a number:"))
# start=(int(input("Enter the starting number:")))
# end=(int(input("Enter the ending number:")))
# count=0
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,int(math.sqrt(num))+1):
#             if num%i==0:
#                 break
#         else:
#             # print(num,end=" ")
#             count+=1
# print("Number of primes:",count)

#Check and count perfect numbers in a given range
start=int(input("Enter the starting number:"))
end=(int(input("Enter the ending number:")))
count=0
for num in range(start,end+1):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num,end=" ")
        count+=1
print()
print("Total perfect numbers:",count)

