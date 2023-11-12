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

# -------------------------------
# Create Deck of Cards
# -------------------------------

originalDeck = []

with open ('/Users/devpatel/Documents/GitHub/BlackJack/deckofcards.txt', 'r') as file:
    lines = file.readlines()
    
    card_list = [line.strip() for line in lines]
    
    for card in card_list:
        card = card.split('|')
        originalDeck.append(card)

currentDeck = originalDeck


value = random.choice(currentDeck)

del value
    #print(originalDeck)

# ----------------------------------
# Player Data Class
# ----------------------------------

class Players():
    
    def __init__(self, name, points=100):
        self.name = name 
        self.points = points
        
    def __str__(self):
        return(f'Player Name: {self.name} | Points: {self.points}')
        
    def get_points(self):
        return self.points
    
    def update_points(self, points):
        self.points = points
        
    # print(playerList[0].get_points())

    # playerList[0].update_points(90)

    # print(playerList[0].get_points())
    
# --------------------------------
# Card Display Function
# --------------------------------

def displayCard():
        type = '♠'
        
        card = [
                [' -','-','-','-','-', '-','-'],
                ['|    ', '', '', '',  f'    {type}|'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '7', '', '    |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                ['|    ', '', '', '', '     |'],
                [f'|{type}    ', '', '', '', '    |'],
                [' -','-','-','-','-','-','-']
                
               ]

        for row in card:
            print(' '.join(row))
        
displayCard()

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
    'SPADE' : 'S',
    'DIAMOND': 'D',
    'CLUB' : 'C',
    'HEART' : 'H',
}

# ----------------------------------
# Create Player Instance
# ----------------------------------

numberofPlayers = int(input('Enter number of players: '))

playerList = []

for i in range(1, numberofPlayers+1):
    playerName = input(f'Enter Player {i} Name: ')
    playerObj = Players(playerName)
    playerList.append(playerObj)
    
for player in playerList:
    print(player)
    