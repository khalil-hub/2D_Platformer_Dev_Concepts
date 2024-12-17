class Player:
    def _init__(self, name, x, y):
        self.name=name
        self.x=x
        self.y=y
    
    def move(self, dx, dy):
        self.x=self.x+dx
        self.y=self.y+dy
        