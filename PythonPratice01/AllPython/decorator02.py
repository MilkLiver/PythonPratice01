def sidedish1(meal):
    return lambda: meal() /2
    
def sidedish2(meal):
    return lambda: meal() + 40

@sidedish1
@sidedish2
def friedchicken():
    return 50.0

print(friedchicken())   # 119.0
