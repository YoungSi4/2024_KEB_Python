# Pokemon Project

# class
# 최초에 생성할 때 디폴트 네임 + 해당 포켓몬의 타입을 적어줘야함
class attack_skill():
    pass

class Human():
    def __init__(self, name, partner):
        self.name = name
        self.partner = partner # 보유한 파트너 포켓몬


class Pokemon():
    def __init__(self, name, type, hp, atk, defence):
    # text
        self.name = name
        self.type = (type,)

    # basic numeric status
        self.hp
        self.atk
        self.defence

    # act
    def attack(self, target):
        print(f'{self}(이)가 {target.name}을(를) 공격했다!')
        # 데미지 계산 및 적용 스탭 추가할 예정


# # 포켓몬 리스트

class Piplup(Pokemon):
    def __init__(self):
        super.__init__("펭도리", "물", 60, 61, 56)

class Bullbasuar(Pokemon):
    def __init__(self):
        super.__init__("이상해씨", "풀", 45, 68, 70)

class Torchic(Pokemon):
    def __init__(self):
        super.__init__("아차모", "불", 45, 75, 40)

class Alakazam(Pokemon):
    def __init__(self):
        super.__init__("후딘", "에스퍼", 55, 175, 65)

class Gyaradose(Pokemon):
    def __init__(self):
        super.__init__("갸라도스", "물", 95, 135, 85)






piplup = Piplup()