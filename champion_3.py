class Champion:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.cure = 15
        self.speed = 300
        self.attack_power = 10
        self.depend_power = 10

    def cham_detail_info(self, hp, cure, speed, attack_power, depend_power):
        print(f"-----------------현재 lux의 {slef.naem} 정보-----------------")
        print(f"체력 : {slef.hp}\n, 회복 : {slef.cure}\n, 속도 : {slef.speed}\n, 공격력 : {slef.attack_power}\n, 방어력 : {slef.depend_power}")

class Item(Champion):
    def __init__(self, names, item_name):
        self.name = name
        self.item_name = item_name
        hp = 1000
        cure = 15
        speed = 300
        attack_power = 10
        depend_power = 10

    def which_item(self, item_name):
        print(f"-----------------현재 lux의 {slef.naem} 정보-----------------")
        print(f"체력 : {slef.hp}\n, 회복 : {slef.cure}\n, 속도 : {slef.speed}\n, 공격력 : {slef.attack_power}\n, 방어력 : {slef.depend_power}")
