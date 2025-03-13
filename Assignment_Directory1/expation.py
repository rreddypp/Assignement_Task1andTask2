try:
    a=6
    b=0
    print(a/b)
except ZeroDivisionError:
    print("There is an error")
finally:
    print('Contiune with the following  code')