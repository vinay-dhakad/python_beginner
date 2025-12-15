#class is blueprint of object.
# class Student:
#     name = "mustafa"

# s1 = Student()
# print(s1)



# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class  Car:
#     brand = "bmw"
#     color = "red"

# car1 = Car()
# print(car1.brand)
# print(car1.color)

#__init__Function

# class Student:
    # def __init__(self, fullname):   #if we don't create constructor[def __init__] than python will create it by own nd we have to always pass an argument inside constructor self-argument
        # self.name = fullname
#         print("adding new student in Database..")

# s1 = Student("karan")
# print(s1.name) 

# s2 = Student("mustafa")
# print(s2.name)            #constructor calls again for every new object.





# class Student:
#     def __init__(self, name, marks):   #if we don't create constructor[def __init__] than python will create it by own nd we have to always pass an argument inside constructor self-argument
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")

# s1 = Student("karan", 44)
# print(s1.name,s1.marks) 

# s2 = Student("mustafa", 90)
# print(s2.name,s2.marks)            #constructor calls again for every new object.


# class Student:
#      #default constructors
#      def __init__(self):
#         pass
     
#     #parameterized constructors
#     def __init__(self, name, marks):   
#         self.name = name
#         self.marks = marks
#          print("adding new student in Database..")

# s1 = Student("karan", 44)
# print(s1.name,s1.marks) 

# s2 = Student("mustafa", 90)
# print(s2.name,s2.marks)


# class Student:
#     college_name = "ABC College"     #class attribute

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new students in Database..")


# s1 = Student("rahul gandhi", 1)
# print(s1.name, s1.marks)
# print(Student.college_name)



class Student:
    college_name = "ABC College"     #class attribute

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in Database..")

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("rahul gandhi", 1)
s1.welcome()
print(s1.get_marks())