class Father:
    def func1(self):
        print("This is parent class")
class Son(Father):
    def func2(self):
        print("This is child class")
obj=Son()
obj.func1()