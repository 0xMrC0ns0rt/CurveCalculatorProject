print ('''


   ____  _____ ___    __  ______ 
  / __ \/ ___//   |  /  |/  /   |
 / / / /\__ \/ /| | / /|_/ / /| |
/ /_/ /___/ / ___ |/ /  / / ___ |
\____//____/_/  |_/_/  /_/_/  |_|
                                 
----------(C) 2023 . Curve calculator project----------
''')
import sympy
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
def f(x):
  func = input('Input the function and use (x) : ')
  return func

x = sympy.Symbol('x')
derivative = sympy.diff(f(x), x)
r1 = int(input('Input the range argument (1) : '))
r2 = int(input('Input the range argument (2) : '))
x_values = range(r1, r2)
derivative_values = []

for x_val in x_values:
  derivative_values.append(derivative.evalf(subs={x: x_val}))

plt.plot(x_values, derivative_values)
print('The first derivative is: ',derivative)
derivative2 = sympy.diff(derivative, x)
print('The second derivative is: ',derivative2)
sol1 = solve(derivative)
sol2 = solve(derivative2)
print('X  in the first derivative = ',sol1)
print('X  in the second derivative = ',sol2)
plt.show()
