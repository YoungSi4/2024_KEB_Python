# 숙제 리뷰
# Assignment (loop)

while True:
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit  3) Quit Program: ")

    if menu == '1':
        fahrenheit = float(input('Input Fahenheit : '))
        print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celsius: '))
        print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9/5) + 32):.4f}F')
    elif menu == '3':
        print('Terminate Program. Goodnight.')
        break
    else:
        print('Error: You put in a wrong number.')

