class Character:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def move(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy

class Player(Character): #Player inherits from Character
    def jump(self):
        self.y=self.y-10 # Move up

class Enemy(Character):#Enemy inherits from Character
    def patrol(self):
        self.move(1,0) #Move sideways

mario=Player(50,100)
mario.jump()
print(mario.y)#output 90
goomba = Enemy(200, 150)
goomba.patrol()
print(goomba.x)  # Output: 201
