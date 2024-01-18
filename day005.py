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

# 함수
# Prime number with funcrtion
def isprime(n) -> bool: # 리턴값 명시. 없어도 되는데 있으면 더 좋다.
    """
    매개변수로 넘겨 받은 수가 소수인지 여부를 boolean type으로 반환
    :param n: 소수인지 판정할 매개변수
    :return: 소수 True, 아니면 False
    """
    pass
    if n < 2:
        return False # False를 반환하고 함수를 즉시 종료한다.

    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True # True를 반환하고 함수를 즉시 종료한다.
# 이전에 만들어둔 소수 찾는 코드

while True:
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit 3) Prime number 4) Prime number range 5) Quit Program: ")

    if menu == '1':
        fahrenheit = float(input('Input Fahenheit : '))
        print(f'화씨온도: {fahrenheit}F, 섭씨: {((fahrenheit - 32) * 5 / 9):.4f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius: '))
        print(f'Celsius: {celsius}C, Fahrenheit: {((celsius * 9/5) + 32):.4f}F')

    elif menu == '3':
        number = int(input("Input Number : "))
        if isprime(number):
            print(f"{number} is prime number")
        else:
            print(f"{number} is not prime number")

    elif menu == '4':
        numbers = input("Input First Second Number : ").split() # 숫자 하나만 입력하는 경우?
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1   # 입력부터 순서 바꾸는 것까지, 코드라인 줄이고 더 가독성 좋게.

        for number in range(n1, n2 + 1):
            if isprime(number):
                print(number, end=' ')
        print() # print 자체에 줄바꿈을 가지고 있다

    elif menu == '5':
        print('Terminate Program. Goodnight.')
        break
    else:
        pass