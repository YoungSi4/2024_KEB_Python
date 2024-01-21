# 재귀함수 예제.
# 팩토리얼. 재귀함수 아닌 for를 사용한 모습
# def factorial_repetition(n) -> int:
#     """
#     for를 사용한 팩토리얼 함수
#     :param n: int
#     :return: 팩토리얼 값, int
#     """
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#     return result
#
# # 재귀함수를 쓴 모습. 할당이 없다. 즉, 값이 바뀔 여지가 없고, side effect가 없다. 보장되어있다.
# # 단 속도가 다소 느릴 수 있다. 계속 step 메모리를 쓰고 왔다갔다 해야한다.
# # 반복문은 속도가 압도적으로 빠르다. cpu 바로 옆 accumulator에서 계산해서 바로바로 꺼내온다.
# # 재귀는 메모리 주소 찾고 가서 계산해오고 메모리 주소 찾고 거슬러 올라오고 등등등... 숫자가 클수록 오래걸림.
#
# def factorial_recursion(n):
#     """
#     재귀함수를 사용한 팩토리얼 함수
#     :param n: 정수, int
#     :return: function, 최종: int
#     """
#     if n == 1:
#         return n
#     else:
#         return n * factorial_recursion(n-1) # 이게 재귀함수.
#
# number = int(input("Number: "))
# print(factorial_repetition(number))
# print(factorial_recursion(number))
# print(globals())

# 앞으로 피보나치에서도 쓸 예정임. 반복으로도 할 수 있지만, side effect의 위험, 이전 값을 상당히 기억해야함

# # 예외처리 + 랜덤 모듈을 활용한
#
# import random
#
# class OopsException(Exception):
#     pass
#
# numbers = [random.randint(1,100) for i in range(5)]
# print(numbers)
#
# try:
#     pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
#     # 4 이상의 값을 넣으면 IndexError: list index out of range
#     # 가이드라인을 주니까 조금 더 낫긴한데, 여전히 예외처리가 필요하다.
#     print(numbers[pick])
#     # print(4/0) # zeroDivisionError를 보기 위한 코드
#     raise OopsException("Oops!") # 여기서 에러를 발생시킴. 저 밑에 Exception의 err가 Oops!를 받는다.
#
# except IndexError as err :  # 근데 그냥 except만 써두면 에러가 아닌 것도 잡는다.
#                     # 예시를 들면, 병원 갔더니 '아프시네요'라고 듣고 온 셈. 그래서 병명이 뭐에요...
#                     # 그래서 IndexError라고 지정해서 처리해준다.
#                     # as err : 시스템이 던지는 메세지를 변수 err 받아서 예외처리에 출력한 것.
#     print(f"Wrong index number\nReason: {err}")
#
# except ValueError as err :
#     print(f"Please input number only\n{err}")
#
# except ZeroDivisionError as err : # 위에 print(4/0) 떄문에 발생하는 에러. 직접 실행시키고
#                                   # 시스템이 던지는 메세지를 가져오는 편
#     print(f"Dennomenator cannot be 'Zero' : {err}")
#
# except OopsException as err:
#     print(f"OOoooops OOOoopps {err}")
#
# except Exception as err : # 주의 : 얘는 가장 아래에 배치해야한다. 위로 올라가면 얘가 모든 에러를 먼저 잡아버린다.
#                           # 어떤 언어들은 Exception이 가장 위로 가면 아예 실행을 못하게 에러를 던진다.
#     print(f"Error occurs: {err}")
#
# else:
#     print(f"Program is running")

# # 데코 추가 설명
#
# def desc(func):
#     def wrapper():
#         print("study")
#         func()
#     return wrapper
#
# # 방법 1.
#
# # def something():
# #     print("do something")
# #
# # s = desc(something) # 할당할 객체 = 데코레이터(데코 입힐 함수())
# # s() # 할당한 객체(함수)를 실행시킴
#
# # 방법 2.
# # 혹은 위에 @데코레이터 를 붙이고 something()을 호출하면 된다.
#
# @desc
# def something():
#     print("do something")
#
# s = desc(something)
# s()
# print()
# something()


# Class !

# 클래스 선언

# class Pokemon: # 꼭 대문자로 하자. 상속이 아니라면 빈 괄호는 지우자.
#     def __init__(self, name): # 이닛(생성자)에 이름을 던져줘서 만들 수도 있다.
#                               # 이닛은 각 객체가 처음 생성될 때 딱 한 번 호출된다.
#                               # self는 cpp의 this와 같다.
#                               # 태어나는 건 한 번이다. 먹고 자는 건 할 때마다 호출하지만 탄생은 한 번.
#         print(f"포켓몬스터 생성: {name}")
#
# pikachu = Pokemon("피카츄") # name을 str으로 준다.
# squirtle = Pokemon("꼬부기")
# pikachu.name = '피카츄'
# pikachu.rival = squirtle
# print(pikachu)
# print(pikachu.name)
# squirtle.name = "꼬부기"
# print(pikachu.rival.name)
# pikachu.rival.name = "꼬꼬부기"
# print(squirtle.name)


