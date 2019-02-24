import random
r = random.randint(1,10)
print('r\n')


def hello(x):
    print('Tejas'+ str(len('Tejas')) + x)
    print('is' + x)
    print('Beast' + x)
hello('xxxx')
hello('xxx')
hello('xx')

def addition(x):
    return x+1
n = addition(10)
print(n)

a = 10

def scope(a):
    a = 20
    print(a)
print(a)
scope(20)
