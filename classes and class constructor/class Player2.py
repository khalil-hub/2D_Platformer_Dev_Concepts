class Player2:
    def __init__(self, x, y):
        self.x_position=x
        self.y_position=y
        self.speed=5

    def move(self, direction):
        if direction=="left":
            self.x_position==self.x_position-self.speed
        elif direction=="right":
            self.x_position==self.x_position+self.speed

    def jump(self):
        self.y_position=self.y_position-10
