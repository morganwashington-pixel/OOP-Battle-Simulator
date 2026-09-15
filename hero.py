import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__ (self,name):
        self.name = name 
        self.health = 110
        self.attack_power = 20
        

    def attack(self):
        return random.randint(1,20)

    def take_damage(self, damage):
    # Subtract damage, but do not allow health to fall below 0.
        self.health =  max(0, self.health - damage)

        
    def is_alive(self):
    # Return a Boolean based on this Hero's health.
        if self.health > 0:
            return True 
        else: 
            return False 

