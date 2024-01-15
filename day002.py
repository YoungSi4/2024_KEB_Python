#str은 immutable한 자료형이다
# univ = "Inha Univ"
# print(univ)
# print(univ[5])
# univ[5] = "U"
# print(univ)

#리스트는 mutable한 자료형이다
# subjects = ['파이썬', "cpp", '리눅스']
# print(subjects)
# print(subjects[2])
# subjects[2] = 'data structure & algorithm' #mutable
# print(subjects)

#Literal Value
#"univ" = "Inha" / Cannot assign to literal

#Variables
# False = 5  예약어라 불가능
# A, a = 1, 2 둘은 다른 변수
# 0tset 숫자로 시작은 불가능
# _0test 언더바로는 시작할 수 있다

#Assignment(할당)
# y = x + 12
# x에 아무 것도 할당을 안하면 작동을 안 한다...
# x에는 쓰레기값이 들어있을수도 있다. 초기화가 필요하다.

#변수는 이름이지 장소가 아니다
# a=7
# print(a) = >> 7
# b = a >> b의 값이 7?...
# 아니다. b는 a가 가지고 있는 주소를 받아서 똑같이 가리킬 뿐이다

#자료형 알아보기
# print(type(3.14))
# >> float
# print(type(3.14) == float)
# >> True
# print(isinstance(3.14, float))
# >> True
#print(isinstance("아", float))
# >> False
# 궁금한 것. 노션에 적어둠.

# 주의할 점
# a = [2, 4, 6]
# b = a
# print(b)
# >> [2, 4, 6]
#
# a[0] = 99
# print(a)
# >> [99, 4, 6]
# print(b)
# >> [99, 4, 6] ** 참조의 개념이기 떄문이다!!

#숫자형 자료
# a = 1,000,000
# print(type(a)) # >> <class 'tuple'>
# 튜플로 인식한다. 따라서 언더바를 쓰자

# a = 1_000_000
# print(type(a)) # >> <class 'int'>

base_number = int(input('input base number: '))
exponent_number = int(input('input exponent number: '))
print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과값은 {base_number ** exponent_number}')