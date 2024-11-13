# Hierarchical Inheritance

# Hierarchical inheritance occurs when multiple derived classes inherit from a single base class.
class Parent:
    def func1(self):
        print("This is parent class")
class Child1(Parent):
    def func2(self):
        print("This is child class 1")
class Child2(Parent):
    def func3(self):
        print("This is child class 2")
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj2.func1()
