# 숙제 리뷰
# Assignment (loop)

# while True:
#     menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit  3) Quit Program: ")
#
#     if menu == '1':
#         fahrenheit = float(input('Input Fahenheit : '))
#         print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')
#     elif menu == '2':
#         celsius = float(input('Input Celsius: '))
#         print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9/5) + 32):.4f}F')
#     elif menu == '3':
#         print('Terminate Program. Goodnight.')
#         break
#     else:
#         print('Error: You put in a wrong number.')
#

# 5장 문자열 Text Strings
# university = 'inha\nuniversity'
# print(university)

#문자열 결합
# number1 = input("First number: ")
# number2 = input("Second number: ")
# print(number1*5 + number2)

# Substring, slice
# print(university[:4])
# print(university[:-11])
# print(university[0:len(university)])
# print(university[:16])
# print(university[::2])

# split()
# course = '2024 KEB bootcamp'
# print(course)
# list_course = course.split('B')
# print(list_course)

# 중요!!!
# numbers = input("FirstNumber SecondNumber: ").split()
# print(numbers[0] + numbers[1]) # 문자열 합성만 된다 concatenation
# print(int(numbers[0]) + int(numbers[1]))

# join()
subjects = ["python", "cpp", "database"]
subjects_string = " ".join(subjects)
print(subjects_string)


