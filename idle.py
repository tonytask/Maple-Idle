import pygame
import random
import sys

width = 640
height = 480

monster_list = ['Snail', 'Blue Snail', 'Shroom', 'Red Snail', 'Slime', 'Orange Mushroom',
                'Ribbon Pig', 'Octopus', 'Bubbling', 'Green Mushroom', 'Horny Mushroom',
                'Evil Eye']

boss_list = ['Mano']

#Level, HP, Att, Exp, Meso, Kill Count
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

boss_table = {'Mano': [20,2000,125,200,200,0]}

drop_table = {'Snail': {20: 'Work Gloves +1',125: 'Green Headband'},
               'Blue Snail': {25: 'Grey Thick Sweat Pants',50: 'Blue One-Lined T-Shirt', 125: 'White Undershirt +1'},
               'Shroom': {25: 'Ice Jeans', 125: 'Jean Capris'},
               'Red Snail': {10: 'Wooden Sword +3', 80: 'Wooden Sword'},
               'Slime': {25: 'Fork on a Stick', 55: 'Bronze Aroa Boots', 100: 'White Bandana'},
               'Orange Mushroom': {40: 'Bronze Koif', 80: 'White Gomushin', 125: 'Spear'},
               'Ribbon Pig': {25: 'Orange Sporty T-Shirt +2', 110: 'Orange Sporty T-Shirt', 200: 'Work Gloves'},
               'Octopus': {40: 'Brown Corporal',70: 'Brown Corporal Pants', 125: 'Aqua Snowboard'},
               'Bubbling': {25: 'Fish Spear +1', 75: 'Fish Spear'},
               'Green Mushroom': {25:'Work Gloves +2',50: 'White Starry Bandana'},
               'Horny Mushroom': {20: 'Iron Burgernet Helm',35:'Warfare Pants', 60: 'Red Whitebottom Shoes'},
               'Evil Eye': {25: 'Maple Sword', 50: 'Maple Cape'},
               'Mano': {1000: 'Work Gloves +3'}}

exp_to_next_level = {1: 15, 2:34, 3:57, 4:92, 5:135, 6:372, 7:560, 8:840, 9:1242, 10:1144,
                    11:1573,12:2144,13:2800,14:3640,15:4700,16:5893,17:7360,18:9144, 
                    19:11120,20:13477,21:16268,22:19320,23:22880,24:27008,25:31477,
                    26:36600,27:42444,28:48720,29:55813,30:63800}

hat_table_armor = {'Empty': [0,0,0], 'Green Headband': [0,0,5], 'White Bandana': [0,0,8], 'Bronze Koif': [0,0,10],
                   'White Starry Bandana': [0,0,15],
                   'Iron Burgernet Helm': [0,0,25]}

top_table_armor = {'Empty': [0,0,0], 'White Undershirt': [0,0,3], 'Blue One-Lined T-Shirt': [0,0,11],
                   'White Undershirt +1': [0,0,5], 
                   'Orange Sporty T-Shirt': [0,0,11], 'Orange Sporty T-Shirt +2': [4,0,11],'Brown Corporal': [0,0,20]}

bottom_table_armor = {'Empty': [0,0,0], 'Blue Jean Shorts': [0,0,2], 'Jean Capris': [0,0,5],
                      'Grey Thick Sweat Pants': [0,0,10], 'Ice Jeans': [0,0,13], 
                      'Brown Corporal Pants': [0,0,16], 'Warfare Pants': [0,0,19]}

gloves_table_armor = {'Empty': [0,0,0], 'Work Gloves': [0,0,2],'Work Gloves +1': [0,2,2], 
                      'Work Gloves +2': [0,4,2],
                      'Work Gloves +3': [0,6,2]}

shoes_table_armor = {'Empty': [0,0,0], 'Leather Sandals': [0,0,2], 'White Gomushin': [0,0,4], 
                     'Bronze Aroa Boots': [0,0,7], 'Red Whitebottom Shoes': [0,0,13]}

cape_table_armor = {'Empty': [0,0,0], 'Maple Cape': [0,0,5]}

weapon_table_attack = {'Sword': [0,17,0], 'Wooden Sword': [0,30,0], 'Wooden Sword +3': [3,36,0],'Aqua Snowboard': [0,30,0], 
                       'Spear': [0,32,0], 'Fork on a Stick': [0,37,0],'Iron Axe': [0,37,0], 'Fish Spear': [0,40,0],
                       'Fish Spear +1': [1,42,0], 'Maple Sword': [0,48,0],
                       'Cutlus': [0,52,0]}


