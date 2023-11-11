'''
CPS 109 - Assignment
Project Name : BlackJack
Developed By : Dev Patel
Student ID   : //
Section No.  :  
'''

# ----------------------------------
# Libraries/Modules
# ----------------------------------

import random

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
    
    #print(originalDeck)

    
# --------------------------------
# Giving Values to Royal Cards
# --------------------------------

royalValues = {
    'A':11,
    'K': 10,
    'Q':10,
    'J':10,
}

#print(royalValues['K']) == 10

# -------------------------------
# Cards in Current Round
# -------------------------------