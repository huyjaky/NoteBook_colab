import math

print("Enter a, b, c follow format: ax^2+bx+c=0")
a = int(input())
b = int(input())
c = int(input())


def calc_quadratic_equation(a, b, c):
    delta = b**2 - 4 * (a * c)
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return {'x1': x1, 'x2': x2}
    elif delta < 0:
        return "equation without solution"
    else:
        return -b / (2 * a)


def calc_linear_equation(b, c):
    a = b
    b = c
    return -b/a

if (a == 0):
    calc_linear_equation(b, c)
else :
    result = calc_quadratic_equation(a, b, c)
    # switch result case 
    if (isinstance(result, dict)):
        x1 = result.get('x1')
        x2 = result.get('x2')
        print(f'x1 = {x1}\nx2 = {x2}')
        
    elif (isinstance(result, str)):
        print(result)
    else: 
        print(f'x1 = x2 = {result}')
