from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''decorator'''
        print('Calling decorated function...')
        return func(*args, **kwargs)
    def test():
        pass
    return wrapper
 
@my_decorator 
def example():
    """Docstring""" 
    print('Called example function')

print(example.__name__, example.__doc__)
print(my_decorator.__name__, my_decorator.__doc__)

print("-------------------------------------------------------------------")

a=example
print(a.__name__)
