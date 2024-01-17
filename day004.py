# # Assignment 소수 구간 v8.0 수정사항 추가
# numbers = input("Input First Second Number : ").split() # 하나만 입력한 경우?
# n1 = int(numbers[0])
# n2 = int(numbers[1])
#
# if n1 > n2:
#     n1, n2 = n2, n1     # 2 ~ 7 번줄까지 가독성, 코드 압축 가능
#
# for number in range(n1, n2+1):
#     is_prime = True
#     i = 2
#
#     if number < 2:
#         pass
#
#     else:
#         while i*i <= number: # 메뉴 3번과 중복 기능. 함수, 모듈화, i > i*i ??
#             if number % i == 0:
#                 is_prime = False
#                 break
#             print(i, end=' ')
#             i += 1
#
#         if is_prime: print(number, end=' ')

# # 튜플
# t1 = (5) # 튜플이 아님. 최소 한 개 이상의 쉼표가 있어야 함
# t2 = (5,)
# t3 = 5,
# t6 = 'python', 'kim'
# print(type(t1),type(t2), type(t3), type(t6))
# print(t6[0], t6[1])
# subject, prof = t6
# print(subject, prof)
# # a, b, c = t6 #ValueError: not enough values to unpack (expected 3, got 2)
#
# t7 = ()
# print(type(t7)) # tuple. 빈 튜플은 예외
# t8 = tuple()    # 다른 자료형을 튜플로 만들 때 주로 사용
# print(type(t8)) # <class 'tuple'>

# # 괄호와 반저멩 주의
# print(type('py',))
# print(type(('py'),))
# print(type(('py',)))
# t9 = ('py',)
# print(type(t9)) # == print(type(('py',)))

# # 튜플 간 비교연산이 가능하다
# t10 = 1, 2, 3
# t11 = 1, 2
# print(t10 == t11)
# print(t10 <= t11)
# print(t10 > t11)
# t11 = 1, 21
# print(t10 <= t11)
# print(t10 > t11) # 정확한 기준? 총합의 크기?
#
# # 튜플의 수정이 가능하다
# print(t10 + t11)

# # 튜플의 변수명이 동일하면 동일한 튜플인걸까?
# t12 = 4.43,
# t13 = 3.97, 4.1, 3.27
# print(t12 + t13)
# print(id(t12)) #1199411778016
# t12 = t12 + t13
# print(t12)
# print(id(t12)) #1199411975552 > 둘이 다른 튜플이다! 새로 만들어서 준거야

# # List
# list = 'cat'
# print(list[0])

# # 임시로 튜플을 리스트로 바꿀 수  있다.
# a_tuple = ('ready', 'fire', 'aim')
# a_tuple = (a_tuple)
# print(a_tuple)

# # 리스트를 스플릿 할 수 있다.

# # 어... reverse의 특징?
# subjects = ['cpp', 'java', 'python']
# print(subjects[::-1])
# subjects[::-1]
# print(subjects)
# subjects.reverse()
# print(subjects)

# # 지우는 명령어 실험
# subjects = ['cpp', 'java', 'python']
# print(subjects)
# del subjects[2]
# subjects.remove("java")
# print(subjects)
# subjects.pop()
# print(subjects)

# # sort, sorted
# 1.
# subjects = ['java', 'python','cpp']
# print(subjects)
# subjects.sort()
# print(subjects)
# subjects.sort(reverse=True)
# print(subjects)

# 2.
# subjects = ['java', 'python', 5, 'cpp', 4, 9, '데이터베이스']
# print(subjects)
# subjects.sort()
# print(subjects)
# subjects.sort(reverse=True)
# print(subjects)

# 3.
# subjects = ['java', 'python', '5', 'cpp', '4', '9', '데이터베이스']
# sorted(subjects)
# print(subjects)
# subjects = sorted(subjects)
# print(subjects)


# # Copy
# subjects = ["a", "b", "c"]
# subjects = ["a", ["b", "c"], "d"]
# a = subjects
# b = subjects.copy()
# c = list(subjects)
# d = subjects[:]
# print(subjects, a, b, c, d)
# subjects[1][1] = 'x'
# print(subjects, a, b, c, d)

