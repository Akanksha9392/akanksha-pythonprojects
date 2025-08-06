# class i_class:
#     def m1(self):
#         print("It is an instance method/Non-static method")
# i=i_class()
# i.m1()
# print()

#class()

# class c_class():
#     @classmethod
#     def m2(cls):
#         print("This is a class method")
# c=c_class()
# c.m2()
# print()
# c_class.m2()
# print()

#static method

# class s_class:
#     @staticmethod
#     def m3():
#         print("this is a static method")
# c=s_class()
# c.m3()
# print()
# s_class.m3()


# class c1_class():
#     @staticmethod
#     def m3(x,y):
#         print("The sum is:",x+y)
# c1=c1_class()
# 

class c_class():
    def __init__(self):
        print("This is a constructor method")
    def m1(self):
        print("This is an Instance/non-static method")
    @classmethod
    def m2(a):
        print("This is a class method")
    @staticmethod
    def m3(x,y):
        print("This is a static method and the mul is",x*y)
a=c_class()
a.m1()
print()
a.m2()
print()
c_class.m2()
print()
a.m3(4,7)
print()
c_class.m3(4,7)