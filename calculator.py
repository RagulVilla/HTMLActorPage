input1 = input('Enter the first number:')
a = float(input1) 

input2 = input('Enter the second number:')
b = float(input2)

c = input ('Enter the arithmetic operator:')

def calculation():
    if c == '+':
        print(a+b)
    if c == '-':
        print(a-b)
    if c == '*':
        print(a*b)
    if c == '/':
        print(a/b)
    if c =='**':
        print(a**b)
        
calculation()
