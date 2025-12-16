class Person:
    name = "afgani"

    # def changeName(obj, name):
    #   self.__class__.name = "Rahul"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("santa clos")
print(p1.name)
print(Person.name)