# Зробити "Орел та Решка".

# Програма випадково показує на екран слово ОРЕЛ або РЕШКА.

# Як зробити:
# 1. випадкове число
# 2. if

# Приклад: якщо 1 то орел...........

import random

while True:
    number=random.randint(1,2)
    if number == 1:
        print("ОРЕЛ")
    else:
        print("РЕШКА")
    input_char = input("Введить любий один символ з клавіатури для продовження або 'q' для виходу ")
    ascii_value = ord(input_char)
    if ascii_value == 113:
        break
