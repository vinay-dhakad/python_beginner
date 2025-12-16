# #single inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name


# car1 = Toyota("fortuner")
# car2 = Toyota("prius")

# print(car1.start())




# #multi - inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class Toyota(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()



#multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varC)