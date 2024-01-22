
class Pokemon:
    def __init__(self, name, hp, fly):
        self.__name = name  # 진짜 이름
        self.hp = hp
        self.fly = fly # aggregation (has-a)

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

class Fly: # 리스코프 치환의 법칙
    def fly(self):
        return f'공중날기!'

class JetPack(Fly):
    def fly(self):
        return "10분간 날 수 있습니다"

class Nofly(Fly):
    def fly(self):
        return f'하늘을 못 날아요'

class FlyWithWings(Fly):
    def fly(self):
        return f"날개로 하늘을 날아갑니다"

class Pikachu:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = Nofly() # composition


p1 = Pikachu("피카츄", 100)
print(p1.fly_behavior.fly())