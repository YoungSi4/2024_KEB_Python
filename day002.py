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

# ----------------------------------------------------------------------------

# 숫자형 자료
# a = 1,000,000
# print(type(a)) # >> <class 'tuple'>
# 튜플로 인식한다. 따라서 언더바를 쓰자
# a = 1_000_000
# print(type(a)) # >> <class 'int'>

# 연산과 출력
# base_number = int(input('input base number: '))
# exponent_number = int(input('input exponent number: '))
# int 변환을 안 해주면, input 함수는 기본적으로 str이기 때문에 **로 계산할 수 없다

# pow 함수로 해보기
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과값은 {pow(base_number, exponent_number)}')

# 출력
# f-stirng fuction은 파이썬 3.6부터 지원한다. 간편하게 print에서 출력 가능하다. 가장 최신.
# print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과값은 {base_number ** exponent_number}')

# format function이 이전에 같은 기능을 수행했다.
# print('밑은 {0}, 지수는 {1}, 결과 값은 {2}'.format(base_number, exponent_number, pow(base_number, exponent_number)))
# 이전 버전의 불편한 함수이긴 하지만, 호환성을 생각하면 계속 사용하게 된다.

# c like / ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 오랜만이네
# print('밑은 %d, 지수는 %d, 결과 값은 %d' % (base_number, exponent_number, pow(base_number, exponent_number)))

# divmod 사용해보기
# 일단 기본만
# first_number = int(input("First number: "))
# second_number = int(input("Second number: "))

# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'목은 {quotient} 나머지는 {remainder}')

# divmod 함수 사용하기 // 연산기호가 미세하게 더 빠르다고 하다. 함수를 불러와서 그럼. 근데 그리 큰 차이는 X
# print(f'목은 {divmod(first_number, second_number)[0]} 나머지는 {divmod(first_number, second_number)[1]}')
# divmod가 (몫, 나머지)이기 떄문에 []를 이용해서 방을 지정해준다

# ----------------------------------------------------------------------------

# 진법 써보기
# dec = 65
# octal = 0o101
# hecadecimal = 0x41
# binary = 0b01000001
# print(dec, octal, hecadecimal, binary)
# print(chr(dec), chr(octal), chr(hecadecimal), chr(binary))
# print(ord('B'), ord("Z"), ord('a'), ord('2')) # 66, 90, 97, 50

# ----------------------------------------------------------------------------

# # (화씨°F − 32) × 5/9 = 0°C
#fahrenheit = float(input("화씨 온도: "))
#print(f'화씨온도: {fahrenheit}F, 섭씨: {(fahrenheit - 32) * 5 / 9}C')

# ----------------------------------------------------------------------------

# if문 활용 > 반복문 활용 > 모듈 > 클래스 객체

# menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit  3) Quit Program: ")
#
# if menu == '1':
#     fahrenheit = float(input('Input Fahenheit : '))
#     print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')
# elif menu == '2':
#     celsius = float(input('Input Celsius: '))
#     print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9/5) + 32):.4f}F')
# else:
#     print('Terminate Program. Goodnight.')

# ----------------------------------------------------------------------------

# # 소수점 넷째 자리까지만 나오도록 처리
# print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')

# 진수 변환 방법 추가
# print(int('11', 16))
# print(int('1A', 16))

# ----------------------------------------------------------------------------

# 값의 존재 여부
# temp = []
# if temp:
#     print("원소가 존재")
# else:
#     print("비어있다") # >> 비어있다 출력
#                      # temp[0]이면 >> 원소가 존재

# ----------------------------------------------------------------------------

# 모음 자음 탐색하기

letter = input('put any alpabet letter you want: ')

# 방법 1, set 사용
vowels = {'a', 'e', 'i', 'o', 'u'} # 이건 key 형식의 시퀀스 자료형

# 방법2, str 사용
# vowels = 'aeiou'

if letter in vowels: # in 구문을 이용해서 파이썬다운 코드를 짤 수 있다.
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')

