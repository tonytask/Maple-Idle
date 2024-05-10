import pygame
from pygame.locals import *
import random
import json


#Screen Dimensions
width = 1024
height = 768

#List of Monsters
monster_list = ['Snail', 'Blue Snail', 'Shroom', 'Red Snail', 'Slime', 'Orange Mushroom',
                'Ribbon Pig', 'Octopus', 'Bubbling', 'Green Mushroom', 'Horny Mushroom',
                'Evil Eye']

#List of Bosses
boss_list = ['Mano', 'Stumpy']

#Monster Data Table
#0: Level
#1: HP
#2: Attack
#3: EXP
#4: Mesos
#5: Kill Count
monster_table = {'Snail': [1,8,12,3,6,0],
                 'Blue Snail': [2,15,18,4,12,0],
                 'Shroom': [2,20,24,5,12,0],
                 'Red Snail': [5,40,35,8,18,0],
                 'Slime': [6,50,42,10,20,0],
                 'Orange Mushroom': [8,80,52,15,24,0],
                 'Ribbon Pig': [10,120,66,20,30,0],
                 'Octopus': [12,200,76,24,36,0],
                 'Bubbling': [15,240,80,26,36,0],
                 'Green Mushroom': [15,250,82,26,42,0],
                 'Horny Mushroom': [22,300,90,35,54,0],
                 'Evil Eye': [27,720,100,50,72,0]}

boss_table = {'Mano': [20,2000,125,200,200,0],
              'Stumpy': [35,3500,175,350,350,0]}

boss_timer = {'Mano': 0, 'Stumpy': 0}

#Loot Table for Monster
#Number/10000 represents Probability of Item Dropping
drop_table = {'Snail': {25:'Glove Scroll ATT 100%',50: 'Work Gloves',125: 'Green Headband',},
               'Blue Snail': {25: 'Grey Thick Sweat Pants',50: 'Blue One-Lined T-Shirt', 125: 'White Undershirt +1'},
               'Shroom': {25: 'Ice Jeans',40:'Hat Scroll DEF 100%', 125: 'Jean Capris'},
               'Red Snail': {10: 'Wooden Sword +3', 25:'Glove Scroll ATT 10%',80: 'Wooden Sword'},
               'Slime': {25: 'Fork on a Stick', 55: 'Bronze Aroa Boots', 100: 'White Bandana'},
               'Orange Mushroom': {40: 'Bronze Koif', 80: 'White Gomushin', 125: 'Spear'},
               'Ribbon Pig': {25: 'Orange Sporty T-Shirt +2', 110: 'Orange Sporty T-Shirt', 200: 'Work Gloves'},
               'Octopus': {40: 'Brown Corporal',70: 'Brown Corporal Pants', 125: 'Aqua Snowboard'},
               'Bubbling': {10:'Glove Scroll ATT 60%',25: 'Fish Spear +1', 75: 'Fish Spear'},
               'Green Mushroom': {25:'Work Gloves +2',50: 'White Starry Bandana'},
               'Horny Mushroom': {20: 'Iron Burgernet Helm',35:'Warfare Pants', 60: 'Red Whitebottom Shoes'},
               'Evil Eye': {25: 'Maple Sword', 50: 'Maple Cape'},


               #bosses
               'Mano': {100: 'Cutlus', 500: 'Work Gloves +3'},
               'Stumpy': {500: 'Dark Knuckle +2'}}

#Exp Table
exp_to_next_level = {1: 15, 2:34, 3:57, 4:92, 5:135, 6:372, 7:560, 8:840, 9:1242, 10:1144,
                    11:1573,12:2144,13:2800,14:3640,15:4700,16:5893,17:7360,18:9144, 
                    19:11120,20:13477,21:16268,22:19320,23:22880,24:27008,25:31477,
                    26:36600,27:42444,28:48720,29:55813,30:63800}




#List of all droppable items              
               #hat
drop_list = {'Empty': ['Hat', 0,0,0,0,0],
              'Green Headband': ['Hat',0,0,5,7,0],
              'White Bandana': ['Hat',0,0,8,7,0],
              'Bronze Koif': ['Hat',0,0,10,7,0],
              'White Starry Bandana': ['Hat',0,0,15,7,0],
              'Iron Burgernet Helm': ['Hat',0,0,25,7,0],

                #top
                'White Undershirt': ['Top',0,0,3,7,0], 
                'Blue One-Lined T-Shirt': ['Top',0,0,11,7,0],
                'White Undershirt +1': ['Top',0,0,5,0,0], 
                'Orange Sporty T-Shirt': ['Top',0,0,11,7,0], 
                'Orange Sporty T-Shirt +2': ['Top',4,0,11,0,0],
                'Brown Corporal': ['Top',0,0,20,7,0],

                #bottom
                'Blue Jean Shorts': ['Bottom',0,0,2,7,0], 
                'Jean Capris': ['Bottom',0,0,5,7,0],
                'Grey Thick Sweat Pants': ['Bottom',0,0,10,7,0], 
                'Ice Jeans': ['Bottom',0,0,13,7,0], 
                'Brown Corporal Pants': ['Bottom',0,0,16,7,0], 
                'Warfare Pants': ['Bottom',0,0,19,7,0],

                #gloves
                'Work Gloves': ['Gloves',0,0,2,5,0],
                'Work Gloves +1': ['Gloves',0,2,2,0,0], 
                'Work Gloves +2': ['Gloves',0,4,2,0,0],
                'Work Gloves +3': ['Gloves',0,6,2,0,0],
                'Dark Knuckle +2': ['Gloves',3,4,17,0,0],

                #shoes
                'Leather Sandals': ['Shoes',0,0,2,5,0], 
                'White Gomushin': ['Shoes',0,0,4,5,0], 
                'Bronze Aroa Boots': ['Shoes',0,0,7,5,0], 
                'Red Whitebottom Shoes': ['Shoes',0,0,13,5,0],

                #cape
                'Maple Cape': ['Cape',0,0,5,5,0],

                #weapon
                'Sword': ['Weapon',0,17,0,7,0], 
                'Wooden Sword': ['Weapon',0,30,0,7,0], 
                'Wooden Sword +3': ['Weapon',3,36,0,0,0],
                'Aqua Snowboard': ['Weapon',0,30,0,7,0], 
                'Spear': ['Weapon',0,32,0,7,0], 
                'Fork on a Stick': ['Weapon',0,37,0,7,0],
                'Iron Axe': ['Weapon',0,37,0,7,0], 
                'Fish Spear': ['Weapon',0,40,0,7,0],
                'Fish Spear +1': ['Weapon',1,42,0,0,0], 
                'Maple Sword': ['Weapon',0,48,0,7,0],
                'Cutlus': ['Weapon',0,52,0,7,0],

                #scroll
                'Glove Scroll ATT 100%': ['Scroll',0,1,0,100,'Gloves'],
                'Glove Scroll ATT 60%': ['Scroll',0,2,0,60,'Gloves'],
                'Glove Scroll ATT 10%': ['Scroll',0,3,0,10,'Gloves'],
                'Hat Scroll DEF 100%': ['Scroll',0,0,1,100,'Hat']
              }

