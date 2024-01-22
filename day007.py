
# class Pokemon:
#     def __init__(self, name, hp, fly):
#         self.__name = name  # 진짜 이름
#         self.hp = hp
#         self.fly = fly # aggregation (has-a)
#
#     def attack(self):
#         print("공격")
#
#     @property
#     def get_name(self):
#         print("getter 내부")
#         return self.name
#
#     @get_name.setter
#     def set_name(self, new_name):
#         print("setter 내부")
#         self.name = new_name
#
#     # name = property(get_name, set_name)
#     def __str__(self):
#         return self.__name + "입니다."
#
#     def __add__(self, target):
#         # return self.__name + " + " + target.__name
#         return f'두 포켓몬의 체력 합은 {self.hp + target.hp}입니다.'
#
# class Fly: # 리스코프 치환의 법칙
#     def fly(self):
#         return f'공중날기!'
#
# class JetPack(Fly):
#     def fly(self):
#         return "10분간 날 수 있습니다"
#
# class Nofly(Fly):
#     def fly(self):
#         return f'하늘을 못 날아요'
#
# class FlyWithWings(Fly):
#     def fly(self):
#         return f"날개로 하늘을 날아갑니다"
#
# class Pikachu:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         self.fly_behavior = Nofly() # composition
#
#
# p1 = Pikachu("피카츄", 100)
# print(p1.fly_behavior.fly())

# import mymath
# Prime number with funcrtion
import mymath as mm

from mymath import * # 모듈 이름을 앞에 안 붙여도 되도록 해주는 형식
while True:
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fehrenheit 3) Prime number 4) Prime number range 5) Quit Program: ")

    if menu == '1':
        fahrenheit = float(input('Input Fahenheit : '))
        print(f'화씨온도: {fahrenheit}F, 섭씨: {(mm.fahrenheit_to_celsius(fahrenheit)):.4f}C')

    elif menu == '2':
        celsius = float(input('Input Celsius: '))
        print(f'Celsius: {celsius}C, Fahrenheit: {(mm.celsius_to_fahrenheit(celsius)):.4f}F')

    elif menu == '3':
        number = int(input("Input Number : "))
        if mm.isprime(number):
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
            if mm.isprime(number):
                print(number, end=' ')
        print() # print 자체에 줄바꿈을 가지고 있다

    elif menu == '5':
        print('Terminate Program. Goodnight.')
        break
    else:
        pass