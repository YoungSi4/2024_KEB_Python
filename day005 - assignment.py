# # Day 5 Assignment
# 9.1 ['Harry', 'Ron', 'Hermione'] 리스트를 반환하는 good() 함수를 정의해보자
#
# def good():
#     Gryffindor = ['Harry', 'Ron', 'Hermione']
#     return Gryffindor
#     # return ['Harry', 'Ron', 'Hermione']
#
# print(good())
#

# 교수님 코드
# def good() -> list:
#     """
#     9.1 연습문제
#     :return: list
#     """
#     harry_portter = input().split() # 스플릿이 list에 담아주니까 편함
#     return harry_portter
#
# print(good())

# -------------------------------------------------------------------------------

# 9.2 range(10)의 홀수를 반환하는 get_odds 제네레이터 함수를 정의해보자.
# for로 반환된 세 번째 홀수를 찾아서 출력한다

# 이런 건 곤란해
# def get_odds(numbers):
#     counts = 0
#     for number in numbers:
#         if number % 2 == 1:
#             counts += 1
#         if counts == 3:
#             return number

# # 별로 좋은 코드는 아닌 것 같다.
# counts = 0
# for numbers in range(10):
#     odd = get_odds(numbers)
#
#     if odd != None:
#         counts += 1
#
#     if counts == 3:
#         print(odd)
#         break

# 시도 한 번 더
# odds = []
# for numbers in range(10):
#     if get_odds(numbers) != None:
#         odds.append(get_odds(numbers))
# print(odds[2])

# 내 결론.
# def get_odds():
#     for i in range(10):
#         if i % 2 == 1:
#             yield i
#
# print([i for i in get_odds()][2])

# 교수님 코드
# def get_odds(n) -> int:
#     """
#     1부터 n까지의 홀수를 발생시키는 제네레이터
#     :param n: int
#     :return: 홀수
#     """
#     for i in range(1, n+1, 2):
#         yield i
#
# cnt = 0
# odds = get_odds(9) # 제네레이터에 담아줘야 한다.
# for odd in odds:
#     cnt += 1
#     if cnt == 3:
#         print(f'Third Number is {odd}')
#         break

# -------------------------------------------------------------------------------

# 9.3 어떤 함수가 호출되면 'start'를, 끝나면 'end'를 출력하는 test 데코레이터를 정의해보자
# def test(func):
#     """
#     시작과 끝에 각각 start와 end를 출력해주는 함수입니다.
#     :param func: do_nothing
#     :return: new_func
#     """
#     def new_func():
#             print("start")
#             func()
#             print("end")
#     return new_func
#
# @test
# def do_nothing():
#     """
#     아무런 내용이 없습니다. 그냥 시작과 종료만을 알립니다.
#     :return:
#     """
#     print("operate any")
#     print("terminate any")
#     pass
#
# do_nothing()

# 교수님 방법 1. t라는 객체에 데코를 합체시킨 형태로 입힘
# def test(f):
#     """
#     데코레이터. 함수 시작하면 start 출력, 끝나면 end 출력
#     :param f: function
#     :return: closure function
#     """
#     def test_in(*args, **kwargs): #가변 매개변수이기 때문에 없어도 동작, 100개가 와도 동작
#         print('start')
#         result = f(*args, **kwargs) # result에 담을거면 리턴 해줘야함.
#         print('end')
#         return result
#     return test_in
#
# def greeting():
#     print("안녕하세요")
#
# t = test(greeting)
# t()

# 교수님 방법 2. @로 데코하기
# def test(f):
#     """
#     데코레이터. 함수 시작하면 start 출력, 끝나면 end 출력
#     :param f: function
#     :return: closure function
#     """
#     def test_in(*args, **kwargs): #가변 매개변수이기 때문에 없어도 동작, 100개가 와도 동작
#         print('start')
#         result = f(*args, **kwargs) # 내가 짠 코드처럼 해도 무관함.
#         print('end')
#         return result
#     return test_in
#
# @test
# def greeting():
#     print("안녕하세요")
#
# greeting()

# # 교재 예제
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print("A")
#         result = func(*args, **kwargs)
#         print(f'결과: {result}')
#         return result
#     return new_function
#
# @docu
# def add_ints(a, b):
#     return a + b
#
# print(add_ints(3, 5))

# -------------------------------------------------------------------------------

# 9.4 OopsException 예외를 정의해보자. 이 예외를 발생시켜보자.
#  그리고 이 예외를 잡아서 'Caught an Oops'를 출력하는 코드를 작성해보자.

# class OopsException(Exception):
#     def __init__(self):
#         super().__init__("Caught an Oops")
#
# def iseven():
#     try:
#         even = int(input("짝수를 입력: "))
#         if even % 2 != 0:
#             raise OopsException
#         print(even)
#
#     except Exception as e:
#         print("예외가 발생했습니다.", e)
#
# iseven()

# 교재의 예외 만들기 예제
# class UppercaseException(Exception):
#
# words = ['eenie', 'meenie', 'miny', 'mo']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
#     else:
#         try:
#             raise OopsException('panic')
#         except OopsException as exc:
#             print(exc)
# 교재에서 어떻게 하는건지 안 알려주네





