from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage
    #hybrid override
    def take_damage(self, damage):
        damage = damage * .25
        super().take_damage(damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        return super().take_damage(damage)