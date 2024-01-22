# Pokemon Project

import random
import sys

# class
# 최초에 생성할 때 디폴트 네임 + 해당 포켓몬의 타입을 적어줘야함
class Attack_skill():
    def __init__(self, name, power, accuracy, _type_):
        self.skill_name = name
        self.power = power
        self.accuracy = accuracy
        self._type_ = _type_

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

class bubble_beam(Attack_skill):
    def __init__(self):
        super().__init__("거품광선", 65, 100, "물")

class flame_wheel(Attack_skill):
    def __init__(self):
        super().__init__("화염자동차", 60, 100, "불")

class masiclal_leaves(Attack_skill):
    def __init__(self):
        super().__init__("매지컬리프", 60, 100, "풀")


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

def type_chart(my_type, target_type, skill_type) -> float: # 타입상성, 자속보정 여부 반환
    type_adv, type_effect = 1.0, 1.0

    if my_type == skill_type:
        type_adv = 1.5

    if skill_type == "물":
        if target_type == "불":
            type_effect = 2.0
        elif target_type == "물" or "풀":
            type_effect = 0.5
        else:
            type_effect = 1.0

    if skill_type == "불":
        if target_type == "풀":
            type_effect = 2.0
        elif target_type == "불" or "물":
            type_effect = 1.0
        else:
            type_effect = 0.5

    if skill_type == "풀":
        if target_type == "물":
            type_effect = 2.0
        elif target_type == "풀" or "물":
            type_effect = 0.5
        else:
            type_effect = 1.0

    return type_effect * type_adv

class Pokemon():
    def __init__(self, name, _type_, hp, atk, defence, skills):
    # text
        self.name = name
        self._type_ = _type_
        self.skill = skills

    # basic numeric status
        self.max_hp = hp
        self.current_hp = hp
        self.atk = atk
        self.defence = defence

    # act
    def attack(self, target, skill):
        # (데미지 = (위력 × 공격 × (레벨 × [[급소]] × 2 ÷ 5 + 2 ) ÷ 방어 ÷ 50 + 2 ) × [[자속 보정]] × 타입상성1)
        damage = int((skill.power * self.atk * (10 * 2 / 5 + 2) / target.defence / 50 + 2 )* type_chart(self._type_, target._type_, skill._type_))
        target.current_hp -= damage


# # 포켓몬 리스트
class Piplup(Pokemon): # 물
    def __init__(self):
        super().__init__("펭도리", "물", 53, 51, 56, [tackle(), None, None, None])

class Bullbasuar(Pokemon): # 풀
    def __init__(self):
        super().__init__("이상해씨", "풀", 45, 65, 49, [tackle(), None, None, None])

class Torchic(Pokemon): # 불
    def __init__(self):
        super().__init__("아차모", "불", 45, 60, 50, [tackle(), None, None, None])

class Alakazam(Pokemon):    # 빌런 보스 # 에스퍼
    def __init__(self):
        super().__init__("후딘", "에스퍼", 55, 75, 30, [tackle(), None, None, None])

class Gyaradose(Pokemon):   # 체육관 관장 # 물
    def __init__(self):
        super().__init__("갸라도스", "물", 95, 60, 30, [tackle(), None, None, None])

def pokemon_center(pokemon):
    pokemon.current_hp = pokemon.max_hp

def skill_select(pokemon, selected_num):
    return pokemon.skill[selected_num - 1]

def display_skill(pokemon):
    str = ""
    for i in range(0, 4):
        if pokemon.skill[i] is None:
            str += f"{i + 1}) [---] "
            continue
        str += f"{i + 1}) [{pokemon.skill[i].skill_name}] "
    print(str, end=' ')

def display_status(pokemon):
    print(f"{pokemon.name}: {pokemon.current_hp}/{pokemon.max_hp}", end=' ')

