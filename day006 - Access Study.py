# class Pokemon():
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         print("게더 실행됨")
#         print('이름은', end=' ')
#         return self.hidden_name
#
#     # @name.setter
#     # def name(self, new_name):
#     #     print("세터 실행됨")
#     #     self.hidden_name = new_name
#
#     # name = property(get_name, set_name) # 속성으로 추가하여 property로 우회시킴
#
# class Pikachu(Pokemon):
#     pass
#
# class Eevee(Pokemon):
#     pass
#
#
# pika = Pikachu("노란돼지")
# eve = Eevee("수상할정도로 수상한")
#
# print(pika.__name) # 맹글링
# print(pika.name)
# pika.name = "레드의 피카츄"
# print(pika.name)
#
# print(eve.name)



# # 프로퍼티 이해를 위한 코드

# class Test2:
#     def __init__(self, val):
#         self._val = val
#
#     @property
#     def val(self):
#         print("내부적으로 getter사용")
#         return self._val
#
#     @val.setter
#     def val(self, value):
#         print("내부적으로 setter사용")
#         if not value:
#             raise ValueError("Value Error")
#         self._val = value
#
#     @val.deleter
#     def val(self):
#         del self._val
#
# t2 = Test2("테스트2")
# print(t2.val)
# t2.val = "테스트3"
# print(t2.val)



# 연습문제 279p 배운 것만 하자
# 1, 2, 3, 4(인스턴스 속성?), 5, 6, 8, 9,