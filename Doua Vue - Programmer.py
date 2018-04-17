class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)

class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def job(self):
        print("You work as an employee")

class Programmer(Person):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age)

    def program(self):
        print("You program Games")
