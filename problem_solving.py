# Probelm 1
import random
number1 = []
square_number = []
cube_numbers = []
for i in range(10):
    random_number = random.randint(-10,10)
    number1.append(random_number)
print(number1)
for number in number1:
    square_number.append(number **2)
    cube_numbers.append(number **3)
print("square of list", square_number)
print("Cube of list ", cube_numbers)
