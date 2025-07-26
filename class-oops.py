# class A:
#     def __init__(self): # constractor
#         age = 23
#         print(age)
# obj=A()
# obj2=A()

# class A:
#     "Learnn"
#     age=10
#     print(age)
# obj=A()
# print(obj.age)
# print(A.age)
# print(obj.__doc__)

class A:
    age=10
    def __init__(self,age,name,address):
        print(age," ",name," ",address)

obj=A(10, "ASN", "Khamgaon")
obj2=A(20, "Gojbni", "Delhi")
obj=A("Ajnjn", 12,23)
# print(obj.fun.__doc__)
# print(obj.age)
# print(A.age)