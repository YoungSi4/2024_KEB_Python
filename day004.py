# Assignment 소수 구간 v8.0 수정사항 추가
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

# 튜플
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

# 괄호와 반저멩 주의
# print(type('py',))
# print(type(('py'),))
# print(type(('py',)))
# t9 = ('py',)
# print(type(t9)) # == print(type(('py',)))

# 튜플 간 비교연산이 가능하다
# t10 = 1, 2, 3
# t11 = 1, 2
# print(t10 == t11)
# print(t10 <= t11)
# print(t10 > t11)
#
# # 튜플의 수정이 가능하다
# print(t10 + t11)

t12 = 4.43,
t13 = 3.97, 4.1, 3.27
print(t12 + t13)
print(id(t12))
t12 = t12 + t13
print(t12)
print(id(t12))
