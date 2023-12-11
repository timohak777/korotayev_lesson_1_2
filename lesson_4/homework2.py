# Зробити гру УКРАЇНСЬКА РУЛЕТКА.

# Програма дає випадкове число от 1 до 6.

# Якщо число 3 - пише що ви програли.
# Якщо 1,2,4,5,6 - ви перемогли.

import random

while True: 
    number=random.randint(1,6)
    print(number)
    if number == 3:
        print("Ви програли ")
    elif 1 <= number <=2 or 4 <= number <= 6:
        print("Ви перемогли ")   
    input_char = input("Введить любий один символ з клавіатури для продовження або 'q' для виходу ")
    ascii_value = ord(input_char)
    if ascii_value == 113:
        break
