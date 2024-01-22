# # 간단하게 매직 메소드 써보기.
class FlyMixin:
    def fly(self):
        return f'{self.__name}의 공중날기!'


class SurfMixin:
    def Surf(self):
        return f"{self.__name}의 파도타기!"  # 이건 Mixin 설명을 위해 사용했음


class Pokemon:
    def __init__(self, name, hp):
        self.__name = name  # 진짜 이름
        self.hp = hp

    def attack(self):
        print("공격")

    @property
    def get_name(self):
        print("getter 내부")
        return self.name

    @get_name.setter
    def set_name(self, new_name):
        print("setter 내부")
        self.name = new_name

    # name = property(get_name, set_name)
    def __str__(self):
        return self.__name + "입니다."

    def __add__(self, target):
        # return self.__name + " + " + target.__name
        return f'두 포켓몬의 체력 합은 {self.hp + target.hp}입니다.'


class Charizard(Pokemon, FlyMixin):
    pass


class Gyarados(Pokemon, SurfMixin, FlyMixin):
    pass


g1 = Gyarados("갸라도스", 100)
ch1 = Charizard("리자몽", 120)
print(g1) # __str__ used
print(ch1)
print(g1+ch1) # 클래스끼리 더할 수 있나...?