#The game's variables and functions
class GameState():
    def __init__(self):
        self.mobCounter = 0
        self.bossCounter = 0
        self.isBoss = False
        self.currentEnemy = 'Snail'
        self.monsterLevel = monster_table[self.currentEnemy][0]
        self.monsterCurrentHP = monster_table[self.currentEnemy][1]
        self.monsterAttack = monster_table[self.currentEnemy][2]
        self.monsterMeso = monster_table[self.currentEnemy][4]
        self.currentEXP = 0
        self.playerStrength = 12
        self.playerTotalStrength = 12
        self.playerLevel = 1
        self.playerCurrentHP = 50
        self.playerMaxHP = 50
        self.playerCurrentMP = 5
        self.playerMaxMP = 5
        self.playerSP = 0
        self.playerHPRecovery = 1
        self.playerDamageTaken = 1
        self.playerNextDamage = 0
        self.playerIsDead = False
        self.playerMeso = 50
        self.playerInventorySize = 16
        self.playerInventoryCount = 0
        #Item name, Item Type, Strength, WA, Armor, Upgrade Slots, Scroll Detect
        #0 = Name of Item
        #1 = Type of Item
        #2 = Strength
        #3 = Weapon Attack
        #4 = Armor
        #5 = Upgrade Slots Remaining
        #6 = For Scroll Items, Detects what Equipment to Upgrade
        self.InventoryR = []

        self.expCount = [0]*60
        self.expMin = 0

        #Equipment
        self.playerEquips = {'Weapon':['Sword', 'Weapon', 0, 17, 0, 7],'Top':['White Undershirt', 'Top', 0, 0, 3, 7],'Bottom':['Blue Jean Shorts','Bottom',0,0,2,7],
                             'Gloves':['Empty', 'Gloves',0,0,0,0],'Hat':['Empty', 'Hat', 0,0,0,0],
                             'Shoes':['Leather Sandals', 'Shoes',0,0,2,5], 'Cape':['Empty','Cape',0,0,0,0]}

        self.playerArmor = self.playerEquips['Hat'][4] + self.playerEquips['Top'][4] + self.playerEquips['Bottom'][4] + self.playerEquips['Shoes'][4] + self.playerEquips['Weapon'][4] + self.playerEquips['Gloves'][4] + self.playerEquips['Cape'][4]
        self.playerWA = self.playerEquips['Hat'][3] + self.playerEquips['Top'][3] + self.playerEquips['Bottom'][3] + self.playerEquips['Shoes'][3] + self.playerEquips['Weapon'][3] + self.playerEquips['Gloves'][3] + self.playerEquips['Cape'][3]
        self.playerMaxDamage = int(self.playerWA * self.playerTotalStrength * 4 / 100)

        #Skills
        self.powerStrikeCost = 10
        self.powerStrikeMultiplier = 2

        #Others
        self.timeCounter = 0

    def saveGame(self):
        data["self.mobCounter"] = self.mobCounter
        data['self.currentEnemy'] = self.currentEnemy
        data['self.monsterLevel'] = self.monsterLevel
        data['self.monsterCurrentHP'] = self.monsterCurrentHP
        data['self.monsterAttack'] = self.monsterAttack
        data['self.monsterMeso'] = self.monsterMeso
        data['self.currentEXP'] = self.currentEXP
        data['self.playerStrength'] = self.playerStrength
        data['self.playerTotalStrength'] = self.playerTotalStrength
        data['self.playerLevel'] = self.playerLevel
        data['self.playerCurrentHP'] = self.playerCurrentHP
        data['self.playerMaxHP'] = self.playerMaxHP
        data['self.playerCurrentMP'] = self.playerCurrentMP
        data['self.playerMaxMP'] = self.playerMaxMP
        data['self.playerSP'] = self.playerSP
        data['self.playerHPRecovery'] = self.playerHPRecovery
        data['self.playerDamageTaken'] = self.playerDamageTaken
        data['self.playerNextDamage'] = self.playerNextDamage
        data['self.playerIsDead'] = self.playerIsDead
        data['self.playerMeso'] = self.playerMeso
        data['self.playerInventorySize'] = self.playerInventorySize
        data['self.playerInventoryCount'] = self.playerInventoryCount

        data['self.playerEquips'] = self.playerEquips

        data['self.playerArmor'] = self.playerArmor
        data['self.playerWA']= self.playerWA
        data['self.playerMaxDamage'] = self.playerMaxDamage

        data['self.powerStrikeCost'] = self.powerStrikeCost
        data['self.powerStrikeMultiplier'] = self.powerStrikeMultiplier

    def selectRightMob(self):
        if(self.isBoss == True):
            if(len(boss_list)>self.bossCounter+1):
                self.bossCounter += 1
            self.currentEnemy = boss_list[self.bossCounter]
            self.monsterCurrentHP = boss_table[self.currentEnemy][1]
            self.monsterAttack = boss_table[self.currentEnemy][2]
            self.monsterLevel = boss_table[self.currentEnemy][0]
        else:
            if(len(monster_list)>self.mobCounter+1):
                self.mobCounter += 1
            self.currentEnemy = monster_list[self.mobCounter]
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]
            self.monsterAttack = monster_table[self.currentEnemy][2]
            self.monsterLevel = monster_table[self.currentEnemy][0]

    def selectLeftMob(self):
        if(self.isBoss == True):
            self.bossCounter -= 1
            if(self.bossCounter < 0):
                self.bossCounter = 0
            self.currentEnemy = boss_list[self.bossCounter]
            self.monsterCurrentHP = boss_table[self.currentEnemy][1]
            self.monsterAttack = boss_table[self.currentEnemy][2]
            self.monsterLevel = boss_table[self.currentEnemy][0]

        else:
            self.mobCounter -= 1
            if(self.mobCounter<0):
                self.mobCounter = 0
            self.currentEnemy = monster_list[self.mobCounter]
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]
            self.monsterAttack = monster_table[self.currentEnemy][2]
            self.monsterLevel = monster_table[self.currentEnemy][0]

    def selectBossMob(self):
        self.isBoss = True
        self.currentEnemy = boss_list[self.bossCounter]
        self.monsterCurrentHP = boss_table[self.currentEnemy][1]
        self.monsterAttack = boss_table[self.currentEnemy][2]
        self.monsterLevel = boss_table[self.currentEnemy][0]

    def levelUp(self):
        self.currentEXP -= exp_to_next_level[self.playerLevel]
        self.playerLevel+=1
        self.playerStrength+=5
        self.playerSP+=3
        self.playerMaxMP += (5 + int(self.playerLevel/3))
        self.playerMaxHP += (14+int(self.playerTotalStrength/10))
        self.playerHPRecovery = int(self.playerTotalStrength/10)

    def monsterDie(self):
        if(self.isBoss == False):
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]
            self.currentEXP+= monster_table[self.currentEnemy][3]
            monster_table[self.currentEnemy][5]+=1
            self.expCount[self.expMin]=monster_table[self.currentEnemy][3]
            if self.currentEXP>= exp_to_next_level[self.playerLevel]:
                self.levelUp()
        else:
            boss_timer[self.currentEnemy] += 600
            self.monsterCurrentHP = boss_table[self.currentEnemy][1]
            self.currentEXP+= boss_table[self.currentEnemy][3]
            boss_table[self.currentEnemy][5]+=1
            self.expCount[self.expMin]=boss_table[self.currentEnemy][3]
            if self.currentEXP>= exp_to_next_level[self.playerLevel]:
                self.levelUp()

    def loot(self):
        if(self.isBoss == False):
            self.playerMeso += random.randint(int(monster_table[self.currentEnemy][4]*2/3),monster_table[self.currentEnemy][4])
            lootRoll = random.randint(1,10000)

            for key in drop_table[self.currentEnemy]:
                if(key>lootRoll):
                    if(self.playerInventoryCount < self.playerInventorySize):
                        print('You looted',drop_table[self.currentEnemy][key])
                        #Item name, Item Type, Strength, WA, Armor, Upgrade Slots, Scroll Detect
                        self.itemObj = ['Empty','Hat',0,0,0,0,0]
                        self.itemObj[0] = drop_table[self.currentEnemy][key]
                        self.itemObj[1] = drop_list[drop_table[self.currentEnemy][key]][0]
                        self.itemObj[2] = drop_list[drop_table[self.currentEnemy][key]][1]
                        self.itemObj[3] = drop_list[drop_table[self.currentEnemy][key]][2]
                        self.itemObj[4] = drop_list[drop_table[self.currentEnemy][key]][3]
                        self.itemObj[5] = drop_list[drop_table[self.currentEnemy][key]][4]
                        self.itemObj[6] = drop_list[drop_table[self.currentEnemy][key]][5]
                        self.InventoryR.append(self.itemObj)
                        
                        self.playerInventoryCount +=1
                        break
                    else:
                        print('Your inventory is full. Please remove an item')
        else:
            self.playerMeso += random.randint(int(boss_table[self.currentEnemy][4]*2/3),boss_table[self.currentEnemy][4])
            lootRoll = random.randint(1,10000)

            for key in drop_table[self.currentEnemy]:
                if(key>lootRoll):
                    if(self.playerInventoryCount < self.playerInventorySize):
                        self.itemObj = ['Empty','Hat',0,0,0,0]
                        self.itemObj[0] = drop_table[self.currentEnemy][key]
                        self.itemObj[1] = drop_list[drop_table[self.currentEnemy][key]][0]
                        self.itemObj[2] = drop_list[drop_table[self.currentEnemy][key]][1]
                        self.itemObj[3] = drop_list[drop_table[self.currentEnemy][key]][2]
                        self.itemObj[4] = drop_list[drop_table[self.currentEnemy][key]][3]
                        self.itemObj[5] = drop_list[drop_table[self.currentEnemy][key]][4]
                        self.itemObj[6] = drop_list[drop_table[self.currentEnemy][key]][5]
                        self.InventoryR.append(self.itemObj)
                        
                        self.playerInventoryCount +=1
                        break

    def damageRoll(self):
        self.playerMaxDamage = int(self.playerWA * self.playerTotalStrength * 4 / 100)
        self.playerNextDamage = random.randint(1,self.playerMaxDamage)
        if self.playerNextDamage < self.playerMaxDamage / 10:
            self.playerNextDamage = int(self.playerMaxDamage / 10)


    def hitMonster(self):
        if((self.isBoss == True) and (boss_timer[self.currentEnemy] > 0)):
            return
        else:
            self.monsterCurrentHP -= self.playerNextDamage

    def recoverHP(self):
        if(self.playerCurrentHP<self.playerMaxHP):
            self.playerCurrentHP += self.playerHPRecovery
            if(self.playerCurrentHP>self.playerMaxHP):
                self.playerCurrentHP = self.playerMaxHP
        if(self.playerCurrentMP<self.playerMaxMP):
            self.playerCurrentMP += 1

    def takeDamage(self):
        if(self.isBoss == True and boss_timer[self.currentEnemy] >0):
            return
        self.playerDamageTaken = (random.randint(int(self.monsterAttack/2),self.monsterAttack) - self.playerArmor - int(self.playerTotalStrength/10) - self.playerLevel + self.monsterLevel)
        if(self.playerDamageTaken<=0):
            self.playerDamageTaken = 1
        self.playerCurrentHP -= self.playerDamageTaken

    def playerDie(self):
        self.playerCurrentHP = 0
        self.playerIsDead = True
        if(self.isBoss == False):
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]
        else:
            self.monsterCurrentHP = boss_table[self.currentEnemy][1]

    def updateStats(self):
        self.playerTotalStrength = self.playerEquips['Hat'][2] + self.playerEquips['Top'][2] + self.playerEquips['Bottom'][2] + self.playerEquips['Shoes'][2] + self.playerEquips['Weapon'][2] + self.playerEquips['Gloves'][2] + self.playerEquips['Cape'][2] + self.playerStrength
        self.playerArmor = self.playerEquips['Hat'][4] + self.playerEquips['Top'][4] + self.playerEquips['Bottom'][4] + self.playerEquips['Shoes'][4] + self.playerEquips['Weapon'][4] + self.playerEquips['Gloves'][4] + self.playerEquips['Cape'][4]
        self.playerWA = self.playerEquips['Hat'][3] + self.playerEquips['Top'][3] + self.playerEquips['Bottom'][3] + self.playerEquips['Shoes'][3] + self.playerEquips['Weapon'][3] + self.playerEquips['Gloves'][3] + self.playerEquips['Cape'][3]
        self.playerMaxDamage = int(self.playerWA * self.playerTotalStrength * 4 / 100)

    def loadGame(self):
        
        self.mobCounter = data['self.mobCounter']
        self.bossCounter = data['self.bossCounter']
        self.isBoss = data['self.isBoss']
        self.currentEnemy = data['self.currentEnemy']
        self.monsterLevel = data['self.monsterLevel']
        self.monsterCurrentHP = data['self.monsterCurrentHP']
        self.monsterAttack = data['self.monsterAttack']
        self.monsterMeso = data['self.monsterMeso']
        self.currentEXP = data['self.currentEXP']
        self.playerStrength = data['self.playerStrength']
        self.playerTotalStrength = data['self.playerTotalStrength']
        self.playerLevel = data['self.playerLevel']
        self.playerCurrentHP = data['self.playerCurrentHP']
        self.playerMaxHP = data['self.playerMaxHP']
        self.playerCurrentMP = data['self.playerCurrentMP']
        self.playerMaxMP = data['self.playerMaxMP']
        self.playerSP = data['self.playerSP']
        self.playerHPRecovery = data['self.playerHPRecovery']
        self.playerDamageTaken = data['self.playerDamageTaken']
        self.playerNextDamage = data['self.playerNextDamage']
        self.playerIsDead = data['self.playerIsDead']
        self.playerMeso = data['self.playerMeso']
        self.playerInventorySize = data['self.playerInventorySize']
        self.playerInventoryCount = data['self.playerInventoryCount']
        #Name of item, item type, inventory slot, str, wa, armor
        self.InventoryR = data['self.InventoryR']

        #Equipment
        self.playerEquips = data['self.playerEquips']

        self.playerArmor = data['self.playerArmor']
        self.playerWA = data['self.playerWA']
        self.playerMaxDamage = data['self.playerMaxDamage']

        #Skills
        self.powerStrikeCost = data['self.powerStrikeCost']
        self.powerStrikeMultiplier = data['self.powerStrikeMultiplier']


    def proceed(self):
        for item in boss_timer:
            if(boss_timer[item]> 0):
                boss_timer[item] -= 1
        self.expCount[self.expMin]=0
        self.recoverHP()
        self.updateStats()
        if(self.playerIsDead):
            if(self.playerCurrentHP>=self.playerMaxHP):
                self.playerIsDead = False
        if(not self.playerIsDead):
            self.damageRoll()
            self.hitMonster()
            if(self.monsterCurrentHP <=0):
                self.monsterDie()
                self.loot()
            else:
                self.takeDamage()
                if self.playerCurrentHP <= 0:
                    self.playerDie()


        


    
