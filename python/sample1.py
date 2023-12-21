class A():
    def __init__(self, *args, **kwargs):
        print("A")

class B():
    def __init__(self, *args, **kwargs):
        print("B")

class C(A):
    def __init__(self, *args, **kwargs):
        print("C","arg=", *args)
        super().__init__(self, *args, **kwargs)

class D(B):
    def __init__(self, *args, **kwargs):
        print("D", "arg=", *args)
        super().__init__(self, *args, **kwargs)

class E(C,D):
    def __init__(self, *args, **kwargs):
        print("E", "arg=", *args)
        super().__init__(self, *args, **kwargs)
    def s(self):
        print("yes")


# now you can call the classes with a variable amount of arguments
# which are also delegated to the parent classed through the super() calls
a = A(5, 5)
b = B(4, 4)
c = C(1, 2, 4, happy=True)
d = D(1, 3, 2)
e = E(1, 4, 5, 5, 5, 5, value=4)
print(e.s)