import random


class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power

    def normal_attack(self, monster):
        attack_power = random.randint(self.power-2, self.power+2)
        monster.hp -= attack_power
        print(f"{self.name}의 일반공격! {monster.name}에게 {attack_power}의 데미지를 입혔습니다.")

    def magic_attack(self, monster):
        if self.mp < 5:
            print("마나가 부족합니다.")
            return
        attack_power = random.randint(self.power, self.power+10)
        monster.hp -= attack_power
        self.mp -= 5
        print(f"{self.name}의 마법공격! {monster.name}에게 {attack_power}의 데미지를 입혔습니다.")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def normal_attack(self, player):
        attack_power = random.randint(self.power-2, self.power+2)
        player.hp -= attack_power
        print(f"{self.name}의 일반공격! {player.name}에게 {attack_power}의 데미지를 입혔습니다.")


def print_status(player, monster):
    print(f"{player.name} (HP: {player.hp}, MP: {player.mp}) vs {monster.name} (HP: {monster.hp})")


print("=== 플레이어 생성 ===")
player_name = input("플레이어 이름을 입력하세요: ")
player_hp = 50
player_mp = 20
player_power = 10
player = Player(player_name, player_hp, player_mp, player_power)

print("\n=== 몬스터 생성 ===")
monsters = [
    Monster("슬라임", 30, 8),
    Monster("고블린", 40, 12),
    Monster("오크", 50, 15),
    Monster("드래곤", 80, 20)
]
monster = random.choice(monsters)
print(f"{monster.name}이(가) 나타났습니다!\n")

print("=== 전투 ===")
while True:
    print_status(player, monster)
    player_action = input("공격 방법을 선택하세요 (1: 일반공격, 2: 마법공격): ")
    if player_action == "1":
        player.normal_attack(monster)
    elif player_action == "2":
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 선택하세요.")
        continue

    if monster.hp <= 0:
        print(f"\n{monster.name}을(를) 물리쳤습니다!")
        print(f"{player.name}의 승리!")
        break

    monster.normal_attack(player)
    if player.hp <= 0:
        print(f"\n{player.name}이(가) 쓰러졌습니다...")
        print(f"{monster.name}의 승리!")
        break

print("\n=== 종료 ===")
