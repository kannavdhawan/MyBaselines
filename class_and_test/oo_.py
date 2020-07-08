#telusco


# 1 -----------------------------------------basic-----------------------------------------------------------------------
class Student:
    school="uow"                                        # class variable or static variable
    def __init__(self,name,enroll_no):                  # instance method --> can only access instance variables

        pass
        self.name=name                                  # instance variable
        self.enroll_no=enroll_no
    
                                                        # getters and setters 
    def get_name(self):
        return self.name
    def get_enroll_no(self):
        return self.enroll_no
    def set_name(self,n1):
        self.name=n1
    def set_enroll_no(self,e1):
        self.enroll_no=e1

    @classmethod                                        # class method  --> can only access class variables
    def class_method1(cls):
        return cls.school

                                                        # static method --> can't use any variable 
    def static_method():
        print("I am a static method")

s1=Student("Kannav",369)
s2=Student("Dhawan",123)

print(s1.get_name(), s1.get_enroll_no())
print(Student.class_method1())
print(Student.static_method())

# 2 ---------------------------------------------------------------------            Inner class-------------------------------------
print("-----------------------------2-------------------------------")
class Student1:
    def __init__(self,name,rollno):
        pass
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()                                           # instance of inner class made

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()                                             # inner class object called 
    
    class Laptop:                                                   # inner class made
        def __init__(self):
            self.brand="HP"
            self.price=898988
        def show(self):
            print(self.brand,self.price)
        
s1=Student1("kannav",369)
# s2=Student1("dhawan",123)
s1.show()
# s2.show()



# 3 --------------------------------- Inheritance---------------------------------------

class A:
    def __init__(self):
        pass
    def feature1(self):
        print("feature 1 ")
    def feature2(self):
        print("feature 2 ")

class B(A):
    def __init__(self):
        pass
    def feature3(self):
        print("feature 3 ")
    def feature4(self):
        print("feature 4 ")

class C(B):
    def __init__(self):
        pass
    def feature5(self):
        print("feature 5 ")
class D:
    def feature6(self):
        print("feature 6")
class E(C,D):                                                    # Multiple inheritance 
    def feature7(self):
        print("feature 7")


a1=A()

b1=B()

c1=C()

d1=D()

e1=E()


b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1.feature5()
d1.feature6()           # only 6 can be accessed
e1.feature7() 

# 4 -------------------------- constructor in inheritance -----------------------------------------------

class X:
    def __init__(self):
        print("X's init")
class Y(X):
    def __init__(self):
        super().__init__()
        print("Y's init")
class Z(Y):
    pass
    # def __init__(self):
    #     print("z's init")

y1=Y() # will access y's init
z1=Z() # z doesnt have any init so it will search for y's init . if it doesnt have init then it will go for x's init 
# if we want to access x's constructor as well 


# super() functionality in multiple inheritance 
# it will go for first class i.e. A(B,C) using super in A's init will call B . so bias 
# it is method resolution order 
# same goes for the same named methods in the two classes.
# super can also be used to access methods 

# 5--------------------------------polymorphism-------------------------------------------------------------------------

# a. Duck Typing 
class Pycharm:
    def execute(self):
        print("running")
        print("compiling")
class Laptop1:
    def code(self,ide):
        ide.execute()
ide=Pycharm()
l1=Laptop1()    # not passing anything because no constructor 
l1.code(ide)  # VERY IMPORTANT !!!! Here we are passing argument while calling the function


# b. Operator overloading 
class Student3:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,second_object):
        m1=self.m1+second_object.m1
        m2=self.m2+second_object.m2
        s3=Student3(m1,m2)
        return s3      # required to return to come out of the function with an object created for the class with updated values.

    def __gt__(self,other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        if s1 > s2:
            return True
        else:
            return False    
    def __str__(self):
        return self.m1,self.m2
s1=Student3(111,69)
s2=Student3(60,65)

s3=s1+s2 # cant directly add objects because there exists no class to add objects . so make explicitly 
print(s3.m1,s3.m2)

# same for comparison i.e gt ge etc 
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


#ex:
a=100 
print(a.__str__())
print(s3.__str__())
# if we want toprint value of s3 then we need to override the method __str__




# method overloading--> not in python  with trick -- copy 
# using def(self, a=None, b=None, c=None)

# method overriding -similar to construcor overriding 
class P:
    def show(self):
        print("In P's show")
class Q(P):
    pass
    def show(self):
        print("In Q's show")
q1=Q()
q1.show()


