class A(object):
    def __init__(self,num):
        self.num = num
    
    def __contains__(self, item):
        '''
        @summary:当使用in，not in 对象的时候 ,not in 是在in完成后再取反,实际上还是in操作
        '''
        print("__contains__:%s is in?"%item)
        if item < self.num and item >= 0:
            return True
        return False
    
if __name__ == "__main__":
    if 3 in A(10):
        print("True")
    else:
        print("False")
    if 3 not in A(10):
        print("True")
    else:
        print("False")
