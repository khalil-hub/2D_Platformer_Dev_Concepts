#Inventory class manages items for any character 
class Inventory:
    def __init__(self):
        self.items = [] #List to store items

    def add_item(self, item):
        #Add item to the inventory
        self.items.append(item)

    def remove_item(self, item):
        #Remove Item from the if it exists inventory
        if item in self.items():
            self.items.remove(item)
    
    def list_items(self):
        #List of all items in inventory
        return self.items
    
    # player class has its own inventory via composition
class Player:
    def __init__(self, name):
        self.name=name
        self.inventory()=Inventory() #Composition: Player has an inventory
        
    def pick_item(self, item):
        self.inventory().add_item(item) #Add item to inventory
        print(f"{self.name}'s Inventory: {item}")
        
    def show_inventory(self):
            #display players inventory
        items=self.inventory.list_items()
        print(f"{self.name}'s Inventory: {items}")
    #Enemy class has its own inventory via composition
class Enemy:
    def __init__(self, name, level):
        self.name=name
        self.level=level
        self.inventory=Inventory()
        
    def drop_loot(self):
            #simulate dropping a random item from inventory 
        if self.inventory.items:
            dropped_item=self.inventory.items.pop()
            print(f"{self.name} dropped {dropped_item}")
            return dropped_item
        else:
            print(f"{self.name} has nothing to drop")
            return None
    #NPC class has its own inventory composition
class NPC():
    def __init__(self, name, role):
        self.name=name
        self.role=role
        self.inventory=Inventory() #Composition: NPC has an inventory

    def trade_item(self, item):
        #simulate trading an item in the NPC inventory
        if item in self.inventory.items:
            self.inventory.remove_item(item)
            print(f"{self.name} traded {item}")
            return item
        else:
            print(f"{self.name}doesnt have {item} to trade")
            return None
            
#Using the classes
#Create a player
player = Player("Mario")
player.pick_item("Mushroom")
player.pick_item("fire flower")
player.show_inventory()
#Create an enemy
enemy=Enemy("Goomba", 1)
enemy.inventory.add_item("Gold Coin")
enemy.inventory.add_item("shell")
enemy.drop_loot()
#create an NPC
npc=NPC("Toad","Merchant")
npc.inventory.add_item("potion")
npc.trade_item("potion")
 #Player interacts with loot from the enemy and trades with the NPC
loot = enemy.drop_loot()  # Goomba drops another item
if loot:
    player.pick_item(loot)

player.show_inventory()  # Display updated inventory