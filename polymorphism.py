# # Operator overloading....
# class productclass:
#     def __init__(self,items):
#         self.items=items
# p1=productclass(90)
# print(p1)

# class productclass:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return "Number of items in p1 is:"+str(self.items)
# p1=productclass(90)
# print(p1)

# # For Arthemetic operators
# class productclass:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __add__(self,other):
#         return self.items+other.items
# p1=productclass(90)
# print("Number of items in p1 is:",p1)
# print()
# p2=productclass(120)
# print("Number of items in p2 is:",p2)
# print()
# print("Result set is:",p1+p2)
# print()

# class p2class:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __pow__(self,other):
#         return self.items**other.items
# p3=p2class(3)
# print("Number of items in p3 is:",p3)
# print()
# p4=p2class(2)
# print("Number of items in p4 is:",p4)
# print()
# print("Result set is:",p3**p4)
# print()


# # For assignment operators
# class productclass:
#     def __init__(self,items):
#         self.items=items
#     def __str__(self):
#         return str(self.items)
#     def __iadd__(self,other):
#         return self.items+other.items
# p1=productclass(90)
# print("Number of items in p1 is:",p1)
# print()
# p2=productclass(120)
# print("Number of items in p2 is:",p2)
# print()
# p1+=p2
# print("Result set is:",p1)
# print()

# class sclass:
#     def __init__(self,marks):
#         self.marks=marks
#     def __str__(self):
#         return str(self.marks)
#     def __imul__(self,other):
#         return self.marks*other.marks
# s1=sclass(80)
# print("Marks of maths subject:",s1)
# print()
# s2=sclass(88)
# print("Marks of science subject:",s2)
# print()
# s1*=s2
# print("Result is:",s1)


# # method overloading

# class aclass:
#     def m1(self):
#         print("0's number of argument")
#     def m1(self,x1):
#         print("1's number of argument")
#     def m1(self,x1,x2):
#         print("2's number of argument")
# a=aclass()
# a.m1(100,200)

# # method overloading using default argument
# class A_class:
#     def m1(self,obj1=None,obj2=None,obj3=None):
#         if(obj1!=None and obj2!=None and obj3!=None):
#             print("Sum of three number of arguments:",obj1+obj2+obj3)
#         elif(obj1!=None and obj2!=None):
#             print("Sum of two numbers of arguments:",obj1+obj2)
#         else:
#             print("Only allow three or two number of argument")
# a1=A_class()
# a1.m1(10,20,30)
# print()
# a1.m1(10,20)
# print()
# a1.m1(10)
# print()
# print("End of an application")

# Method overloading using variable(*) length argument
# class bclass:
#     def m1(self,*x1):
#         for x in x1:
#             print(x)
# b=bclass()
# b.m1(10)
# b.m1(10,20)
# b.m1(10,20,30)
# b.m1(10,20,30,40)

# class bclass:
#     def m1(self,*x1):
#         y=0
#         for x in x1:
#             y=y+x
#         print("sum of arguments:",y)
# b=bclass()
# b.m1(10)
# b.m1(10,20)
# b.m1(10,20,30)
# b.m1(10,20,30,40)

# class A_class:
#     def m1(self,*X1):
#         for a1 in X1:
#             print(a1)      
# a1=A_class()
# a1.m1(1001,"Mobile_1",23000.0,"Samsung")
# print()
# a1.m1(1002,"Mobile_2",25000.0,"Samsung")
# print()
# class A_class:
#     def __init__(self,a1=None,A2=None,a3=None):
#         print("Constructor overloading using default argument")
# a1=A_class(10,20,30)
# print()
# a1=A_class(10,20)
# print()
# a1=A_class(10)
# print()

# class A_class:
#     def __init__(self,*a1):
#         print("Constructor overloading using default argument")
# a1=A_class(10)
# print()
# a1=A_class(10,20)
# print()
# a1=A_class(10,20,30)
# print()
# a1=A_class(10,20,30,40)
# print()
# a1=A_class(10,20,30,40,50)
# print()

class pclass1:
    def __init__(self,pid,pname):
        self.pid=pid
        self.pname=pname
    def m1(self):
        print("Pid is:",self.pid)
        print("Pname is:",self.pname)
class Product_Class_2(pclass1):
    def __init__(self,pid,pname,Price,Company,M_date,Exp_date):
        super().__init__(pid,pname)
        self.Price=Price 
        self.Company=Company 
        self.M_date=M_date 
        self.Exp_date=Exp_date 
    def m2(self):
        super().m1()
        print("Price is:",self.Price)
        print("Company is:",self.Company) 
        print("M_date is:",self.M_date)
        print("Exp_date is:",self.Exp_date)
p1=Product_Class_2(1001,"Mobile_1",23000,"Sasung","12/7/2025","12/72026")
p1.m2()
print()