nn="testOwO"
def test(n):
    print("P1",n)
    def test2(t):
        print("P2",t)
    print("P3",n)
    return test2

OAOTest=test("OwO")
OAOTest("OAO")
OAOTest2=test("Test1")("Test2")



def tag(tag_name):
    def add_tag(content):
        print("test1")
        #return "<{0}>{1}</{0}>".format(tag_name, content)
        return add_tag2
    def add_tag2(content):
        print("test2")
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag

content = 'Hello'

add_tag = tag('a')
print (add_tag(content))


add_tag = tag('b')
print (add_tag(content))

print("-----------------------------------------------------------------------")

OwO=tag("c")
print(OwO(content)("OUO"))


