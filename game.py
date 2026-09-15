from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Square"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening... \nAs you enter the lights turn on and the crowd is waiting for an epic battle \nAre you ready for the challenge?")

    goblin = Goblin("GreenGoblin")
    goblinTwo = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")
   
    print("But no hero has answered the call... yet.")

    hero = Hero("Spooderman")

    print(f"{hero.name} enters the arena with {hero.health} health.")

    hero_giveDamage = hero.attack()
    goblin.take_damage(hero_giveDamage)
            


if __name__ == "__main__":
    main()
