# Assignment No.1 : 섭씨 화씨 변환 프로그램에 소수 탐색 프로그램 붙이기

# while True:
#     menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit \
#     3) Prime number 4) Prime number range 5) Quit Program: ")
#
#     if menu == '1':
#         fahrenheit = float(input('Input Fahenheit : '))
#         print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')
#
#     elif menu == '2':
#         celsius = float(input('Input Celsius: '))
#         print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9/5) + 32):.4f}F')
#
#     elif menu == '3':
#         number = int(input("Input Number : "))
#         is_prime = True
#
#         if number < 2:
#             print(f"{number} is not prime number")
#         else:
#             for i in range(2, number):
#                 if number % i == 0:
#                     is_prime = False
#                     break
#                 # print(i, end=' ')
#
#             # print('\n')
#             if is_prime:
#                 print(f"{number} is prime number")
#             else:
#                 print(f"{number} is not prime number")
#
#     elif menu == '4':
#         numbers = input("Input First Second Number : ").split() # 숫자 하나만 입력하는 경우?
#         n1 = int(numbers[0])
#         n2 = int(numbers[1])
#
#         if n1 > n2:
#             n1, n2 = n2, n1   # 입력부터 순서 바꾸는 것까지, 코드라인 줄이고 더 가독성 좋게.
#
#         for number in range(n1, n2 + 1):
#             is_prime = True
#
#             if number < 2:
#                 pass
#                 # 대신 continue를 사용할 수 있다.
#             else:
#                 for i in range(2, number): # 위에 중복되는 코드 존재. 함수, 모듈화 필요
#                     if number % i == 0:    # 너무 많이 돈다.
#                         is_prime = False
#                         break
#
#                 if is_prime: print(number, end=' ')
#         print() # print 자체에 줄바꿈을 가지고 있다
#
#     elif menu == '5':
#         print('Terminate Program. Goodnight.')
#         break
#     else:
#         pass

# ----------------------------------------------------------------------------------

# Assignment No.2 : 143p practice #6.5 - 1, 2, 3.
# 1: for 문으로 리스트 [3, 2, 1, 0] 을 출력하기

# Solution 1 > 길이를 정하고 시작한 거라 별로 마음에 안 든다.

# list = [0, 0, 0, 0]
# index = 0
# for number in range(3, -1, -1):
#     list[index] = number
#     index += 1
# print(list)

# Solution 2

# list = []
# for number in range(3, -1, -1):
#     list.append(number)
# print(list)

# Solution 3

# print([i for i in range(3, -1, -1)])

# Solution 4

# for i in [list(range(3, -1, -1))]:
#     print(i)


# ---------------------------------------------------------------------------------------------------------------

# 2: guess_me 변수에 7을 할당하고, number 변수에 1을 할당한다. number와 guess_me를 비교하는 while 문을 작성해보자.
# number가 guess_me보다 작으면 too low를 출력, 같으면 found it!을 출력하고 반복문 종료, 크면 oops를 출력하고 반목문 종료
# 그리고 반복문의 마지막에 number을 1씩 증가시킨다.

# guess_me = 7
# number = 1
#
# while True:
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print("found it!")
#         break
#     else:
#         print("oops")
#         break
#     number += 1

# ---------------------------------------------------------------------------------------------------------------

# 3: guess_me 변수에 5를 할당하고, for문을 사용하여 range(10)에서 number 변수를 사용한다.
# number가 guess_me보다 작으면 too low를 출력, 같으면 found it!을 출력하고 반복문을 종료
# number가 guess_me보다 크면 oops를 출력하고 반복문을 종료한다.

# guess_me = 5

# for number in range(10):
#     if number < guess_me:
#         print("too low")
#     elif number == guess_me:
#         print(f"found it!")
#         break
#     else:
#         print("oops")
#         break

# ---------------------------------------------------------------------------------------------------------------