# # deep copy
# import copy
# subjects = ["a", ["b", "c"], "d"]
# a = subjects
# b = subjects.copy()
# c = list(subjects)
# d = subjects[:]
# e = copy.deepcopy(a)
# print(subjects, a, b, c, d, e)
# subjects[1][1] = 'x'
# print(subjects, a, b, c, d, e)

# # List Comphrehension
# square of 1 to 5
# squares = list()
# squares.append(1*1)
# squares.append(2*2)
# squares.append(3*3)
# squares.append(4*4)
# squares.append(5*5)
# print(squares) # 최악
#
# squares = list()
# for i in range(1, 6):
#     squares.append(i*i)
# print(squares)

# # 자 잘봐
# squares = [i*i for i in range(1, 6)] # 정말 간결하고 강력하다. 축약식 표현
# print(squares)
#
# even_squares = [i*i for i in range(1, 6)  if i % 2 == 0]
# print(even_squares)

# # Lists of Lists 예제
# small_birds = ['humingbird', 'finch']
# extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
# carol_birds = [3, 'French hens', '2', 'turtledoves']
# all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
#
# print(all_birds)
# print(all_birds[0])
# print(all_birds[0][1])

# # Dictionary

# 1.
# sugang = dict(python="kim", db='kang', cpp='sung')
# print(sugang)
# sugang['datastructure'] = 'kim' # add
# print(sugang)
# sugang['datastructure'] = 'park' # overwrite
#
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource', 'not exist')) # 해당 키가 없으면 default로는 None을 리턴한다

# 2.
# sugang = dict(python="kim", db='kang', cpp='sung')
# for subject, professor in sugang.items():
#     print(f'{subject} 과목 담당교수는 {professor}입니다.') # 단 이 순서는 보장된 게 아니다.
#
# for k in sugang.keys():
#     print(k)
# for k in sugang:
#     print(k)    # 둘이 동일한 출력. default가 키 출력이라고 보면 됨
#
# for v in sugang.values():
#     print(v)

# 3. 주류 종류에 따라 안주 추전하는프로그램 : 딕셔너리가 제일 편해보임.

import random
drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}
# 입력을 받는 게 드링크

# del drinks_foods["위스키"]
# drinks_foods["사케"] = "연어회"
# japan_drinks_foods = {"사케": "연어회", "위스키": "낙곱새",} # 중복키 "위스키"
# drinks_foods.update(japan_drinks_foods)
drinks_foods_keys = list(drinks_foods)
print(drinks_foods)
# print(drinks_foods.pop("고량주"))
print(drinks_foods_keys.remove("위스키"))
print(drinks_foods)


while True:
    menu = input(f'다음 주류 중에 고르세요 \n1) {drinks_foods_keys[0]} 2) {drinks_foods_keys[1]} 3) {drinks_foods_keys[2]} 4) {drinks_foods_keys[3]} 5) {drinks_foods_keys[4]} 6) 랜덤 7) 종료 : ')
    #value는 당장 안 쓰고 키값만 필요하니 list로 가져와보자
    if menu == '1': # 1이 문자열임에 주의하자
         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]}\n')
    elif menu == '2':
         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]}\n')
    elif menu == '3':
         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]}\n')
    elif menu == '4':
         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]}\n')
    elif menu == '5':
         print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]}\n')
    elif menu == '6':
         random_drink = random.choice(drinks_foods_keys)
         print(f'오늘은 {random.choice(drinks_foods_keys)}!')
         print(f'{random_drink}에 어울리는 안주는 {random_drink}\n')
    elif menu == '7':
         print(f'다음에 또 오세요')
         break


# 24 01 17 수 Day4 과제
# set은 설명은 못했으나 key와 value 같은 dict라고 보면 된다.
# 책 예제 205p 8.1 ~ 8.10 / 딕셔너리 컴프리헨션은 예습해서 하자.