# # Ctrl + A로 간단하게 모든 코드를 활성화 ! 혹은 영역을 지정하고 Ctrl + / 로 영역별 활성화 !

# # 딕셔너리 컴프리헨션
# univ = 'inha university'
# count_alphabet = {letter : univ.count(letter) for letter in univ}
# print(count_alphabet)
#
# # 컴프리헨션 아닌 형태로
# univ = 'inha university'
# count_alphabet = dict()
# for letter in univ:
#     count_alphabet[letter] = univ.count(letter)
# print (count_alphabet)

# # 과제 8.10
# squares = {n : pow(n, 2) for n in range(10) } # n**2나 n*n으로 해도 된다.
# print(squares)

# # set의 연산
#
# drinks = {
#     'martini' : {'vodka', 'vermouth'},
#     'black russian' : {'vodka', 'kahlua'},
#     'white russian' : {'vodka', 'kahlua', 'cream'},
#     'manhattan' : {'rye', 'vermouth', 'bitters'},
#     'screwdriver' : {"orange juice", "vodka"}
# }
#
# print(not drinks['screwdriver'] & {'vermouth', 'vodka'}) # not을 붙이는 순간 False 를 반환. bool 형
# # True False에 따른 칵테일 이름을 출력하도록 유도해야함
#
# print(drinks['screwdriver'] & {'vermouth', 'vodka'}) # not을 안 붙이면 'vodka'를 반환.
# # 해당 내용을 반환 받고 싶으면 이렇게

# # 함수
# # Prime number with funcrtion
# def isprime(n) -> bool: # 리턴값 명시. 없어도 되는데 있으면 더 좋다.
#     """
#     매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 반환
#     :param n: 소수인지 판정할 매개변수
#     :return: 소수 True, 아니면 False
#     """
#     pass
#     if n < 2:
#         return False # False를 반환하고 함수를 즉시 종료한다.
#
#     else:
#         i = 2
#         while i*i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True # True를 반환하고 함수를 즉시 종료한다.


# # 이전에 만들어둔 소수 찾는 코드
#
# help(isprime)
# # print(isprime.__doc__) # 해당 함수의 document를 보여준다.
#
# while True:
#     menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit 3) Prime number 4) Prime number range 5) Quit Program: ")
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
#         if isprime(number):
#             print(f"{number} is prime number")
#         else:
#             print(f"{number} is not prime number")
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
#             if isprime(number):
#                 print(number, end=' ')
#         print() # print 자체에 줄바꿈을 가지고 있다
#
#     elif menu == '5':
#         print('Terminate Program. Goodnight.')
#         break
#     else:
#         pass

# # 함수의 오버로딩? 파이썬에는 없다.
# def a(n1, n2):
#     print(n1, n2)
#
# def a(n):
#     print(n)
#
# a(7) # 다른 객체지향 언어에서는 지원한다.
# a(7, 11) # 갯수가 다르면 다른 함수 취급해서 호출해주는데, 파이썬은 이건 지원 안 한다.


# # None 과 False 상세히.
# def a(n):
#     if n is None:
#         print(f'{n}은 논')
#     elif n:
#         print(f'{n}은 트루')
#     else:
#         print(f'{n}은 거짓')
#
# a(None) # None
# a([]) # False
# a([0]) # True # 여기에 주의. 얜 빈 리스트가 아님.
# a(0) # False
# a('') # False
# a(-9) # True
# a(' ') # True

# # 함수 추가
# def squares(*n):
#     # return n*n # 튜플끼리 곱셈 불가능.
#     # 몇개가 올지 모르므로 len을 먼저 쓴다.
#     """
#     넘겨 받은 수치 데이터를 거듭제곱 값을 리스트에 담아 리턴
#     :param n: tuple
#     :return: list
#     """
#     return [pow(i, 2) for i in n]
#     # return i*i
#
# def run_func(f, *number) -> list: # 결국 squares에게 받은 리스트를 리턴하기 떄문
#     return f(*number) # ??... ??
#
# print(squares(7, 5, 2))
# print(run_func(squares, 9, 10))

# # 클로저의 이해
# def outter_func(nout):
#     def inner_func(nin):
#         return nin * nin
#     return inner_func(nout)
# print(outter_func(5)) # 기존 이너 아우터 함수 방식

# # closure
# def outter_func(nout):
#     def inner_func():
#         return nout * nout
#     return inner_func
#
# x = outter_func(9) # 이 x는 함수이기 떄문에,
# print(x())         # x에 값을 주거나 / x(7) / 있으면 비우고 굴려야한다.
# print(x)
# print(type(x))

# ------------------------------------------------------------------------

# # 익명함수 가기 전에 map. mapping의 줄임말. 사상하다 비추다라는 뜻
# numbers = ["7", "-11", "3"]
# total_sum = 0
# for number in numbers:
#     total_sum += int(number)
# print(total_sum)             # 너무 길고 복잡하다.
#
# numbers = ["7", "-11", "3"]
# print(sum(map(int, numbers))) # map(함수이름, 적용할 대상)
# # 말도 안 되게 짧아졌다.
#
#
# ------------------------------------------------------------------------


# # 소수 탐색에 map 적용해서 개선
#
# def isprime(n) -> bool: # 리턴값 명시. 없어도 되는데 있으면 더 좋다.
#     """
#     매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 반환
#     :param n: 소수인지 판정할 매개변수
#     :return: 소수 True, 아니면 False
#     """
#     pass
#     if n < 2:
#         return False # False를 반환하고 함수를 즉시 종료한다.
#
#     else:
#         i = 2
#         while i*i <= n:
#             if n % i == 0:
#                 return False
#             i += 1
#         return True # True를 반환하고 함수를 즉시 종료한다.
#
# while True:
#     menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit 3) Prime number 4) Prime number range 5) Quit Program: ")
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
#         if isprime(number):
#             print(f"{number} is prime number")
#         else:
#             print(f"{number} is not prime number")
#
#     elif menu == '4':
#         n1, n2 = map(int, input("Input first second number: ").split()) # 여기를 수정했다.
#         n1, n2 = min(n1, n2), max(n1, n2) # 밑의 if문을 내장 함수로 간소화
#
#         # numbers = input("Input First Second Number : ").split() # 숫자 하나만 입력하는 경우?
#         # n1 = int(numbers[0])
#         # n2 = int(numbers[1])
#
#
#         # if n1 > n2:
#         #     n1, n2 = n2, n1
#
#         for number in range(n1, n2 + 1):
#             if isprime(number):
#                 print(number, end=' ')
#         print() # print 자체에 줄바꿈을 가지고 있다
#
#     elif menu == '5':
#         print('Terminate Program. Goodnight.')
#         break
#     else:
#         pass


def squares(n):
    return n*n

even_numbers = [i for i in range(51) if i % 2 == 0]
print(tuple(map(squares, even_numbers))) # 굳이 함수를 안 쓰고 람다를 쓰고 싶다.

print(tuple(map(lambda x: x**2, even_numbers)))
z = lambda x: pow(x,2)
print(tuple(map(z, even_numbers)))
