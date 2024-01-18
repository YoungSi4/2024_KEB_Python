# # Day 5 Assignment
# 9.1 ['Harry', 'Ron', 'Hermione'] 리스트를 반환하는 good() 함수를 정의해보자
#
# def good():
#     Gryffindor = ['Harry', 'Ron', 'Hermione']
#     return Gryffindor
#     # return ['Harry', 'Ron', 'Hermione']
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

# 시도
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





