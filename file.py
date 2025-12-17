#Single Inheritance

class Person:
    def introduce(self):
        print("I am a person.")

print("--- Single Inheritance ---")
class Student(Person):
    def study(self):
        print("Student is studying.")

s = Student()
s.introduce()
s.study()

#Multiple Inheritance

class Person:
    def __init__(self, name):
        self.name = name

print("--- Multiple Inheritance ---")
class Job:
    def __init__(self, position):
        self.position = position

class Employee(Person, Job):
    def __init__(self, name, position):
        Person.__init__(self, name)
        Job.__init__(self, position)

    def show_details(self):
        print("Name:", self.name)
        print("Position:", self.position)

e = Employee("Kale", "Clerk")
e.show_details()

#Multilevel Inheritance

class Person:
    def speak(self):
        print("Person can speak.")

print("--- Multilevel Inheritance ---")
class Teacher(Person):
    def teach(self):
        print("Teacher is teaching.")

class Professor(Teacher):
    def research(self):
        print("Professor is doing research.")

p = Professor()
p.speak()
p.teach()
p.research()

#Hierarchical Inheritance

class Person:
    def sleep(self):
        print("Person is sleeping.")

print("--- Hierarchical Inheritance ---")
class Student(Person):
    def study(self):
        print("Student is studying.")

class Employee(Person):
    def work(self):
        print("Employee is working.")

st = Student()
st.sleep()
st.study()

emp = Employee()
emp.sleep()
emp.work()

# Hybrid Inheritance

class Person:
    def introduce(self):
        print("I am a person.")

print("--- Hybrid Inheritance ---")
class Worker(Person):
    def work(self):
        print("Working.")

class Hobby:
    def relax(self):
        print("Relaxing with a hobby.")

class Freelancer(Worker, Hobby):
    def earn(self):
        print("Earning as a freelancer.")

f = Freelancer()
f.introduce()
f.work()
f.relax()
f.earn()
