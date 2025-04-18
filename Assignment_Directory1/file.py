#1 Method open and close
'''file1 = open('my_file.txt','r')
#statment
reading_file=file1.readlines()
print(reading_file)
file1.close()'''

'''#2
with open('my_file.txt','r') as file1:
    #statments
    reading_file = file1.read()
    print(reading_file)'''

'''
file1= open('my_file.txt', 'w' )
writing_file= file1.write('Rajesh')
print(writing_file)
file1.close()

file1 = open('my_file.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()

file1 = open('my_file.txt' , 'a')
appending_file = file1.write(' Welcome to python course')
print(appending_file)
file1.close()

file1 = open('my_file.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()'''





#r+---->write and read

file1 = open('my_file.txt', 'r+')
writing_file=file1.write('My Python')
print(writing_file)
file1.close()

file1 = open('my_file.txt', 'r+')
reading_file=file1.read()
print(reading_file)
file1.close()


















