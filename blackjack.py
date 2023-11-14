'''
CPS 109 - Assignment
Project Name : BlackJack
Developed By : Dev Patel
Student ID   : //
Section No.  : 4
'''

# ----------------------------------
# Libraries/Modules
# ----------------------------------

import random
import getpass

# ------------------------------------
# Create Deck of Cards (File Import)
# ------------------------------------

originalDeck = []

with open ('deckofcards.txt', 'r') as file:
    lines = file.readlines()
    
    card_list = [line.strip() for line in lines]
    
    for card in card_list:
        card = card.split('|')
        originalDeck.append(card)

currentDeck = list(originalDeck)


value = random.choice(currentDeck)
#print(value)


# ----------------------------------
# Player Data Class
# ----------------------------------

class Players():
    
    def __init__(self, name, points = 100, currentBet=0, roundSum = 0):
        self.name = name 
        self.points = points
        self.currentBet = currentBet
        self.roundSum = 0

    def __str__(self):
        #return(f'Player Name: {self.name} | Points: {self.points}')
        return(f'Player Name: {self.name} | Points: {self.points} | Bet: {self.currentBet}')
        
    def get_points(self):
        return self.points
    
    def update_points(self, points):
        self.points = points

    def get_bet(self):
        return self.currentBet
    
    def update_bet(self, currentBet):
        self.currentBet = currentBet
    
    def update_cardSum(self, roundSum):
        self.roundSum += roundSum

    def reset_cardSum(self):
        self.roundSum = 0
    
    def get_roundSum(self):
        return self.roundSum

    # print(playerList[0].get_points())

    # playerList[0].update_points(90)

    # print(playerList[0].get_points())
    
# --------------------------------
# Card Display Function
# --------------------------------

def displayCard(value, type):
        
        space = ' '
        
        if value[2] == '10':
            space = ''
        
        
        card = [
                [' -','-','-','-','-', '-','-'],
                ['|    ', '', '', '',  f'    {type}|'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', f'{value[2]}', '', f'   {space}|'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                [f'|{type}    ', '', '', '', '    |'],
                [' -','-','-','-','-','-','-']
                
               ]

        for row in card:
            print(' '.join(row))
        
#displayCard()

# --------------------------------
# Reset Deck for New Round
# --------------------------------
def resetCards(originalDeck, currentDeck):
    
    currentDeck = list(originalDeck)


    return currentDeck
    

# --------------------------------
# Giving Values to Royal Cards
# --------------------------------

CardValues = {
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1
    
}

#print(royalValues['K']) == 10

# ----------------------------------
# Card Symbols to Name for Display
# ----------------------------------

Suit = {
    'SPADE' : '♠',
    'DIAMOND': '♦',
    'CLUB' : '♣',
    'HEART' : '♥'
}

# type = Suit.get(value[1])
# print(type)

# displayCard(value, type)

# ----------------------------------
# Create Player Instance
# ----------------------------------

def playerSetup(playerList):
    numberofPlayers = int(input('Enter number of players playing: '))

    for i in range(1, numberofPlayers+1):
        playerName = input(f'Enter Player {i} Name: ')
        playerObj = Players(playerName)
        playerList.append(playerObj)
        
    
    return playerList


def main():
    
    print('')
    print('Welcome to Blackjack in Python!')
    print('')
    print('Press Enter/Return to start playing!')
    
    beginGame = getpass.getpass(prompt='', stream=None)

    if not beginGame:
        playerList = []
        gameRunning = True
        round = 0
        

        playerSetup(playerList)
        
        for player in playerList:
            print(player)
        
        print('')
        
        while gameRunning:
            

            print(f'Begin Game?')
            
            print('Enter to Continue!')
            print('Any other key to end game and get final scores!')
            
            beginRound = input()
            
            if not beginRound:
                round += 1
                pot = 0
                
                for i in range(0, len(playerList)):
                    
                    if playerList[i].get_points() >= 1:
                        
                        print(f'{playerList[i].name}, it\'s your turn!')
                        print(f'You currently have {playerList[i].get_points()} points!')
                        playerList[i].update_bet(int(input('How much would you like to bet?: ')))
                        print('')
                        
                        if playerList[i].get_bet() > playerList[i].get_points():
                            playerList[i].update_bet(playerList[i].get_points())
                            print('')
                            print(f'Your bet has been set to {playerList[i].get_bet()} since you didn\'t have enough points!')
                        
                        playerList[i].update_points(playerList[i].get_points() - playerList[i].get_bet())
                        pot += playerList[i].get_bet()

                        print(playerList[i])
                        print('')
                    else:
                        print('')
                        print(f'{playerList[i].name}, you do not have any remaining points!')
                    
                
                
                print('-'*30) 
                print(f'Round {round} started!')
                print(f'Current Pot is {pot} tokens!')

                for i in range(0, len(playerList)):

                    if playerList[i].get_bet() == 0:
                        continue

                    else:
                        print('')
                        print(f'{playerList[i].name}, your turn! ')
                        print('')
                        
                        Flag = True
    

                        while Flag == True:
                            value = random.choice(currentDeck)
                            print(value)
                            type = Suit.get(value[1]) 
                            currentDeck.remove(value)
                        
                            playerList[i].update_cardSum(CardValues[value[2]])
                            #print(playerList[i].get_roundSum())
                            displayCard(value, type)



                            if playerList[i].get_roundSum() == 21:
                                print('Nice! You Hit 21! Let\'s see how the dealer does!')
                                print('')
                                break

                            elif playerList[i].get_roundSum() > 21:
                                
                                print('Bust! You\'ve went over 21! Better luck next round!')
                                print('')
                                break
                                
                            
                            flag2 = input(f'Your sum is {playerList[i].get_roundSum()}! Hit or Stand? (H/S) ')

                            if flag2 == 'S':
                                Flag = False

                        if playerList[i].get_roundSum() < 21:     
                            print(f'{playerList[i].name}, your total is {playerList[i].get_roundSum()}!')
                        print('-'*30)
                        print('-'*30)
            else:
                break
    else:
        print('Have a good day!')
        
if __name__ == '__main__':
    main()
    
    