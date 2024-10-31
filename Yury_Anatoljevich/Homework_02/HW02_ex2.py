import os, sys

# clear terminal:
os.system('cls')

print('Input coefficients of quadratic equation: a, b, c')
try:
    a = float(input('Input coefficient a:\n'))
    b = float(input('Input coefficient b:\n'))    
    c = float(input('Input coefficient c:\n'))
    D = b**2 - 4 * a * c
except:
    print('Values should be numeric!\n')
    sys.exit(0)

if D < 0:
      print('No roots!\n')
else:
      x1 = (-b - D**0.5) / 2 / a
      x2 = (-b + D**0.5) / 2 / a

print(f'The roots of the equation are {x1} and {x2}\n')


