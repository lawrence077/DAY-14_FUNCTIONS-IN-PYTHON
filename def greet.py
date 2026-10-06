'''def greet():
    print('hello')
greet()'''

'''def greet(name):
    print('hello',name)
greet('lawrence')'''

'''def add(a,b):
    print(a+b)
add(10,20)'''

'''def greet(name='lawrence'):
    print('hello',name)
greet()'''

'''def greet(name='lawrence'):
    print('hello',name)
greet('john')'''

'''def add(a,b=10):
    print(a+b)
add(5)'''

'''def student(name,age):
    print('name:',name)
    print('age:',age)
student(age=22,name='lawrence')'''

'''def add(*numbers):
    print(numbers)
add(10,20,30)'''

'''def add(*numbers):
    total = 0
    for num in numbers:
        total += num
        print(total)
add(10,20,30,40)'''


def students(**details):
    print(details)
students(name='lawrence',age=22,city='chennai')
