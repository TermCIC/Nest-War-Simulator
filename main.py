from species import *
import random
import time

print('築巢大戰模擬開始。')

name = '測試者'
player = player(name)
player.win()

player.spawn()
player.spawn()
player.spawn()
player.spawn()

round = 0
t = 0

while True:
    print('回合 {}'.format(round))
    sCF = 0
    sOF = 0
    sNK = 0
    sSH = 0
    sSF = 0
    sCD = 0
    sHS = 0
    sPN = 0
    player.win()
    player.card()
    player.status()
    player.checkwin()
    player.showstatus()
    if player.winstatus == 1:
        if player.species == 'Coptotermes formosanus':
            sCF = round
        elif player.species == 'Odontotermes formosanus':
            sOF = round
        elif player.species == 'Nasutitermes koshunensis':
            sNK = round
        elif player.species == 'Stylotermes halumicus':
            sSH = round
        elif player.species == 'Prorhinotermes flavus':
            sSF = round
        elif player.species == 'Cryptotermes domesticus':
            sCD = round
        elif player.species == 'Hodotermopsis sjoestedti':
            sHS = round
        elif player.species == 'Pericapritermes nitobei':
            sPN = round
        player.reset()
        round = 0
        data = '{},{},{},{},{},{},{},{}'.format(sCF, sOF, sNK, sSH, sSF, sCD, sHS, sPN)
        file = open('D:/data.csv', 'a')
        file.write(data + "\n")
        file.close()

    else:
        round += 1


