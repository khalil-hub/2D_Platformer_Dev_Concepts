class Player:
    def __init__(self, name, x, y, health=100):  # health has a default value
        self.name = name
        self.x = x
        self.y = y
        self.health = health  # Initializes health

class Enemy(Player):
    def __init__(self, name, x, y, damage):
        super().__init__(name, x, y)  # Calls Player's __init__ without explicitly mentioning health
        self.damage = damage  # Unique to Enemy
enemy = Enemy("Goomba", 10, 20, 5)
print(enemy.health)  # Output: 100