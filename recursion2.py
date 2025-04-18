#FACTORAL

#0! = 1
#1! = 1 * 0! = 1 * 1 = 1
#2! = 2 * 1! = 2 * 1 = 2
#3! = 3 * 2! = 3 * 2 = 6
#4! = 4 * 3! = 4 * 6 = 24

def factoral(n):
    if n<2:
     return 1
    else:
        return n * (factoral(n -1))
result = factoral(9)
print(result)