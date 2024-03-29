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

# -------------------------------------------------------------------------------

# 5장 문자열 Text Strings
# university = 'inha\nuniversity'
# print(university)

# 문자열 결합
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
# subjects = ["python", "cpp", "database"]
# subjects_string = " ".join(subjects)
# print(subjects_string)

# replace()
# course = '2024 KEB bootcamp'
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)

# 교체 횟수 정해보기
# course = 'KEB 2024 KEB bootcamp KEB'
# print(course)
# course = course.replace('KEB', 'Inha', 1)
# print(course)
# course = course.replace('KEB', 'Inha', 1)
# print(course)

# strip()
# course = 'KEB 2024 KEB !! bootcamp KEB...*!#'
# print(course)
# print(course.strip())
# print(course.strip("!#.*"))

# -------------------------------------------------------------------------------

# 탐색
# course = 'KEB 2024 KEB !! bootcamp KEB...*!#'
# print(course.find("KEB"))
# print(course.rfind("KEB"))
# print(course.find("Inha"))
# print(course[25])
# print(course.index("KEB"))
# print(course.rindex("KEB"))
# print(course.index("Inha")) # ValueError: substring not found

# 종합 활용 예제: find 사용
# subjects = "python cpp database linux"
# subject = input("수강신청과목 입력: ")
#
# if subjects.find(subject) != -1:
#     print(f"해당 과목이 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다.")
# else:
#     print('해당 과목이 없습니다.')

# index를 쓸 경우의 예외처리 방법
# subjects = "python cpp database linux"
# subject = input("수강신청과목 입력: ")
#
# if subjects.index(subject) != -1: # 없으면 value 예외를 반환한다.
#     print(f"해당 과목이 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다.")
# else:
#     print('해당 과목이 없습니다.')

# -------------------------------------------------------------------------------
# 고쳐보자. 예외처리의 프리뷰

# subjects = "python cpp database linux"
# subject = input("수강신청과목 입력: ")
#
# try:
#     print(f"해당 과목이 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다.")
#
# except ValueError:
#     print('해당 과목이 없습니다.')

# .isalnum
# subjects = "python cpp database linux 123" # Fasle
# print(subjects.isalnum())
# subjects = "pythoncppdatabaselinux123" # True
# print(subjects.isalnum())

# Case 서식 수정
# Aligment 정렬
# 출력방식
# print('%e' % 0.7045)

# dictionary 를 활용한 .format() 스트링으로 출력
# subjects = {'python': 'kim', 'cpp': "song", 'datastructure' : 'kim', 'database' : 'kang'}
# print("{0[cpp]} {0[database]}".format(subjects))

# 소수를 찾는 프로그램. prime number. while 활용 v5.0, 1 같은 케이스 제거
# 계속 진화할 예정
# number = int(input("Input Number : "))
# is_prime = True # int > bool
#
# if number < 2: # 1 이하의 소수가 아닌 모든 숫자 처리
#     print(f"{number} is not prime number")
# else:
#     i = 2
#
#     while i < number:
#         if number % i == 0:
#             is_prime = False # 연산 제거
#             break
#         # print(i, end=' ')
#         i += 1
#
#     # print('\n')
#     if is_prime: # remove ==
#         print(f"{number} is prime number")
#     else:
#         print(f"{number} is not prime number")


# 책의 예제를 range를 활용해서
# univ = "inha"
# i = 0
# while i < len(univ): # side effect가 발생할 확률이 높다
#     print(univ[i], end=' ') # 줄바꿈 대신 띄어쓰기로 적어준다
#     i += 1
# print()
#
# for letter in univ: # 훨씬 간단하고 안전한 코드이다.
#     print(letter, end=' ') # 대신 특정 구간만 슬라이스 하고 싶을 때 쓰기 어렵다
#     # univ에서 inha를 다 꺼낼 때까지 작동하기 때문이다. 이럴 때 while을 사용
#
# print()

# for k in range(0, len(univ), 1): # range(시작, 종료, 구간 크기)
# for k in range(len(univ)):
#     print(univ[k], end=' ')

# 아까 그 소수 탐색 프로그램 v6.0 for를 사용해서 더 간략하게
# number = int(input("Input Number : "))
# is_prime = True # int > bool
#
# if number < 2: # 1 이하의 소수가 아닌 모든 숫자 처리
#     print(f"{number} is not prime number")
# else:
#     for i in range(2, number): #for를 이용해 더 줄였다
#         if number % i == 0:
#             is_prime = False # 연산 제거
#             break
#         # print(i, end=' ')
#
#     # print('\n')
#     if is_prime: # remove ==
#         print(f"{number} is prime number")
#     else:
#         print(f"{number} is not prime number")

# range 자체는 generator이지 출력을 위한 그런 게 아님
# print(range(3, 9)) # 출력이 이상하게 된다
# print(list(range(3, 9)))

# range로 감소하는 출력
# for x in range(2, -1, -1):
# 	print(x)

# 죽지도 않고 돌아온 소수 프로그램 v8.0
# 2개 입력 받고 그 사이의 소수를 출력하는 프로그램
# numbers = input("Input First Second Number : ").split()  #str로 받음 > .split()으로 리스트로 바꿈**
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2: # 큰 수가 먼저 입력되는 경우를 처리해줌
#     n1, n2 = n2, n1 # ㅅㅂ 파이썬은 이게 되네, 튜플 패킹 언패킹을 활용.
#
# for number in range(n1, n2+1):
#     is_prime = True # 계속 True로 리셋해줘야 False 일 때 소수를 출력한 후 다시 정상으로 돌아온다.
#
#     if number < 2:
#         pass # 그냥 넘어가는 함수. 자리는 차지하는데 아무것도 하지 않는 명령어. 비우면 오류 생길 때 씀.
#         # 대신 continue를 사용할 수 있다.
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 is_prime = False
#                 break # 현재 for만 탈출
#
#         if is_prime: print(number, end=' ')


# 과제! 2024 - 01 -16 화
# 1. 어제 했던 과제에서 3번 메뉴를 소수 판정 프로그램 숫자 하나 받아서 4번 메뉴는 구간 소수 출력 프로그램 5번을 종료
# 2. 교재 143p 연습문제 6.5번 - 1, 2, 3번 작성해서 깃허브에 올릴 것
