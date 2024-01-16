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

# 소수를 찾는 프로그램. prime number. while 활용 v2.0, 탐색 횟수 2번 감소
number = int(input("Input Number : "))
cnt = 0
i = 2

while i < number:
    if number % i == 0:
        cnt += 1
    i += 1

if cnt == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")

