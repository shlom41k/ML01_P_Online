import os
# finding max and min, and a specific point of the parabolic function

# clear terminal:
os.system('cls')

def f(x):
     return(-26 * x**2 + 25 * x - 9)

derivative = list()

dx = 0.1 # step
x1 = -5 # left point
x2 = x1 + dx # central point 
x3 = x2 + dx # right point
y1 = f(x1)
y2 = f(x2)
y3 = f(x3)
# initialize dict for max and min:
maxmin = {
      "xmax" : x1,
      "ymax" : f(x1),
      "xmin" : x1,
      "ymin" : f(x1)      
}

d = (f(x2) - f(x1)) / dx
derivative.append(d) # one-side derivative for the first point x = -5

while x2 <= 5 - dx:
    # finding min and max:
    if y2 > maxmin['ymax']:
          maxmin["xmax"] = x2
          maxmin["ymax"] = y2
    elif y2 < maxmin["ymin"]:
          maxmin["xmin"] = x2
          maxmin["ymin"] = y2
    # finding two-side derivative:
    d = (y3-y1) / 2 / dx 
    derivative.append(d)
    # next step for x and y:
    x1, x2, x3 = x2, x3, x3 + dx
    y1, y2, y3 = y2, y3, f(x3)

d = (f(x3) - f(x2)) / dx
derivative.append(d) # one-side derivative for the last point x = 5

print(f'Maximum value of function: {maxmin["ymax"]} \n')
print(f'Minimum value of function: {maxmin["ymin"]} \n')

# simple way for finding special points, valid only when a single max and/or single min is definitely present:
if maxmin["xmin"] > -5:
      print(f'Special point is a point of minumum: x = {maxmin["xmin"]}, y = {maxmin["ymin"]}\n')
if maxmin["xmax"] < 5:
      print(f'Special point is a point of maximum: x = {maxmin["xmax"]}, y = {maxmin["ymax"]}\n')

# more universal way of finding all extremum points using the derivative:
for i in range(len(derivative)-1):
      xi = -5 + i * dx
      if derivative[i] * derivative[i+1] <= 0:
            print("Another way for finding the special points:\n")
            d1 = abs(derivative[i])
            d2 = abs(derivative[i+1])
            x0 = (d1 * (xi + dx) + d2 * xi) / (d1 + d2)
            y0 = f(x0)
            if derivative[i] >= 0 and derivative[i+1] <= 0:
                 print(f'Special point is a point of maximum: x = {x0}, y = {y0}\n')
            else:
                 print(f'Special point is a point of minumum: x = {x0}, y = {y0}\n') 



