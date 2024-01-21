# Pokemon Project

# class
# 최초에 생성할 때 디폴트 네임 + 해당 포켓몬의 타입을 적어줘야함
class Attack_skill():
    def __init__(self, name, damage, miss, type):
        self.skill_name = name
        self.damage = damage
        self.miss = miss
        self.type = type

class tackle(Attack_skill):

    def __init__(self):
        super().__init__("몸통박치기", 40, 100, "노말")

class water_gun(Attack_skill):
    def __init__(self):
        super().__init__("물대포", 40, 100, "물")

class small_fire(Attack_skill):
    def __init__(self):
        super().__init__("불꽃셰레", 40, 100, "불")

class whip_sweep(Attack_skill):
    def __init__(self):
        super().__init__("덩쿨채찍", 40, 100, "풀")



class Human():
    def __init__(self, name, partner):
        self.name = name
        self.partner = partner # 보유한 파트너 포켓몬

class Hero(Human):
    def __init__(self):
        super().__init__("이름", "아직없음")

class Rival(Human):
    def __init__(self):
        super().__init__("용식", "아직없음")

class Gym_Master(Human):
    def __init__(self):
        super().__init__("맥실러", "아직없음")

class Villain(Human):
    def __init__(self):
        super().__init__("연수", "아직없음")

class Pokemon():
    def __init__(self, name, type, hp, atk, defence, skills):
    # text
        self.name = name
        self.type = (type,)
        self.skill = skills

    # basic numeric status
        self.max_hp = hp
        self.current_hp = hp
        self.atk = atk
        self.defence = defence

    # act
    def attack(self, target, skill):
        print(f'{self}(이)가 {target.name}에게 {skill.name}!')
        # 데미지 계산 및 적용 스탭 추가할 예정


# # 포켓몬 리스트
class Piplup(Pokemon): # 물
    def __init__(self):
        super().__init__("펭도리", "물", 120, 170, 140, [tackle, None, None, None])

class Bullbasuar(Pokemon): # 풀
    def __init__(self):
        super().__init__("이상해씨", "풀", 90, 190, 70, [tackle, None, None, None])

class Torchic(Pokemon): # 불
    def __init__(self):
        super().__init__("아차모", "불", 75, 200, 80, [tackle, None, None, None])

class Alakazam(Pokemon):    # 빌런 보스 # 에스퍼
    def __init__(self):
        super().__init__("후딘", "에스퍼", 55, 175, 65, [tackle, None, None, None])

class Gyaradose(Pokemon):   # 체육관 관장 # 물
    def __init__(self):
        super().__init__("갸라도스", "물", 95, 135, 85, [tackle, None, None, None])

def pokemon_center():
    pass

def battle():
    pass

# 객체 생성
gyaradose_mac = Gyaradose()
alakazam_yeon = Alakazam()
hero = Hero()
rival = Rival()
gymmm = Gym_Master()
villain = Villain()

# 게임 내용 text

# intro
input("박사: 흐음")
input("박사: 잘 왔다!")
input("박사: 포켓몬스터의 세계에 온 것을 환영한다!")
input("박사: 내 이름은 마박사!")
input("박사: 모두가 포켓몬 박사님이라 부르고 있단다.")
input("박사: 이 세계에는")
input("박사: 포켓몬스터")
input("박사: 줄여서 '포켓몬'이라 불리는")
input("박사: 신기한 생명체가")
input("박사: 도처에 살고 있다!")
input("박사: 그건 그렇고 이제 슬슬")
input("박사: 자네에 대해 알아보도록 하지!")
hero.name = input("마박사: 자네의 이름은? : ")
input("흐음...")
input(f"{hero.name}라고 하는가!")
input("좋은 이름이구나!")
input("자네는 분명 친구가 있었지?")
rival.name = input("그 친구의 이름도 가르쳐다오! : ")
input(f"{rival.name}이로군")
input(f"{hero.name}!!")
input("이제부터 너만의 이야기가 시작된다!")
input("행운을 빌지!")

# select starting pokemon
input("쾅!")
input("???: 약속이 언제인데 아직도 안 나와!")
input(f"{rival.name}: 늦으면 벌금 500만원이니까!")
input("쾅!")
input("당신은 나갈 채비를 한다")
input(f"{rival.name}: 늦었어!! 빨리 가자!!")
input(f"당신과 {rival.name}은 박사님의 연구실로 향한다.")
input("연구실 문을 열고 들어간다.")
input("박사: 왔는가!")
input("박사: 자, 이 친구들은 내가 요즘 연구하고 있는 아이들이라네")
input("박사: 밖은 위험하니 데려가도록 하게나.")

# 스타팅 포켓몬 선택
while True:
    Start_select = 0
    Yes_or_No = None
    Start_select = int(input("포켓몬을 골라주세요 1) 아차모 2) 팽도리 3) 이상해씨 : "))
    if Start_select == 1:
        Yes_or_No = int(input("'아차모' 이 아이로 하시겠습니까? 1) 네 2) 아니오 : "))
        if Yes_or_No == 1:
            hero.partner = Torchic()
            rival.partner = Piplup()
            break
        if Yes_or_No == 0:
            continue
    if Start_select == 2:
        Yes_or_No = int(input("'팽도리' 이 아이로 하시겠습니까? 1) 네 2) 아니오 : "))
        if Yes_or_No == 1:
            hero.partner = Bullbasuar()
            rival.partner = Torchic()
            break
        if Yes_or_No == 0:
            continue
    if Start_select == 3:
        Yes_or_No = int(input("'이상해씨' 이 아이로 하시겠습니까? 1) 네 2) 아니오 : "))
        if Yes_or_No == 1:
            hero.partner = Piplup()
            rival.partner = Bullbasuar()
            break
        if Yes_or_No == 0:
            continue

# 선택 이후
input(f"{rival.name}: 넌 {hero.partner.name}을 골랐구나!")
input(f"{rival.name}: 그럼 난 {rival.partner.name}으로 해야지!")
