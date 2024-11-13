#Multiple inheritance allows a class to be derived from more than one base class, inheriting features from all base classes.
class Father:
    fathername=""
    def father(self):
        print(self.fathername)
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)
class Son(Father,Mother):
    def parents(self):
        print("father ----->",self.fathername)
        print("mother ----->",self.mothername)
obj=Son()
obj.fathername="Mark"
obj.mothername="Sonia"
obj.parents()