#The game's variables
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
        self.playerInventory = []
        self.playerInventorySize = 12
        self.playerInventoryCount = 0

        self.expCount = [0]*60
        self.expMin = 0

        #Equipment
        self.playerWeapon = 'Sword'
        self.playerTop = 'White Undershirt'
        self.playerBottom = 'Blue Jean Shorts'
        self.playerGloves = 'Empty'
        self.playerHat = 'Empty'
        self.playerShoes = 'Leather Sandals'
        self.playerCape = 'Empty'

        self.playerArmor = hat_table_armor[self.playerHat][2] + top_table_armor[self.playerTop][2] + bottom_table_armor[self.playerBottom][2] + shoes_table_armor[self.playerShoes][2] + weapon_table_attack[self.playerWeapon][2] + gloves_table_armor[self.playerGloves][2] + cape_table_armor[self.playerCape][2]
        self.playerWA = hat_table_armor[self.playerHat][1] + top_table_armor[self.playerTop][1] + bottom_table_armor[self.playerBottom][1] + shoes_table_armor[self.playerShoes][1] + weapon_table_attack[self.playerWeapon][1] + gloves_table_armor[self.playerGloves][1] + cape_table_armor[self.playerCape][1]
        self.playerMaxDamage = int(self.playerWA * self.playerStrength * 4 / 100)

        #Skills
        self.powerStrikeCost = 10
        self.powerStrikeMultiplier = 2

        #Others
        self.timeCounter = 0

    def selectRightMob(self):
        if(len(monster_list)>self.mobCounter+1):
            self.mobCounter += 1
        self.currentEnemy = monster_list[self.mobCounter]
        self.monsterCurrentHP = monster_table[self.currentEnemy][1]
        self.monsterAttack = monster_table[self.currentEnemy][2]
        self.monsterLevel = monster_table[self.currentEnemy][0]

    def selectLeftMob(self):
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
        self.playerMaxHP += (14+int(self.playerStrength/10))
        self.playerHPRecovery = int(self.playerStrength/10)

    def monsterDie(self):
        if(self.isBoss == False):
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]
            self.currentEXP+= monster_table[self.currentEnemy][3]
            monster_table[self.currentEnemy][5]+=1
            self.expCount[self.expMin]=monster_table[self.currentEnemy][3]
            if self.currentEXP>= exp_to_next_level[self.playerLevel]:
                self.levelUp()
        else:
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
                        self.playerInventory.append(drop_table[self.currentEnemy][key])
                        print(str(len(self.playerInventory)))
                        self.playerInventoryCount += 1
                        break
                    else:
                        print('Your inventory is full. Please remove an item')
        else:
            self.playerMeso += random.randint(int(boss_table[self.currentEnemy][4]*2/3),boss_table[self.currentEnemy][4])
            lootRoll = random.randint(1,10000)
            for key in drop_table[self.currentEnemy]:
                if(key>lootRoll):
                    if(self.playerInventoryCount < self.playerInventorySize):
                        print('You looted',drop_table[self.currentEnemy][key])
                        self.playerInventory.append(drop_table[self.currentEnemy][key])
                        print(str(len(self.playerInventory)))
                        self.playerInventoryCount += 1
                        break
                    else:
                        print('Your inventory is full. Please remove an item')

    def damageRoll(self):
        self.playerMaxDamage = int(self.playerWA * self.playerStrength * 4 / 100)
        self.playerNextDamage = random.randint(1,self.playerMaxDamage)
        if self.playerNextDamage < self.playerMaxDamage / 10:
            self.playerNextDamage = int(self.playerMaxDamage / 10)


    def hitMonster(self):
        self.monsterCurrentHP -= self.playerNextDamage

    def recoverHP(self):
        if(self.playerCurrentHP<self.playerMaxHP):
            self.playerCurrentHP += self.playerHPRecovery
            if(self.playerCurrentHP>self.playerMaxHP):
                self.playerCurrentHP = self.playerMaxHP
        if(self.playerCurrentMP<self.playerMaxMP):
            self.playerCurrentMP += 1

    def takeDamage(self):
        self.playerDamageTaken = (random.randint(int(self.monsterAttack/2),self.monsterAttack) - self.playerArmor - int(self.playerStrength/10) - self.playerLevel + self.monsterLevel)
        if(self.playerDamageTaken<=0):
            self.playerDamageTaken = 1
        self.playerCurrentHP -= self.playerDamageTaken

    def playerDie(self):
        self.playerCurrentHP = 0
        self.playerIsDead = True
        if(self.isBoss == False):
            self.monsterCurrentHP = monster_table[self.currentEnemy][1]

    def proceed(self):
        self.expCount[self.expMin]=0
        self.recoverHP()
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
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Maple Idle")
        pygame.display.set_icon(pygame.image.load("leaf.png"))
        self.running = True

        self.mouse = pygame.mouse.get_pos()

    
    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = 0
                for item in self.GameState.playerInventory:
                    if int(width*0.8) <= self.mouse[0] <(width*0.95) and int(x*height*0.025) <= self.mouse[1] <= (int(x*height*0.025) + int(height*0.025)):
                        if(hat_table_armor.get(item)!=None):
                            if(self.GameState.playerHat == 'Empty'):
                                self.GameState.playerHat = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerHat
                                self.GameState.playerHat = item
                                self.GameState.playerInventory[x] = temp
                        elif(top_table_armor.get(item)!=None):
                            if(self.GameState.playerTop == 'Empty'):
                                self.GameState.playerTop = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerTop
                                self.GameState.playerTop = item
                                self.GameState.playerInventory[x] = temp
                        elif(bottom_table_armor.get(item)!=None):
                            if(self.GameState.playerBottom == 'Empty'):
                                self.GameState.playerBottom = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerBottom
                                self.GameState.playerBottom = item
                                self.GameState.playerInventory[x] = temp
                        elif(shoes_table_armor.get(item)!=None):
                            if(self.GameState.playerShoes == 'Empty'):
                                self.GameState.playerShoes = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerShoes
                                self.GameState.playerShoes = item
                                self.GameState.playerInventory[x] = temp
                        elif(weapon_table_attack.get(item)!=None):
                            if(self.GameState.playerWeapon == 'Empty'):
                                self.GameState.playerWeapon = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerWeapon
                                self.GameState.playerWeapon = item
                                self.GameState.playerInventory[x] = temp
                        elif(gloves_table_armor.get(item)!=None):
                            if(self.GameState.playerGloves == 'Empty'):
                                self.GameState.playerGloves = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerGloves
                                self.GameState.playerGloves = item
                                self.GameState.playerInventory[x] = temp
                        elif(cape_table_armor.get(item)!=None):
                            if(self.GameState.playerCape == 'Empty'):
                                self.GameState.playerCape = item
                                self.GameState.playerInventory.pop(x)
                                self.GameState.playerInventoryCount -= 1
                            else:
                                temp = self.GameState.playerCape
                                self.GameState.playerCape = item
                                self.GameState.playerInventory[x] = temp
                        self.GameState.playerArmor = hat_table_armor[self.GameState.playerHat][2] + top_table_armor[self.GameState.playerTop][2] + bottom_table_armor[self.GameState.playerBottom][2] + shoes_table_armor[self.GameState.playerShoes][2] + weapon_table_attack[self.GameState.playerWeapon][2] + gloves_table_armor[self.GameState.playerGloves][2] + cape_table_armor[self.GameState.playerCape][2]
                        self.GameState.playerWA = hat_table_armor[self.GameState.playerHat][1] + top_table_armor[self.GameState.playerTop][1] + bottom_table_armor[self.GameState.playerBottom][1] + shoes_table_armor[self.GameState.playerShoes][1] + weapon_table_attack[self.GameState.playerWeapon][1] + gloves_table_armor[self.GameState.playerGloves][1] + cape_table_armor[self.GameState.playerCape][1]
                    elif int(width*0.95) <= self.mouse[0] <(width) and int(x*height*0.025) <= self.mouse[1] <= (int(x*height*0.025) + int(height*0.025)):
                        self.GameState.playerInventory.pop(x)
                        self.GameState.playerInventoryCount -= 1
                    x += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_RIGHT:
                    if(self.GameState.isBoss == False):
                        self.GameState.selectRightMob()
                elif event.key == pygame.K_LEFT:
                    if(self.GameState.isBoss == False):
                        self.GameState.selectLeftMob()
                elif event.key == pygame.K_UP:
                    self.GameState.selectBossMob()
                elif event.key == pygame.K_DOWN:
                    self.GameState.isBoss = False
                    self.GameState.selectLeftMob()
                elif event.key == pygame.K_1:
                    if(not self.GameState.playerIsDead):
                        if(self.GameState.playerCurrentMP>= self.GameState.powerStrikeCost):
                            self.GameState.playerCurrentMP -= self.GameState.powerStrikeCost
                            damage = int(random.randint(int(self.GameState.playerMaxDamage / 10),self.GameState.playerMaxDamage)*self.GameState.powerStrikeMultiplier)
                            self.GameState.monsterCurrentHP -= damage
                            if(self.GameState.monsterCurrentHP <=0):
                                self.GameState.monsterDie()
                                self.GameState.loot()


    
    def update(self):
        self.GameState.proceed()

    def render(self):
        #Make screen white
        self.window.fill((255,255,255))

        #Player Stats Descriptors
        pygame.draw.rect(self.window,(192,192,192),(0,height-int(height*0.3),int(width*0.2),int(height*0.3)))

        text_level = self.font.render(('Level: '+str(self.GameState.playerLevel)), False, (0, 0, 0))
        self.window.blit(text_level,(0,int(height*0.71)))

        text_strength = self.font.render(('Strength: '+str(self.GameState.playerStrength)), False, (0, 0, 0))
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

        #Monster Text Descriptors
        pygame.draw.rect(self.window,(0,0,0),(int(width*0.7),int(height*0.44),width*0.15,height*0.03))
        if(self.GameState.isBoss == False):
            pygame.draw.rect(self.window,(255,0,0),(int(width*0.7),int(height*0.44),int(self.GameState.monsterCurrentHP/monster_table[self.GameState.currentEnemy][1]*width*0.15),height*0.03))
            text_enemy_hp = self.font.render(('HP: '+str(self.GameState.monsterCurrentHP)+'/'+str(monster_table[self.GameState.currentEnemy][1])), False, (255, 255, 255))
            self.window.blit(text_enemy_hp,(int(width*0.71),int(height*0.445)))

            text_enemy = self.font.render(('Monster: '+self.GameState.currentEnemy), False, (0, 0, 0))
            self.window.blit(text_enemy,(int(width*0.7),int(height*0.475)))

            text_enemy_lvl = self.font.render(('Level: '+str(self.GameState.monsterLevel)), False, (0, 0, 0))
            self.window.blit(text_enemy_lvl,(int(width*0.7),int(height*0.50)))

            text_enemy_att = self.font.render(('Attack: '+str(self.GameState.monsterAttack)), False, (0, 0, 0))
            self.window.blit(text_enemy_att,(int(width*0.7),int(height*0.525)))

            text_enemy_exp = self.font.render(('Exp: '+str(monster_table[self.GameState.currentEnemy][3])), False, (0, 0, 0))
            self.window.blit(text_enemy_exp,(int(width*0.7),int(height*0.55)))

            text_enemy_meso = self.font.render(('Meso: '+str(int(monster_table[self.GameState.currentEnemy][4]*2/3))+'-'+str(monster_table[self.GameState.currentEnemy][4])), False, (0, 0, 0))
            self.window.blit(text_enemy_meso,(int(width*0.7),int(height*0.575)))

            text_enemy_kc = self.font.render(('Kill Count: '+str(monster_table[self.GameState.currentEnemy][5])), False, (0, 0, 0))
            self.window.blit(text_enemy_kc,(int(width*0.7),int(height*0.60)))
        else:
            pygame.draw.rect(self.window,(255,0,0),(int(width*0.7),int(height*0.44),int(self.GameState.monsterCurrentHP/boss_table[self.GameState.currentEnemy][1]*width*0.15),height*0.03))
            text_enemy_hp = self.font.render(('HP: '+str(self.GameState.monsterCurrentHP)+'/'+str(boss_table[self.GameState.currentEnemy][1])), False, (255, 255, 255))
            self.window.blit(text_enemy_hp,(int(width*0.71),int(height*0.445)))

            text_enemy = self.font.render(('Monster: '+self.GameState.currentEnemy), False, (0, 0, 0))
            self.window.blit(text_enemy,(int(width*0.7),int(height*0.475)))

            text_enemy_lvl = self.font.render(('Level: '+str(self.GameState.monsterLevel)), False, (0, 0, 0))
            self.window.blit(text_enemy_lvl,(int(width*0.7),int(height*0.50)))

            text_enemy_att = self.font.render(('Attack: '+str(self.GameState.monsterAttack)), False, (0, 0, 0))
            self.window.blit(text_enemy_att,(int(width*0.7),int(height*0.525)))

            text_enemy_exp = self.font.render(('Exp: '+str(boss_table[self.GameState.currentEnemy][3])), False, (0, 0, 0))
            self.window.blit(text_enemy_exp,(int(width*0.7),int(height*0.55)))

            text_enemy_meso = self.font.render(('Meso: '+str(int(boss_table[self.GameState.currentEnemy][4]*2/3))+'-'+str(boss_table[self.GameState.currentEnemy][4])), False, (0, 0, 0))
            self.window.blit(text_enemy_meso,(int(width*0.7),int(height*0.575)))

            text_enemy_kc = self.font.render(('Kill Count: '+str(boss_table[self.GameState.currentEnemy][5])), False, (0, 0, 0))
            self.window.blit(text_enemy_kc,(int(width*0.7),int(height*0.60)))

        text_expmin = self.font.render(('Exp/Min: '+str(sum(self.GameState.expCount))), False, (0, 0, 0))
        self.window.blit(text_expmin,(int(width*0.7),int(height*0.65)))

        #Player Descriptors
        pygame.draw.rect(self.window,(0,0,0),(int(width*0.2),int(height*0.44),width*0.15,height*0.03))
        pygame.draw.rect(self.window,(255,0,0),(int(width*0.2),int(height*0.44),int(self.GameState.playerCurrentHP/self.GameState.playerMaxHP*width*0.15),height*0.03))
        text_player = self.font.render(('Player'), False, (0, 0, 0))
        self.window.blit(text_player,(int(width*0.2),int(height*0.475)))
        text_player_hp = self.font.render(('HP: ' + str(self.GameState.playerCurrentHP)+ '/'+str(self.GameState.playerMaxHP)), False, (255, 255, 255))
        self.window.blit(text_player_hp,(int(width*0.21),int(height*0.445)))
        text_player_mp = self.font.render(('MP: ' + str(self.GameState.playerCurrentMP) + '/' + str(self.GameState.playerMaxMP)), False, (0, 0, 0))
        self.window.blit(text_player_mp,(int(width*0.2),int(height*0.50)))

        #Floating Damage Descriptors
        text_player_damage = self.font.render(('-' + str(self.GameState.playerNextDamage)), False, (255, 0, 0))
        self.window.blit(text_player_damage,(int(width*0.7),int(height*0.4)))
        text_monster_damage = self.font.render(('-' + str(self.GameState.playerDamageTaken)), False, (255, 0, 0))
        self.window.blit(text_monster_damage,(int(width*0.2),int(height*0.4)))

        text_player_rec = self.font.render(('+' + str(self.GameState.playerHPRecovery)), False, (0, 50, 255))
        self.window.blit(text_player_rec,(int(width*0.2),int(height*0.35)))


        #Current Equips
        text_equips = self.font.render('Equipment',False,(0,0,0))
        self.window.blit(text_equips, ((int(width*0.01)),height*0.01))
        text_hat = self.font.render('Hat: ' + self.GameState.playerHat,False,(0,0,0))
        self.window.blit(text_hat, ((int(width*0.01)),height*0.035))
        text_top = self.font.render('Top: ' + self.GameState.playerTop,False,(0,0,0))
        self.window.blit(text_top, ((int(width*0.01)),height*0.06))
        text_bottom = self.font.render('Bottom: ' + self.GameState.playerBottom,False,(0,0,0))
        self.window.blit(text_bottom, ((int(width*0.01)),height*0.085))
        text_gloves = self.font.render('Gloves: ' + self.GameState.playerGloves,False,(0,0,0))
        self.window.blit(text_gloves, ((int(width*0.01)),height*0.11))
        text_shoes = self.font.render('Shoes: ' + self.GameState.playerShoes,False,(0,0,0))
        self.window.blit(text_shoes, ((int(width*0.01)),height*0.135))
        text_cape = self.font.render('Cape: ' + self.GameState.playerCape,False,(0,0,0))
        self.window.blit(text_cape, ((int(width*0.01)),height*0.16))
        text_weapon = self.font.render('Weapon: ' + self.GameState.playerWeapon,False,(0,0,0))
        self.window.blit(text_weapon, ((int(width*0.01)),height*0.185))


        
        #Inventory
        x = 0
        for item in self.GameState.playerInventory:
            pygame.draw.rect(self.window,(192,192,192),(int(width*0.8),int(x*height*0.025),int(width*0.20),int(height*0.025)))

            if int(width*0.8) <= self.mouse[0] <(width*0.95) and int(x*height*0.025) <= self.mouse[1] <= (int(x*height*0.025) + int(height*0.025)):
                pygame.draw.rect(self.window,(128,128,128),(int(width*0.8),int(x*height*0.025),int(width*0.20),int(height*0.025)))
                pygame.draw.rect(self.window,(192,192,192),(int(width*0.65),int(x*height*0.025),int(width*0.15),int(height*0.075)))
                if(hat_table_armor.get(item)!=None):
                    equip_str = hat_table_armor[item][0]
                    equip_wa = hat_table_armor[item][1]
                    equip_armor = hat_table_armor[item][2]
                elif(top_table_armor.get(item)!=None):
                    equip_str = top_table_armor[item][0]
                    equip_wa = top_table_armor[item][1]
                    equip_armor = top_table_armor[item][2]
                elif(bottom_table_armor.get(item)!=None):
                    equip_str = bottom_table_armor[item][0]
                    equip_wa = bottom_table_armor[item][1]
                    equip_armor = bottom_table_armor[item][2]
                elif(gloves_table_armor.get(item)!=None):
                    equip_str = gloves_table_armor[item][0]
                    equip_wa = gloves_table_armor[item][1]
                    equip_armor = gloves_table_armor[item][2]
                elif(shoes_table_armor.get(item)!=None):
                    equip_str = shoes_table_armor[item][0]
                    equip_wa = shoes_table_armor[item][1]
                    equip_armor = shoes_table_armor[item][2]
                elif(cape_table_armor.get(item)!=None):
                    equip_str = cape_table_armor[item][0]
                    equip_wa = cape_table_armor[item][1]
                    equip_armor = cape_table_armor[item][2]
                elif(weapon_table_attack.get(item)!=None):
                    equip_str = weapon_table_attack[item][0]
                    equip_wa = weapon_table_attack[item][1]
                    equip_armor = weapon_table_attack[item][2]
                item_strength = self.font.render(('Str: ' + str(equip_str)), False, (0, 0, 0))
                self.window.blit(item_strength,(int(width*0.65),int(x*height*0.025)))
                item_WA = self.font.render(('WA: ' + str(equip_wa)), False, (0, 0, 0))
                self.window.blit(item_WA,(int(width*0.65),int(x*height*0.025)+int(height*0.025)))
                item_armor = self.font.render(('Armor: ' + str(equip_armor)), False, (0, 0, 0))
                self.window.blit(item_armor,(int(width*0.65),int(x*height*0.025)+int(height*0.05)))
            elif int(width*0.95) <= self.mouse[0] <=(width) and int(x*height*0.025) <= self.mouse[1] <= (int(x*height*0.025) + int(height*0.025)):
                pygame.draw.rect(self.window,(255,0,0),(int(width*0.95),int(x*height*0.025),int(width*0.05),int(height*0.025)))
                pygame.draw.rect(self.window,(255,0,0),(int(width*0.65),int(x*height*0.025),int(width*0.15),int(height*0.025)))
                item_delete = self.font.render(('Press to Delete: '), False, (0, 0, 0))
                self.window.blit(item_delete,(int(width*0.65),int(x*height*0.025)))
            item_name = self.font.render((item), False, (0, 0, 0))
            self.window.blit(item_name,(int(width*0.8),int(x*height*0.025)))
            x+=1


        pygame.display.update()

    def run(self):
        while self.running:
            self.mouse = pygame.mouse.get_pos()
            self.processInput()
            if(self.GameState.timeCounter %1 == 0):
                self.update()
            self.render()
            self.GameState.timeCounter += 1
            self.GameState.expMin += 1
            if(self.GameState.expMin == 60):
                self.GameState.expMin = 0
            pygame.time.wait(50)
            self.clock.tick(60)

UserInterface = UserInterface()
UserInterface.run()
