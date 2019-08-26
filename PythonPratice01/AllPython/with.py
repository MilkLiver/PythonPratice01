class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        #print(Sample.__class__.__dict__)
        print("In __exit__()")
        print(type)
        print(value)
        print(trace)
        if type==ValueError:
            print("Value Error!!")
        #return False
        return True
        

    
def get_sample():
    print("get")
    return Sample()


with get_sample() as sample:
    inp=int(input("test:"))
    print ("sample:", sample)

print("OwO")

print('-----------------------------------------------------------------------')

class A:  
    def __enter__(self):  
        print('in enter') 
    def __exit__(self, e_t, e_v, t_b):  
        print('in exit' )
  
with A() as a:
    print('in with')

#print(open.__class__.__dict__)
