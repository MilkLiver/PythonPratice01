class test2():
    def __new__(self):
        return "new test2"

class test():
    def __new__(self):
        #return "new test"
        return test2()
    def __init__(self):
        print("init OAO")
    def show(self):
        print("show OwO")

        
#test().show()
print(test())
