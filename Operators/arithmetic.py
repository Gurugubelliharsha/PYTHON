#Write a function for arithmetic operators(+,-,*,/)
def arithmetic(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid operator"
a=eval(input())
b=eval(input())
print(arithmetic(a, b, '+'))
print(arithmetic(a, b, '-'))
print(arithmetic(a, b, '*'))
print(arithmetic(a, b, '/'))