# class Pokemon:
#     def __init__(self, name):
#         self.name = name
#         print(f'포켓몬 생성: {name}')
#
#     def attack(self, target):
#         print(f"{self.name}(이)가 {target.name}을(를) 공격했다!")
#
# pikachu = Pokemon("피카츄")
# squirtle = Pokemon('꼬부기')
# charizard = Pokemon("리자몽")
# charizard.attack(squirtle)

# 상속
# class Pokemon():
#     def __init__(self, name):
#         self.name = name
#
#     def attack(self, target):
#         print(f'{self.name}(이)가 {target.name}을(를) 공격했다!')
#
# class Pikachu(Pokemon):
#     def __init__(self, name, type):
#         super().__init__(name) # 부모클래스를 호출 super(), 부모의 init을 사용ㅇ
#         self.type = type
#
#     def attack(self, target):
#         print(f'{self.name}(이)가 {target.name}에게 10만 볼트!')
#
#     def electric_info(self):
#         print(f"{self.type}타입")
#
# class Squirtle(Pokemon):
#     pass
#
# pikachu_1 = Pikachu("피가죽", '전기')
# sq1 = Squirtle("고북이")
# pikachu_1.electric_info()


# class Animal:
#     def say(self):
#         return "I'm a animal!"
#
# class Horse(Animal):
#     # def say(self):
#     #     return "난 말왕이야"
#     pass
#
# class Donkey(Animal):
#     def say(self):
#         return "당나기"
#     # pass
#
# class Mule(Donkey, Horse):
#     pass
#
# class Hinny(Horse, Donkey):
#     pass
#
# m1 = Mule()
# h1 = Hinny()
# print(m1.say())
# print(h1.say())

# Mixin - 다중 상속을 이용해서 설명

# class FlyMixin:
#     def fly(self):
#         return f'{self.__name}의 공중날기!'
#
# class SurfMixin:
#     def Surf(self):
#         return f"{self.__name}의 파도타기!" # 이건 Mixin 설명을 위해 사용했음
#
# class Pokemon:
#     def __init__(self, hidden_name):
#         self.__name = hidden_name # 진짜 이름
#
#     def attack(self):
#         print("공격")
#
#     @property
#     def get_name(self):
#         print("getter 내부")
#         return self.hidden_name
#
#     @get_name.setter
#     def set_name(self, new_name):
#         print("setter 내부")
#         self.hidden_name = new_name
#
#     # name = property(get_name, set_name)
#
# class Charizard(Pokemon, FlyMixin):
#     pass
#
# class Gyarados(Pokemon, SurfMixin, FlyMixin):
#     pass
#
# g1 = Gyarados("갸라도스")
# ch1 = Charizard("리자몽")
# print(g1.Surf())
# print(g1.fly())
# print(ch1.fly())
# ch1.attack()
# Charizard.attack(ch1)
# Charizard.attack() # 이건 클래스 이름이다. self 자리에는 '객체'가 들어간다.
                   # 이런 형식을 쓰고 싶으면 객체를 줘야한다.

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())

# property
# print(g1.name)
# g1.hidden_name = "잉어킹"
# print(g1.name)
# print(g1.hidden_name)

# property +++
# print(g1.name)
# print(g1.hidden_name)
# # print(g1.__name) # 직접 접근 불가. 에러.
# print(g1._Pokemon__name)


# 과제 (주말과제 !)
#  어... 교재 연습문제는 당연히 해볼 것
#
# 포켓몬스터 게임을 만들어옵시다
# 1. 기획을 해야한다.
#   클래스 설계 : 필드를 만들고 상속관계를 설계해야 한다.
#   어떤 기능이 있어야 하는지
#   텍스트 기반 게임
#   게임을 시작하면 스타팅 포켓몬 정하고, 야생의 포켓몬 등장하고, 라이벌 대결하고
#   스타팅 포켓몬 고름 > 객체 생성해야함
#   상대 포켓몬도 여러 종류 만들어서 랜덤으로 등장
#   상대 포켓몬 등장 > 무엇을 할까? 1) 공격, 2) 도망, 3) 게임종료
#   리스트에 attack_name, attack_damage 2차원으로?
#   도망을 간다면? 레벨을 고려해서. 확률적으로
#
#   생각드는대로 만들어보자.
#   여태 배운 기술을 총동원해서 만들어보자.
#   절대 ! 같은 결과물이 나올 수 없다 !
#   스스로 배운 기술을 써먹기 위해서 열심히 해볼 것.

#   분명 다양한 버그가 생기고 어려울 것임.
#   한 세월 붙잡고 만들어야 할 것임 ㅋㅋㅋ
#   굳이 모든 기능을 억지로 쓸 필요는 없다.
#   자연스럽게 필요한 기능을 활용할 것.

# Mixin 부터 이해를 못해서 다시 읽어보고
# 접근, 프로퍼티, 게터 세터, 유사 private 다 완전히 이해할 것