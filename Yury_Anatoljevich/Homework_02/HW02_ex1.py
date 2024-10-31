import os, sys

# clear terminal:
os.system('cls')

try:
    distance = float(input('Input distance in km:\n'))
    rate = float(input("Input specific consumption in l per 100 km:\n"))    
except:
    print('Values should be numeric!\n')
    sys.exit(0)

if distance < 0:
        print('Distance should be non-negative!\n')
        raise Exception("Invalid input data")

if rate <= 0:
        print('Specific consumption must be positive!\n')
        raise Exception("Invalid input data")

consumption = distance * rate / 100
print(f'Fuel consumption at the distance {distance} km is {consumption} litres\n')


