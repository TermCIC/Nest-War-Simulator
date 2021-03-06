
import random

resource = ['劣質木材'] * 20 + ['中等木材'] * 10 + ['優質木材'] * 5 + ['土壤'] * 15 + ['水源'] * 5
disaster = ['螞蟻攻擊'] * 8 + ['白蟻攻擊'] * 4 + ['寒冷氣候'] * 4 + ['乾燥氣候'] * 2 + ['都市開發'] * 4 + ['盲蛇入侵'] * 2 + ['穿山甲入侵'] * 1
event = ['分飛'] * 10 + ['資源掠奪'] * 10 + ['有效溝通'] * 10
termitephile = ['寄生真菌'] * 5 + ['蟻蟋'] * 5
eventList = resource + disaster + event + termitephile
castes = ['工蟻']*1 + ['兵蟻']*1

# the list of termite species in game
speciesList = ['Coptotermes formosanus',
               'Odontotermes formosanus',
               'Nasutitermes koshunensis',
               'Stylotermes halumicus',
               'Prorhinotermes flavus',
               'Cryptotermes domesticus',
               'Hodotermopsis sjoestedti',
               'Pericapritermes nitobei']

# define the species class
class player:
    def __init__(self, name):
        self.name = name
        self.resource = []
        self.wood = 0
        self.soil = 0
        self.water = 0
        self.cold = 0
        self.workerMult = 1
        self.soldierMult = 1
        self.termite = []
        self.workerN = 0
        self.soldierN = 0
        self.species = ''
        self.winstatus = 0
        self.woodWin = 0
        self.soilWin = 0
        self.waterWin = 0
        self.coldWin = 0

    def reset(self):
        self.termite = []
        self.resource = []
        self.select()
        self.spawn()
        self.spawn()
        self.spawn()
        self.spawn()

    def select(self):
        self.species = random.choice(speciesList)

    # how to win the game
    def win(self):
        if self.species == 'Coptotermes formosanus':
            self.woodWin = 5
            self.soilWin = 0
            self.waterWin = 1
            self.coldWin = 0
        elif self.species == 'Odontotermes formosanus':
            self.woodWin = 4
            self.soilWin = 2
            self.waterWin = 0
            self.coldWin = 0
        elif self.species == 'Nasutitermes koshunensis':
            self.woodWin = 6
            self.soilWin = 0
            self.waterWin = 0
            self.coldWin = 0
        elif self.species == 'Stylotermes halumicus':
            self.woodWin = 5
            self.soilWin = 0
            self.waterWin = 1
            self.coldWin = 0
        elif self.species == 'Prorhinotermes flavus':
            self.woodWin = 5
            self.soilWin = 0
            self.waterWin = 1
            self.coldWin = 0
        elif self.species == 'Cryptotermes domesticus':
            self.woodWin = 5
            self.soilWin = 0
            self.waterWin = 0
            self.coldWin = 0
        elif self.species == 'Hodotermopsis sjoestedti':
            self.woodWin = 4
            self.soilWin = 0
            self.waterWin = 0
            self.coldWin = 1
        elif self.species == 'Pericapritermes nitobei':
            self.woodWin = 2
            self.soilWin = 4
            self.waterWin = 0
            self.coldWin = 0


    # check whether the player wins
    def checkwin(self):
        if self.wood >= self.woodWin and self.water >= self.waterWin and self.soil >= self.soilWin and self.cold >= self.coldWin:
            print('You win!')
            self.winstatus = 1
        else:
            self.winstatus = 0

    # lost card, triggered by event
    def lost(self, target):
        if target == "all":
            if len(self.resource) > 0 and len(self.termite) > 0:
                goto = random.choice(['資源卡', '白蟻卡'])
                if goto == '資源卡':
                    lostCard = random.choice(self.resource)
                    self.resource.remove(lostCard)
                    print('你損失了一張{}'.format(lostCard))
                if goto == '白蟻卡':
                    lostCard = random.choice(self.termite)
                    self.termite.remove(lostCard)
                    print('你損失了一張{}'.format(lostCard))
            elif len(self.resource) > 0 and len(self.termite) == 0:
                lostCard = random.choice(self.resource)
                self.resource.remove(lostCard)
                print('你損失了一張{}'.format(lostCard))
            elif len(self.resource) == 0 and len(self.termite) > 0:
                lostCard = random.choice(self.termite)
                self.termite.remove(lostCard)
                print('你損失了一張{}'.format(lostCard))
            else:
                print('你沒有資源可以損失。')

        elif target == "resource":
            if len(self.resource) > 0:
                lostCard = random.choice(self.resource)
                self.resource.remove(lostCard)
                print('你損失了一張{}'.format(lostCard))
            else:
                print('你沒有資源可以損失。')

        elif target == 'termite':
            if len(self.termite) > 0:
                lostCard = random.choice(self.termite)
                self.termite.remove(lostCard)
                print('你損失了一張{}'.format(lostCard))
            else:
                print('你沒有資源可以損失。')

    def spawn(self):
        newTermite = random.choice(castes)
        self.termite.append(random.choice(castes))
        print('你獲得了一個新的 {}'.format(newTermite))


    def passturn(self):
        print('你略過了這個回合。')
        pass


    def robber(self):
        print('目前尚未開放這個功能。')


    def caste(self):
        if len(self.termite) > 0:
            for i in self.termite:
                self.termite.remove(i)
                self.termite.append(random.choice(castes))
        else:
            print('你沒有足夠的白蟻能轉換階級。')


    def card(self):
        cardName = random.choice(eventList)
        print('你抽到了 {}。'.format(cardName))
        if cardName in resource:
            cardType = '資源卡'
            if cardName == '劣質木材':
                if self.workerN >= 2:
                    self.resource.append('劣質木材')
                    print('你獲得了一個單位的 劣質木材。')
                else:
                    print('你的工蟻不足，無法採集 劣質木材。')
            elif cardName == '中等木材':
                if self.workerN >= 3:
                    self.resource.append('中等木材')
                    print('你獲得了一個單位的 中等木材。')
                else:
                    print('你的工蟻不足，無法採集 中等木材。')
            elif cardName == '優質木材':
                if self.workerN >= 5:
                    self.resource.append('優質木材')
                    print('你獲得了一個單位的 優質木材。')
                else:
                    print('你的工蟻不足，無法採集 優質木材。')
            elif cardName == '土壤':
                if self.workerN >= 3:
                    self.resource.append('土壤')
                    print('你獲得了一個單位的 土壤。')
                else:
                    print('你的工蟻不足，無法採集 土壤。')
            elif cardName == '水源':
                if self.workerN >= 2:
                    self.resource.append('水源')
                    print('你獲得了一個單位的 水源。')
                else:
                    print('你的工蟻不足，無法採集 水源。')
        elif cardName in disaster:
            cardType = '災難卡'
            if cardName == '螞蟻攻擊':
                if self.soldierN < 2:
                    self.lost('all')
                else:
                    print('你有足夠的兵蟻防禦 螞蟻攻擊。')

            elif cardName == '白蟻攻擊':
                if self.soldierN < 2:
                    self.lost('resource')
                else:
                    print('你有足夠的兵蟻防禦 白蟻攻擊。')

            elif cardName == '寒冷氣候':
                if self.species == 'Hodotermopsis sjoestedti':
                    self.resource.append('寒冷氣候')
                    print('你獲得了一個單位的 寒冷氣候。')
                else:
                    self.lost('termite')

            elif cardName == '乾燥氣候':
                if self.species == 'Cryptotermes domesticus':
                    print('你不受 乾燥氣候 影響。')
                else:
                    self.lost('termite')

            elif cardName == '都市開發':
                if self.species == 'Coptotermes formosanus':
                    self.spawn()
                else:
                    self.passturn()

            elif cardName == '盲蛇入侵':
                self.lost('all')

            elif cardName == '穿山甲入侵':
                goto = random.choice(['資源卡', '白蟻卡'])
                if goto == '資源卡':
                    while len(self.resource) > 0:
                        self.lost('resource')
                elif goto == '白蟻卡':
                    self.lost('termite')
                    self.lost('termite')

        elif cardName in event:
            cardType = '事件卡'
            if cardName == '分飛':
                self.spawn()

            elif cardName == '資源掠奪':
                print('目前尚未開放這個功能。')

            elif cardName == '有效溝通':
                self.caste()

        elif cardName in termitephile:
            cardType = '蟻客卡'
            print('本功能尚未開放。')

    def status(self):
        self.workerN = self.termite.count('工蟻') * self.workerMult
        self.soldierN = self.termite.count('兵蟻') * self.soldierMult
        self.wood = self.resource.count('劣質木材') + self.resource.count('中等木材')*2 + self.resource.count('優質木材')*3
        self.soil = self.resource.count('土壤')
        self.water = self.resource.count('水源')
        self.cold = self.resource.count('寒冷氣候')

    def showstatus(self):
        print(
            '你的物種為 {}。'.format(
                self.species))
        print(
            '你的勝利條件為 {} 單位木材、{} 單位土壤、{} 單位水、及 {} 單位寒冷。'.format(
                self.woodWin, self.soilWin, self.waterWin, self.coldWin))
        print(
            '你目前有 {} 單位木材、{} 單位土壤、{} 單位水、及 {} 單位寒冷。'.format(
                self.wood, self.soil, self.water, self.cold))
        print(
            '你目前有 {} 頭工蟻、及 {} 頭兵蟻。'.format(
                self.workerN, self.soldierN))



