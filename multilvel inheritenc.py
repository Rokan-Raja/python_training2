class Base:
    print("Hi")

class Derived1(Base):
    a = Base()
    print("Welcome")

class Derived2(Derived1):
    b = Derived1()