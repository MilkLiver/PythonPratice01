class Fruit(object):
    def __init__(self):
        print("just a fruit")
        #print("init test")
        pass

    def print_color(self):
        print("this fruit is in purple")

class Apple(Fruit):
    testfruit="I am fruit"
    def __init__(self):
        pass

    def print_color(self):
        print(self.testfruit)
        self.testfruit="fruit is died"
        print(self.testfruit)
        print(self)
        print("apple is in red")

class Orange(Fruit):
    def __init__(self):
        print("Hi apple")
        pass

    def print_color(self):
        print(self)
        print("orange is in orange")

class FruitFactory(object):
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        print(name)
        if name in cls.fruits.keys():
            print(cls)
            return cls.fruits[name]()
        else:
            return Fruit()
    def __init__(self,name):
        print(name,"init test")
    def test(self):
        print("test")

#Apple.testfruit="fruit is disappear
        
fruit1 = FruitFactory("apple")
fruit2 = FruitFactory("orange")
fruit3 = FruitFactory("grape")
fruit4 = FruitFactory("orange")
print("---------------------------------------------------------------------------")
fruit1.print_color()    
fruit2.print_color()
fruit3.print_color()
print("---------------------------------------------------------------------------")
print(Apple.testfruit)
Apple.testfruit="fruit is disappear"
print(Apple.testfruit)
#fruit1.test()
print("fruit2:",id(fruit2))
print("fruit4:",id(fruit4))
print(fruit2 is fruit4)


