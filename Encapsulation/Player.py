class Player:
    def __init__(self, health):
        self.__health = health #private attribute
    def take_damage(self, amount):
        if amount>0:
            self.__health=self.__health-amount
        if self.__health<=0:
            self.die()
    def get_health(self): #method to access health
        return self.__health
    def die(self):
        print("player has died")
player = Player(100)
#print(player.__health)#Error: AttributeError: 'Player' object has no attribute '__health'
print(player.get_health())  # Output: 100
player.take_damage(20)
print(player.get_health())  # Output: 80
