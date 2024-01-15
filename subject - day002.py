# 과제
# 반복문을 이용해서 섭씨 화씨 전환 프로그램 3번 입력 전까지 계속 작동되도록 만들기
# 방법 1. For 구문
# 방법 2. While 구문
# 들여쓰기를 주의할 것
# 깃허브에 올리세용

# While을 사용하는 경우 # Ctrl + / 로 활성화
# power = 1
# while power == 1:
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

# For를 사용하는 경우
# power = [0]
# looop = 0
# for looop in power:
#     power.append(looop+1)
#
#     menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit  3) Quit Program: ")
#
#     if menu == '1':
#         fahrenheit = float(input('Input Fahenheit : '))
#         print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')
#     elif menu == '2':
#         celsius = float(input('Input Celsius: '))
#         print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9 / 5) + 32):.4f}F')
#     elif menu == '3':
#         print('Terminate Program. Goodnight.')
#         break
#     else:
#         print('Error: You put in a wrong number.')

# 스택 오버플로우에서 코드를 참고했음을 알림
# https://stackoverflow.com/questions/34253996/are-infinite-for-loops-possible-in-python
# l = [1]
# for x in l:
#     l.append(x + 1)
#     print(x)
