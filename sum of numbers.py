def Sum_Of_Digits(number):
    Sum = 0
    while number > 0:
        x = number % 10
        Sum = Sum + x
        number = number //10
    return Sum

number = int(input("введите число:   "))
Sum = Sum_Of_Digits(number)
print("сумма чисел =  ", Sum)