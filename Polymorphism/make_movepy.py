def make_move(entity):
    entity.move() #works for any object with a move() method

player = Player("Mario", 100)
enemy = Enemy("Goomba", 20)

make_move(player) #Output: Mario is moving
make_move(enemy) #Output: Goomba is moving
