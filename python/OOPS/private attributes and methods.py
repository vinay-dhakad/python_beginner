class Person:
    __name__ = "king"

    def __hello():               #we have used here 2 underscores to make it private a.  
        print("hello person!")

p1 = Person()

print(p1.__hello())       #error bcoz this is private attribute