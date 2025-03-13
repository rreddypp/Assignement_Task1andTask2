n = 1  #GLOBAL VARIABLE

def fn():
    n = 5
    print("in", n) #LOCAL VARIABLE
fn()

print(n)