#UI
class UserInterface():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.GameState = GameState()
        self.window = pygame.display.set_mode((width,height))
        self.font = pygame.font.SysFont('Helvetica',int(width*0.018))
        self.fontBig = pygame.font.SysFont('Helvetica', int(width*0.025))
        self.fontHuge = pygame.font.SysFont('Helvetica', int(width*0.04))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Maple Idle")
        pygame.display.set_icon(pygame.image.load("leaf.png"))
        self.running = True
        self.onMenu = True
        self.onControls = False
        self.image_item_rect = []
        self.gameLoaded = 0

        self.mouse = pygame.mouse.get_pos()

    
    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GameState.saveGame()
                with open('data.txt','w') as store_data:
                    json.dump(data, store_data)
                self.running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for a in range((self.GameState.playerInventoryCount)):
                        if(self.image_item_rect[a].x<=self.mouse[0]< (self.image_item_rect[a].x+int(self.image_item_rect[a].width)) and (self.image_item_rect[a].y<= self.mouse[1] < self.image_item_rect[a].y+int(self.image_item_rect[a].height))):
                            if(self.GameState.InventoryR[a][1] == 'Hat'):
                                if(self.GameState.playerEquips['Hat'][0] == 'Empty'):
                                    self.GameState.playerEquips['Hat'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Hat']
                                    self.GameState.playerEquips['Hat'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Top'):
                                if(self.GameState.playerEquips['Top'][0] == 'Empty'):
                                    self.GameState.playerEquips['Top'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Top']
                                    self.GameState.playerEquips['Top'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Bottom'):
                                if(self.GameState.playerEquips['Bottom'][0] == 'Empty'):
                                    self.GameState.playerEquips['Bottom'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Bottom']
                                    self.GameState.playerEquips['Bottom'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Gloves'):
                                if(self.GameState.playerEquips['Gloves'][0] == 'Empty'):
                                    self.GameState.playerEquips['Gloves'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Gloves']
                                    self.GameState.playerEquips['Gloves'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Shoes'):
                                if(self.GameState.playerEquips['Shoes'][0] == 'Empty'):
                                    self.GameState.playerEquips['Shoes'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Shoes']
                                    self.GameState.playerEquips['Shoes'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Cape'):
                                if(self.GameState.playerEquips['Cape'][0] == 'Empty'):
                                    self.GameState.playerEquips['Cape'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Cape']
                                    self.GameState.playerEquips['Cape'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Weapon'):
                                if(self.GameState.playerEquips['Weapon'][0] == 'Empty'):
                                    self.GameState.playerEquips['Weapon'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR.pop(a)
                                    self.GameState.playerInventoryCount -=1
                                    break
                                else:
                                    temp = self.GameState.playerEquips['Weapon']
                                    self.GameState.playerEquips['Weapon'] = self.GameState.InventoryR[a]
                                    self.GameState.InventoryR[a] =temp
                                    break
                            elif(self.GameState.InventoryR[a][1] == 'Scroll'):
                                print(self.GameState.playerEquips[self.GameState.InventoryR[a][6]][5])
                                if(self.GameState.playerEquips[self.GameState.InventoryR[a][6]][0] == 'Empty'):
                                    print('No '+self.GameState.playerEquips[self.GameState.InventoryR[a][6]][1]+' Equipped')
                                elif(self.GameState.playerEquips[self.GameState.InventoryR[a][6]][5]==0):
                                    print('No Upgrade Slots Left')
                                else:
                                    b = random.randint(1,100)
                                    if(b<=self.GameState.InventoryR[a][5]):
                                        print("Scroll succeeded")
                                        self.GameState.playerEquips[self.GameState.InventoryR[a][6]][2] +=self.GameState.InventoryR[a][2]
                                        self.GameState.playerEquips[self.GameState.InventoryR[a][6]][3] +=self.GameState.InventoryR[a][3]
                                        self.GameState.playerEquips[self.GameState.InventoryR[a][6]][4] +=self.GameState.InventoryR[a][4]
                                        self.GameState.playerEquips[self.GameState.InventoryR[a][6]][5] -= 1
                                        self.GameState.InventoryR.pop(a)
                                        self.GameState.playerInventoryCount-=1
                                    else:
                                        print("Scroll failed")
                                        self.GameState.playerEquips[self.GameState.InventoryR[a][6]][5] -= 1
                                        self.GameState.InventoryR.pop(a)
                                        self.GameState.playerInventoryCount-=1
                                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.GameState.saveGame()
                    with open('data.txt','w') as store_data:
                        json.dump(data, store_data)
                    self.onMenu = True
                    break
                elif event.key == pygame.K_RIGHT:
                    self.GameState.selectRightMob()
                elif event.key == pygame.K_LEFT:
                    self.GameState.selectLeftMob()
                elif event.key == pygame.K_UP:
                    self.GameState.selectBossMob()
                elif event.key == pygame.K_DOWN:
                    self.GameState.isBoss = False
                    self.GameState.currentEnemy = monster_list[self.GameState.mobCounter]
                    self.GameState.monsterCurrentHP = monster_table[self.GameState.currentEnemy][1]
                    self.GameState.monsterAttack = monster_table[self.GameState.currentEnemy][2]
                    self.GameState.monsterLevel = monster_table[self.GameState.currentEnemy][0]
                elif event.key == pygame.K_1:
                    if(not self.GameState.playerIsDead):
                        if(self.GameState.playerCurrentMP>= self.GameState.powerStrikeCost):
                            if(self.GameState.isBoss == True and boss_timer[self.GameState.currentEnemy]>= 0):
                                return
                            else:
                                self.GameState.playerCurrentMP -= self.GameState.powerStrikeCost
                                damage = int(random.randint(int(self.GameState.playerMaxDamage / 10),self.GameState.playerMaxDamage)*self.GameState.powerStrikeMultiplier)
                                self.GameState.monsterCurrentHP -= damage
                                if(self.GameState.monsterCurrentHP <=0):
                                    self.GameState.monsterDie()
                                    self.GameState.loot()
                                break
                elif event.key == pygame.K_d:
                    for a in range((self.GameState.playerInventoryCount)):
                        if(self.image_item_rect[a].x<=self.mouse[0]< (self.image_item_rect[a].x+int(self.image_item_rect[a].width))
                            and (self.image_item_rect[a].y<= self.mouse[1] < self.image_item_rect[a].y+int(self.image_item_rect[a].height))):
                            self.GameState.InventoryR.pop(a)
                            self.GameState.playerInventoryCount -=1
                            break
   
    def update(self):
        self.GameState.proceed()

    def render(self):
        #Make screen white
        self.window.fill((255,255,255))

        #Player Stats Descriptors
        pygame.draw.rect(self.window,(192,192,192),(0,height-int(height*0.3),int(width*0.20),int(height*0.3)))

        text_level = self.fontBig.render(('Level: '+str(self.GameState.playerLevel)), False, (0, 0, 0))
        self.window.blit(text_level,(0,int(height*0.71)))

        text_strength = self.font.render(('Strength: '+str(self.GameState.playerTotalStrength)), False, (0, 0, 0))
        self.window.blit(text_strength,(0,int(height*0.76)))

        text_wa = self.font.render(('Weapon Attack: '+str(self.GameState.playerWA)), False, (0, 0, 0))
        self.window.blit(text_wa,(0,int(height*0.785)))

        text_damage_range = self.font.render(('Damage: ' + str(int(self.GameState.playerMaxDamage/10))+'-'+str(self.GameState.playerMaxDamage)),False,(0,0,0))
        self.window.blit(text_damage_range,(0,int(height*0.81)))

        text_armor = self.font.render(('Armor: '+str(self.GameState.playerArmor)), False, (0, 0, 0))
        self.window.blit(text_armor,(0,int(height*0.835)))

        text_sp = self.font.render(('Skill Points: '+str(self.GameState.playerSP)), False, (0, 0, 0))
        self.window.blit(text_sp,(0,int(height*0.86)))

        text_meso = self.font.render(('Meso: ' + str(self.GameState.playerMeso)), False, (0,0,0))
        self.window.blit(text_meso,(0,int(height*0.885)))
        
        pygame.draw.rect(self.window,(0,0,0),(0,int(height*0.97),int(width*0.2),height*0.03))
        pygame.draw.rect(self.window,(0,255,0),(0,int(height*0.97),int(self.GameState.currentEXP/exp_to_next_level[self.GameState.playerLevel]*width*0.2),height*0.03))
        text_exp = self.font.render(('Exp: ' + str(self.GameState.currentEXP) + "/" + str(exp_to_next_level[self.GameState.playerLevel])),False,(255,255,255))
        self.window.blit(text_exp,(width*0.01,int(height*0.975)))

        #Monster Descriptors

        image_monster = pygame.image.load(self.GameState.currentEnemy + '.gif')
        image_monster_rect = image_monster.get_rect(center=(int(width*0.675),int(height*0.3)))
        self.window.blit(image_monster,image_monster_rect)

        pygame.draw.rect(self.window,(0,0,0),(int(width*0.6),int(height*0.44),width*0.15,height*0.03))
        if(self.GameState.isBoss == False):
            pygame.draw.rect(self.window,(255,0,0),(int(width*0.6),int(height*0.44),int(self.GameState.monsterCurrentHP/monster_table[self.GameState.currentEnemy][1]*width*0.15),height*0.03))
            text_enemy_hp = self.font.render(('HP: '+str(self.GameState.monsterCurrentHP)+'/'+str(monster_table[self.GameState.currentEnemy][1])), False, (255, 255, 255))
            self.window.blit(text_enemy_hp,(int(width*0.61),int(height*0.445)))

            text_enemy = self.font.render(('Monster: '+self.GameState.currentEnemy), False, (0, 0, 0))
            self.window.blit(text_enemy,(int(width*0.6),int(height*0.475)))

            text_enemy_lvl = self.font.render(('Level: '+str(self.GameState.monsterLevel)), False, (0, 0, 0))
            self.window.blit(text_enemy_lvl,(int(width*0.6),int(height*0.50)))

            text_enemy_att = self.font.render(('Attack: '+str(self.GameState.monsterAttack)), False, (0, 0, 0))
            self.window.blit(text_enemy_att,(int(width*0.6),int(height*0.525)))

            text_enemy_exp = self.font.render(('Exp: '+str(monster_table[self.GameState.currentEnemy][3])), False, (0, 0, 0))
            self.window.blit(text_enemy_exp,(int(width*0.6),int(height*0.55)))

            text_enemy_meso = self.font.render(('Meso: '+str(int(monster_table[self.GameState.currentEnemy][4]*2/3))+'-'+str(monster_table[self.GameState.currentEnemy][4])), False, (0, 0, 0))
            self.window.blit(text_enemy_meso,(int(width*0.6),int(height*0.575)))

            text_enemy_kc = self.font.render(('Kill Count: '+str(monster_table[self.GameState.currentEnemy][5])), False, (0, 0, 0))
            self.window.blit(text_enemy_kc,(int(width*0.6),int(height*0.60)))
        else:
            if(boss_timer[self.GameState.currentEnemy]>0):
                text_boss_time = self.font.render(str(int(boss_timer[self.GameState.currentEnemy]/60))+ ':' + str(boss_timer[self.GameState.currentEnemy]%60), False, (0,0,0))
                self.window.blit(text_boss_time, (int(width*0.6),int(height*0.35)))

            pygame.draw.rect(self.window,(255,0,0),(int(width*0.6),int(height*0.44),int(self.GameState.monsterCurrentHP/boss_table[self.GameState.currentEnemy][1]*width*0.15),height*0.03))
            text_enemy_hp = self.font.render(('HP: '+str(self.GameState.monsterCurrentHP)+'/'+str(boss_table[self.GameState.currentEnemy][1])), False, (255, 255, 255))
            self.window.blit(text_enemy_hp,(int(width*0.61),int(height*0.445)))

            text_enemy = self.font.render(('Monster: '+self.GameState.currentEnemy), False, (0, 0, 0))
            self.window.blit(text_enemy,(int(width*0.6),int(height*0.475)))

            text_enemy_lvl = self.font.render(('Level: '+str(self.GameState.monsterLevel)), False, (0, 0, 0))
            self.window.blit(text_enemy_lvl,(int(width*0.6),int(height*0.50)))

            text_enemy_att = self.font.render(('Attack: '+str(self.GameState.monsterAttack)), False, (0, 0, 0))
            self.window.blit(text_enemy_att,(int(width*0.6),int(height*0.525)))

            text_enemy_exp = self.font.render(('Exp: '+str(boss_table[self.GameState.currentEnemy][3])), False, (0, 0, 0))
            self.window.blit(text_enemy_exp,(int(width*0.6),int(height*0.55)))

            text_enemy_meso = self.font.render(('Meso: '+str(int(boss_table[self.GameState.currentEnemy][4]*2/3))+'-'+str(boss_table[self.GameState.currentEnemy][4])), False, (0, 0, 0))
            self.window.blit(text_enemy_meso,(int(width*0.6),int(height*0.575)))

            text_enemy_kc = self.font.render(('Kill Count: '+str(boss_table[self.GameState.currentEnemy][5])), False, (0, 0, 0))
            self.window.blit(text_enemy_kc,(int(width*0.6),int(height*0.60)))

        text_expmin = self.font.render(('Exp/Min: '+str(sum(self.GameState.expCount))), False, (0, 0, 0))
        self.window.blit(text_expmin,(int(width*0.6),int(height*0.65)))

        #Player Descriptors
        pygame.draw.rect(self.window,(0,0,0),(int(width*0.2),int(height*0.44),width*0.15,height*0.03))
        pygame.draw.rect(self.window,(255,0,0),(int(width*0.2),int(height*0.44),int(self.GameState.playerCurrentHP/self.GameState.playerMaxHP*width*0.15),height*0.03))
        text_player = self.fontBig.render(('Player'), False, (0, 0, 0))
        self.window.blit(text_player,(int(width*0.2),int(height*0.475)))
        text_player_hp = self.font.render(('HP: ' + str(self.GameState.playerCurrentHP)+ '/'+str(self.GameState.playerMaxHP)), False, (255, 255, 255))
        self.window.blit(text_player_hp,(int(width*0.21),int(height*0.445)))
        text_player_mp = self.font.render(('MP: ' + str(self.GameState.playerCurrentMP) + '/' + str(self.GameState.playerMaxMP)), False, (0, 0, 0))
        self.window.blit(text_player_mp,(int(width*0.2),int(height*0.515)))

        #Damage Descriptors
        text_player_damage = self.fontBig.render(('-' + str(self.GameState.playerNextDamage)), False, (255, 0, 0))
        self.window.blit(text_player_damage,(int(width*0.6),int(height*0.4)))
        text_monster_damage = self.fontBig.render(('-' + str(self.GameState.playerDamageTaken)), False, (255, 0, 0))
        self.window.blit(text_monster_damage,(int(width*0.2),int(height*0.4)))

        text_player_rec = self.fontBig.render(('+' + str(self.GameState.playerHPRecovery)), False, (0, 50, 255))
        self.window.blit(text_player_rec,(int(width*0.2),int(height*0.35)))

        #Inventory Remastered
                #Inventory Box and Text
        pygame.draw.rect(self.window,(192,192,192),(width*0.80,0,width*0.225,height*0.25))
        text_inventory = self.font.render('Inventory', False, (0,0,0))
        text_inventory_rect = text_inventory.get_rect(center=(int(width*0.90),int(height*0.025)))
        self.window.blit(text_inventory,text_inventory_rect)
                #Initialize to Empty
        image_empty = pygame.image.load('empty.gif')
        for x in range(self.GameState.playerInventorySize):
            image_empty_rect = image_empty.get_rect(center=(int(width*0.825)+(x%4)*int(width*0.05),int(height*0.075)+int(x/4)*int(height*0.05)))
            self.window.blit(image_empty,image_empty_rect)

        #Current Equips
        pygame.draw.rect(self.window,(192,192,192),(0,0,width*0.175,height*0.225))

        image_hat = pygame.image.load(self.GameState.playerEquips['Hat'][0] + '.gif')
        image_hat_rect = image_hat.get_rect(center=(int(width*0.075),int(height*0.05)))
        self.window.blit(image_hat,image_hat_rect)

        image_top = pygame.image.load(self.GameState.playerEquips['Top'][0] + '.gif')
        image_top_rect = image_top.get_rect(center=(int(width*0.075),int(height*0.1)))
        self.window.blit(image_top,image_top_rect)

        image_bottom = pygame.image.load(self.GameState.playerEquips['Bottom'][0] + '.gif')
        image_bottom_rect = image_bottom.get_rect(center=(int(width*0.075),int(height*0.15)))
        self.window.blit(image_bottom,image_bottom_rect)

        image_shoes = pygame.image.load(self.GameState.playerEquips['Shoes'][0] + '.gif')
        image_shoes_rect = image_shoes.get_rect(center=(int(width*0.075),int(height*0.20)))
        self.window.blit(image_shoes,image_shoes_rect)

        image_gloves = pygame.image.load(self.GameState.playerEquips['Gloves'][0] + '.gif')
        image_gloves_rect = image_gloves.get_rect(center=(int(width*0.125),int(height*0.15)))
        self.window.blit(image_gloves,image_gloves_rect)

        image_cape = pygame.image.load(self.GameState.playerEquips['Cape'][0] + '.gif')
        image_cape_rect = image_cape.get_rect(center=(int(width*0.025),int(height*0.1)))
        self.window.blit(image_cape,image_cape_rect)

        image_weapon = pygame.image.load(self.GameState.playerEquips['Weapon'][0] + '.gif')
        image_weapon_rect = image_weapon.get_rect(center=(int(width*0.125),int(height*0.1)))
        self.window.blit(image_weapon,image_weapon_rect)

        #Show Equipment Stats

        self.equipHovered = False
        if int(image_hat_rect.x) <= self.mouse[0] <(image_hat_rect.x+image_hat_rect.width) and int(image_hat_rect.y) <= self.mouse[1] < (image_hat_rect.y+image_hat_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Hat'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Hat'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Hat'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Hat'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Hat'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_top_rect.x) <= self.mouse[0] <(image_top_rect.x+image_top_rect.width) and int(image_top_rect.y) <= self.mouse[1] < (image_top_rect.y+image_top_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Top'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Top'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Top'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Top'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Top'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_bottom_rect.x) <= self.mouse[0] <(image_bottom_rect.x+image_bottom_rect.width) and int(image_bottom_rect.y) <= self.mouse[1] < (image_bottom_rect.y+image_bottom_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Bottom'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Bottom'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Bottom'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Bottom'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Bottom'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_shoes_rect.x) <= self.mouse[0] <(image_shoes_rect.x+image_shoes_rect.width) and int(image_shoes_rect.y) <= self.mouse[1] < (image_shoes_rect.y+image_shoes_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Shoes'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Shoes'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Shoes'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Shoes'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Shoes'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_gloves_rect.x) <= self.mouse[0] <(image_gloves_rect.x+image_gloves_rect.width) and int(image_gloves_rect.y) <= self.mouse[1] < (image_gloves_rect.y+image_gloves_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Gloves'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Gloves'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Gloves'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Gloves'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Gloves'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_cape_rect.x) <= self.mouse[0] <(image_cape_rect.x+image_cape_rect.width) and int(image_cape_rect.y) <= self.mouse[1] < (image_cape_rect.y+image_cape_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Cape'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Cape'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Cape'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Cape'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Cape'][5]),False,(0,0,0))
            self.equipHovered = True
        elif int(image_weapon_rect.x) <= self.mouse[0] <(image_weapon_rect.x+image_weapon_rect.width) and int(image_weapon_rect.y) <= self.mouse[1] < (image_weapon_rect.y+image_weapon_rect.height):
            equip_str_text = self.font.render('Str: '+ str(self.GameState.playerEquips['Weapon'][2]), False, (0,0,0))
            equip_wa_text = self.font.render('WA: '+ str(self.GameState.playerEquips['Weapon'][3]), False, (0,0,0))
            equip_armor_text = self.font.render('Armor: '+ str(self.GameState.playerEquips['Weapon'][4]), False, (0,0,0))
            equipped_text = self.font.render(self.GameState.playerEquips['Weapon'][0], False, (0,0,0))
            equip_upgrades = self.font.render('Upgrade Slots: '+ str(self.GameState.playerEquips['Weapon'][5]),False,(0,0,0))
            self.equipHovered = True
            
        if(self.equipHovered == True):
            pygame.draw.rect(self.window,(192,192,192),(int(width*0.18),0,int(width*0.15),int(height*0.15)))
            self.window.blit(equipped_text,(int(width*0.18),0))
            self.window.blit(equip_str_text, (int(width*0.18),int(height*0.025)))
            self.window.blit(equip_wa_text, (int(width*0.18),int(height*0.05)))
            self.window.blit(equip_armor_text, (int(width*0.18),int(height*0.075)))
            self.window.blit(equip_upgrades, (int(width*0.18),int(height*0.1)))
        
        #Inventory System R
        self.image_item_rect.clear()

        images_item = [pygame.image.load(f'{self.GameState.InventoryR[x][0]}.gif') for x in range(self.GameState.playerInventoryCount)]
        
        for x in range(self.GameState.playerInventoryCount):
            self.image_item_rect.append(images_item[x].get_rect(center=(int(width*0.825)+(x%4)*int(width*0.05),int(height*0.075)+int(x/4)*int(height*0.05))))

        for x in range((self.GameState.playerInventoryCount)):
            #images_item[x] = pygame.image.load(self.GameState.InventoryR[x][0]+'.gif')
            #image_item_rect = images_item[x].get_rect(center=(int(width*0.825)+(x%4)*int(width*0.05),int(height*0.075)+int(x/4)*int(height*0.05)))
            self.window.blit(images_item[x],self.image_item_rect[x])

        #Hover over Inventory Menu
        for a in range((self.GameState.playerInventoryCount)):
            if(self.image_item_rect[a].x<=self.mouse[0]< (self.image_item_rect[a].x+int(self.image_item_rect[a].width))
               and (self.image_item_rect[a].y<= self.mouse[1] < self.image_item_rect[a].y+int(self.image_item_rect[a].height))):
                pygame.draw.rect(self.window,(192,192,192),(int(width*0.60),0,int(width*0.2),int(height*0.15)))
                equip_str_text = self.font.render('Str: '+ str(self.GameState.InventoryR[a][2]), False, (0,0,0))
                equip_wa_text = self.font.render('WA: '+ str(self.GameState.InventoryR[a][3]), False, (0,0,0))
                equip_armor_text = self.font.render('Armor: '+ str(self.GameState.InventoryR[a][4]), False, (0,0,0))
                equipped_text = self.font.render(self.GameState.InventoryR[a][0], False, (0,0,0))
                equip_type_text = self.font.render(''+ str(self.GameState.InventoryR[a][1]), False, (0,0,0))
                equip_upgrades_text = self.font.render('Upgrade Slots: '+ str(self.GameState.InventoryR[a][5]), False, (0,0,0))
                self.window.blit(equipped_text,(int(width*0.60),0))
                self.window.blit(equip_str_text, (int(width*0.60),int(height*0.05)))
                self.window.blit(equip_wa_text, (int(width*0.60),int(height*0.075)))
                self.window.blit(equip_armor_text, (int(width*0.60),int(height*0.1)))
                self.window.blit(equip_type_text,(int(width*0.60),int(height*0.025)))
                self.window.blit(equip_upgrades_text, (int(width*0.60),int(height*0.125)))
                break
                

        pygame.display.update()


    #Inputs when you're on the Menu
    def processMenuInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.onMenu = False
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.onMenu = False
                    self.running = False
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if int(width*0.4) <= self.mouse[0] <(width*0.6) and int(height*0.4) <= self.mouse[1] < (int(height*0.5)):
                    self.onMenu = False
                    break
                elif int(width*0.4) <= self.mouse[0] <(width*0.6) and int(height*0.6) <= self.mouse[1] < (int(height*0.7)):
                    self.onMenu = False
                    self.onControls = True
                    break


    #Menu UI
    def menuUI(self):
        #Make screen white
        self.window.fill((255,255,255))

        #Maple Idle
        maple_idle = self.fontHuge.render('Maple Idle', False, (0,0,0))
        maple_idle_rect = maple_idle.get_rect(center=(int(width*0.5),int(height*0.25)))
        self.window.blit(maple_idle, maple_idle_rect)


        #Play Button
        play_button = self.fontBig.render('Play', False, (0,0,0))
        play_button_rect = play_button.get_rect(center=(int(width*0.5),int(height*0.45)))
        pygame.draw.rect(self.window,(192,192,192),(int(width*0.4),int(height*0.4),int(width*0.20),int(height*0.1)))

        if int(width*0.4) <= self.mouse[0] <(width*0.6) and int(height*0.4) <= self.mouse[1] <= (int(height*0.5)):
            pygame.draw.rect(self.window,(128,128,128),(int(width*0.4),int(height*0.4),int(width*0.20),int(height*0.1)))

        self.window.blit(play_button, play_button_rect)

        #Controls Button
        control_button = self.fontBig.render('Controls', False, (0,0,0))
        control_button_rect = control_button.get_rect(center=(int(width*0.5),int(height*0.65)))
        pygame.draw.rect(self.window,(192,192,192),(int(width*0.4),int(height*0.6),int(width*0.20),int(height*0.1)))

        if int(width*0.4) <= self.mouse[0] <(width*0.6) and int(height*0.6) <= self.mouse[1] <= (int(height*0.7)):
            pygame.draw.rect(self.window,(128,128,128),(int(width*0.4),int(height*0.6),int(width*0.20),int(height*0.1)))

        self.window.blit(control_button, control_button_rect)


        #Version Number
        version_number = self.font.render('Pre Alpha 1.0', False, (0,0,0))
        version_number_rect = version_number.get_rect(center=(int(width*0.9),int(height*0.95)))
        self.window.blit(version_number,version_number_rect)

        pygame.display.update()

    #Control Screen UI
    def controlsUI(self):
        self.window.fill((255,255,255))

        pygame.draw.rect(self.window,(192,192,192),(0,int(height*0.075),width,int(height*0.05)))
        controls_text = self.fontHuge.render('Controls', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.05)))
        self.window.blit(controls_text,controls_text_rect)

        controls_text = self.font.render('Press Left and Right to Change Mobs', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.1)))
        self.window.blit(controls_text,controls_text_rect)

        pygame.draw.rect(self.window,(192,192,192),(0,int(height*0.175),width,int(height*0.05)))
        controls_text = self.font.render('Press Up to Fight Boss, Down to Fight Mob', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.15)))
        self.window.blit(controls_text,controls_text_rect)

        controls_text = self.font.render('Press on Item in Inventory to Equip It', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.20)))
        self.window.blit(controls_text,controls_text_rect)

        pygame.draw.rect(self.window,(192,192,192),(0,int(height*0.275),width,int(height*0.05)))
        controls_text = self.font.render('Press D on Item in Inventory to Destroy It', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.25)))
        self.window.blit(controls_text,controls_text_rect)

        controls_text = self.font.render('Press 1 to Use Power Strike', False, (0,0,0))
        controls_text_rect = controls_text.get_rect(center=(int(width*0.5),int(height*0.30)))
        self.window.blit(controls_text,controls_text_rect)

        pygame.display.update()

    #Control Screen Inputs
    def processControlsInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.onMenu = False
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.onMenu = True
                    self.onControls = False
                    break


    #The Everything Loop
    def run(self):
        while self.running:

            self.clock.tick(60)

            while(self.onMenu == True):
                self.mouse = pygame.mouse.get_pos()
                self.processMenuInput()
                self.menuUI()
                pygame.time.wait(50)
                
            if(self.onControls == True):
                self.mouse = pygame.mouse.get_pos()
                self.processControlsInput()
                self.controlsUI()
                pygame.time.wait(50)

            if(self.gameLoaded==0):
                self.GameState.loadGame()
                self.gameLoaded+=1

            if(self.onControls == False and self.onMenu == False):
                # Main Game Loop
                self.mouse = pygame.mouse.get_pos()
                self.processInput()
                if(self.GameState.timeCounter %20 == 0):
                    self.update()
                    self.GameState.expMin += 1
                    if(self.GameState.expMin == 60):
                        self.GameState.expMin = 0
                if(self.GameState.timeCounter %600 ==0):
                    self.GameState.saveGame()
                self.render()

                #Exp Per Min
                self.GameState.timeCounter += 1

            pygame.time.wait(50)
            

#checks if there is a save file
data = {
    'self.mobCounter':0,
    'self.bossCounter': 0,
    'self.isBoss': False,
    'self.currentEnemy': 'Snail',
    'self.monsterLevel': monster_table['Snail'][0],
    'self.monsterCurrentHP': monster_table['Snail'][1],
    'self.monsterAttack': monster_table['Snail'][2],
    'self.monsterMeso': monster_table['Snail'][4],
    'self.currentEXP': 0,
    'self.playerStrength':12,
    'self.playerTotalStrength': 12,
    'self.playerLevel': 1,
    'self.playerCurrentHP':50,
    'self.playerMaxHP': 50,
    'self.playerCurrentMP': 5,
    'self.playerMaxMP': 5,
    'self.playerSP': 0,
    'self.playerHPRecovery': 1,
    'self.playerDamageTaken': 1,
    'self.playerNextDamage': 0,
    'self.playerIsDead': False,
    'self.playerMeso': 50,
    'self.playerInventorySize':16,
    'self.playerInventoryCount': 0,
    'self.InventoryR': [],

    'self.playerEquips': {'Weapon':['Sword', 'Weapon', 0, 17, 0, 7],'Top':['White Undershirt', 'Top', 0, 0, 3, 7],'Bottom':['Blue Jean Shorts','Bottom',0,0,2,7],
                             'Gloves':['Empty', 'Gloves',0,0,0,0],'Hat':['Empty', 'Hat', 0,0,0,0],
                             'Shoes':['Leather Sandals', 'Shoes',0,0,2,5], 'Cape':['Empty','Cape',0,0,0,0]},

    'self.playerArmor': 7,
    'self.playerWA': 17,
    'self.playerMaxDamage': 8,

    'self.powerStrikeCost': 10,
    'self.powerStrikeMultiplier': 2

}

try:
    with open('data.txt') as load_file:
        data = json.load(load_file)
except:
    with open('data.txt','w') as store_file:
        json.dump(data, store_file)


UserInterface = UserInterface()
UserInterface.run()
