class Kls(object):
    num_inst = 0
    testword="test"

    def __init__(self,testword="test"):
        Kls.num_inst = Kls.num_inst + 1
        self.testword=testword
        Kls.testword=Kls.testword+"t"
        print(self)

    @classmethod
    def get_no_of_instance(cls):
        return cls.num_inst

    def get_no_of_instance2(self):
        return self.num_inst

    @classmethod
    def show_test_word(self):
        return self.testword

    def show_test_word2(self):
        return self.testword

ik1 = Kls()
ik2 = Kls("QAQ")

print("OAO")
print(ik1.get_no_of_instance())
print(Kls.get_no_of_instance())
print("OAO2")
print(ik2.get_no_of_instance())
print(Kls.get_no_of_instance())

print(ik1.get_no_of_instance2())
#print(Kls.get_no_of_instance2())

print("---------------------------------------------------------------------")

print(ik1.show_test_word())
print(ik2.show_test_word())
print(Kls.show_test_word())

print("---------------------------------------------------------------------")

print(ik1.show_test_word2())
print(ik2.show_test_word2())
#print(Kls.show_test_word2())
print(Kls("OUO").show_test_word2())
