#Store the following word meanings in dictionary:
# table : "a piece of furniture","list of facts and figures"
# cat : "a small animal"
# dictionary = {
#         "cat" : "a small animal",
#         "table" : ["a piece of furniture","list of facts and figures"]
# }
# print(dictionary)


#you are given a list of subjects for students.Assume one classroom is required for 1 student.How many classrooms are needed for all students.
# "python" "java" "c++" "javascript" "c" "java" "python" "java" "python" "java"
# subjects = {
# "python","java","c++","javascript","java","python","python","C"
# }
# print(len(subjects))



#WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one. use subject name as a key and mark as value.
# marks = {}

# x = int(input("enter phy: "))
# marks.update({"phy" : x})
# x = int(input("enter math: "))
# marks.update({"math" : x})
# x = int(input("enter che: "))
# marks.update({"che" : x})
# print(marks)



#Figure out a way to store 9&9.0 as a separate values in the set.
# values = {9,9.0,8,8.2,8.0,"9.0"}
# print(values)  


# or


values = {
    ("float",9.0),
    ("int",9)
}
print(values)