def battle(person1, person2):
    isBattle = True
    input(f"{person2.name}(이)가 승부를 걸어왔다!")
    input(f"{person2.name}: 가랏! {person2.partner.name}!")
    input(f"당신은 {person1.partner.name}(을)를 내보냈다!")

    while isBattle == True:
        select = 0
        display_status(person1.partner)
        select = int(input(f"무엇을 할까? 1) 싸운다 2) 도망간다: "))

        if select == 1: # 1) 싸운다
            #select_skill = 0
            #select_skill = int((input(f"1) {person1.partner.skill[0].skill_name} 2) {person1.partner.skill[1].skill_name} 3) {person1.partner.skill[2].skill_name} 4){person1.partner.skill[0].skill_name} 5) 뒤로가기: ")))
            display_skill(person1.partner)
            select_skill = int(input("5) 뒤로가기: "))
            if 4 < select_skill:
                continue
            else:
                selected_skill = skill_select(person1.partner, select_skill) # 기술 선택만 수행
                person1.partner.attack(person2.partner, selected_skill)
                print(f'{person1.partner.name}의 {selected_skill.skill_name}!')
                display_status(person2.partner)
                print()

                if person2.partner.current_hp <= 0:
                    input(f"{person2.partner.name}(이)가 쓰려졌다!")
                    input(f"당신은 전투에서 승리했다!")
                    break
                # 우리 포켓몬 공격 턴 종료 시점(적 공격 시작 시점)
                selected_skill = None
                while selected_skill is None:
                    selected_skill = person2.partner.skill[random.randint(0, 3)]
                person2.partner.attack(person1.partner, selected_skill)
                print(f'{person2.partner.name}의 {selected_skill.skill_name}!')
                display_status(person1.partner)
                print()
                if person1.partner.current_hp <= 0:
                    input(f"{person1.partner.name}(이)가 쓰러졌다!")
                    input("당신은 전투에서 패배했다!")
                    input("눈앞이 깜깜해졌다...")
                    input("당신은 패배했습니다. 게임을 종료합니다.")
                    sys.exit(0) # 바로 실행을 종료시키는 명령어

        if select == 2: # 2) 도망친다
            input("승부 중에 등을 보일 순 없어!")
            continue

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
    elif Start_select == 2:
        Yes_or_No = int(input("'팽도리' 이 아이로 하시겠습니까? 1) 네 2) 아니오 : "))
        if Yes_or_No == 1:
            hero.partner = Piplup()
            rival.partner = Bullbasuar()
            break
        if Yes_or_No == 0:
            continue
    elif Start_select == 3:
        Yes_or_No = int(input("'이상해씨' 이 아이로 하시겠습니까? 1) 네 2) 아니오 : "))
        if Yes_or_No == 1:
            hero.partner = Bullbasuar()
            rival.partner = Torchic()
            break
        if Yes_or_No == 0:
            continue
    else:
        continue

# 선택 이후
input(f"{rival.name}: 넌 {hero.partner.name}을 골랐구나!")
input(f"{rival.name}: 그럼 난 {rival.partner.name}으로 해야지!")
input(f"{rival.name}: 이제 포켓몬도 생겼으니 나랑 승부다!")
battle(hero, rival)
input(f"{rival.name}: 크윽 지다니...")
input(f"{rival.name}: 너 정말 강하구나!")
input(f"{rival.name}(은)는 조금 분해보이는 모습으로 떠났다.")
pokemon_center(hero.partner)
input(f"포켓몬이 전부 회복됐습니다.")
input(f"당신의 {hero.partner.name}(은)는 새로운 기술을 배웠다!")
if isinstance(hero.partner, Piplup):
    hero.partner.skill[1] = bubble_beam()
elif isinstance(hero.partner, Bullbasuar):
    hero.partner.skill[1] = masiclal_leaves()
else:
    hero.partner.skill[1] = flame_wheel()
input(f"이제 {hero.partner.name}(은)는 {hero.partner.skill[1].skill_name}(을)를 사용할 수 있게 됐다!")
input("당신의 여정은 계속된다.")
input("다음은 포켓몬 체육관이다!")
input(f"{gymmm.name}: 어서와라 도전자! 있는 힘껏 상대해주마!")
gymmm.partner = gyaradose_mac
battle(hero,gymmm)
input(f"{gymmm.name}: 크으윽!!! 정말 있는 힘껏 들이받아버리다니!!!")
input(f"{gymmm.name}: 정말 멋진 승부였다!")
input(f"{gymmm.name}: 이건 내가 자네에게 주는 강함의 증거야")
input(f"당신은 체육관뱃지를 획득했다!")
input(f"{gymmm.name}: 자 이제 다음으로 가거라!")
input(f"당신은 체육관을 빠져나왔다.")
input("이제 막 첫 뱃지를 얻었을 뿐, 아직 남은 여정은 길다!")
input(f"당신의 모험은 이제 막 시작됐을 뿐이다!")
input(" - 체험판 종료 - ")
