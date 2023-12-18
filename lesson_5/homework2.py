number1=int(input("Введіть перше число: "))
number2=int(input("Введіть друге число: "))

numbers={
    "number1":number1,
    "number2":number2,
}
if numbers["number1"]>numbers["number2"] :
    print(f"Number1 = {numbers["number1"]} більше Number2 = {numbers["number2"]}")

elif numbers["number1"]<numbers["number2"] :
    print(f"Number2  = {numbers["number2"]} більше Number1 = {numbers["number1"]}")
else:   
    print(f"Числа рівні {number1}")  




#Створити словник, який описує два числа і потім за допомогою команди IF вивести на екран більше число 
    