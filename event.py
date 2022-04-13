from species import *
from event import *
import random

# the list of event cards
resource = ['劣質木材'] * 20 + ['中等木材'] * 10 + ['優質木材'] * 5 + ['土壤'] * 15 + ['水源'] * 5
disaster = ['螞蟻攻擊'] * 8 + ['白蟻攻擊'] * 4 + ['寒冷氣候'] * 4 + ['乾燥氣候'] * 2 + ['都市開發'] * 4 + ['盲蛇入侵'] * 2 + ['穿山甲入侵'] * 1
event = ['分飛'] * 10 + ['資源掠奪'] * 10 + ['有效溝通'] * 10
termitephile = ['寄生真菌'] * 5 + ['蟻蟋'] * 5

eventList = resource + disaster + event + termitephile
print(eventList)


def card(cardName):
    print(cardName)
    if cardName in resource:
        cardType = '資源卡'
        if cardName == '劣質木材':
            if player.workerN >= 2:
                player.resource.append('劣質木材')
                print('你獲得了一個單位的 劣質木材。')
            else:
                print('你的工蟻不足，無法採集 劣質木材。')
        elif cardName == '中等木材':
            if player.workerN >= 3:
                player.resource.append('中等木材')
                print('你獲得了一個單位的 中等木材。')
            else:
                print('你的工蟻不足，無法採集 中等木材。')
        elif cardName == '優質木材':
            if player.workerN >= 5:
                player.resource.append('優質木材')
                print('你獲得了一個單位的 優質木材。')
            else:
                print('你的工蟻不足，無法採集 優質木材。')
        elif cardName == '土壤':
            if player.workerN >= 3:
                player.resource.append('土壤')
                print('你獲得了一個單位的 土壤。')
            else:
                print('你的工蟻不足，無法採集 土壤。')
        elif cardName == '水源':
            if player.workerN >= 2:
                player.resource.append('水源')
                print('你獲得了一個單位的 水源。')
            else:
                print('你的工蟻不足，無法採集 水源。')
    elif cardName in disaster:
        cardType = '災難卡'
        if cardName == '螞蟻攻擊':
            if player.soldierN < 2:
                player.lost('all')
            else:
                print('你有足夠的兵蟻防禦 螞蟻攻擊。')

        elif cardName == '白蟻攻擊':
            if player.soldierN < 2:
                player.lost('resource')
            else:
                print('你有足夠的兵蟻防禦 白蟻攻擊。')

        elif cardName == '寒冷氣候':
            if player.species == 'Hodotermopsis sjoestedti':
                player.resource += '寒冷氣候'
                print('你獲得了一個單位的 寒冷氣候。')
            else:
                player.lost('termite')

        elif cardName == '乾燥氣候':
            if player.species == 'Cryptotermes domesticus':
                print('你不受 乾燥氣候 影響。')
            else:
                player.lost('termite')

        elif cardName == '都市開發':
            if player.species == 'Coptotermes formosanus':
                player.spawn()
            else:
                player.passturn()

        elif cardName == '盲蛇入侵':
            player.lost('all')

        elif cardName == '穿山甲入侵':
            goto = random.choice(['資源卡', '白蟻卡'])
            if goto == '資源卡':
                while len(player.resource) > 0:
                    player.lost('resource')
            elif goto == '白蟻卡':
                player.lost('termite')
                player.lost('termite')

    elif cardName in event:
        cardType = '事件卡'
        if cardName == '分飛':
            player.spawn()

        elif cardName == '資源掠奪':
            print('目前尚未開放這個功能。')

        elif cardName == '有效溝通':
            player.caste()

    elif cardName in termitephile:
        cardType = '蟻客卡'
        print('本功能尚未開放。')
