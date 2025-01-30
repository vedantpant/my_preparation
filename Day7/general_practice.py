class MyClass:
    pass

my_object = MyClass()

class MySubClass(MyClass):
    pass

class MyCompositeClass:
    def __init__(self):
        self.contained_object = MyClass()