'''
CPS 109 - Assignment
Project Name : BlackJack
Developed By : Dev Patel
Section No.  : 4
'''

# ----------------------------------
# Problem/Program Description
# ----------------------------------

'''

The problem/program I've decided to work on to showcase my python skills and abilities
for this assignment is to simulate the card-game "BlackJack". 

In order to simulate this card-game, the sub-problems include but are not limited to the following:
    
    i) Deck of Cards
        ↳ Card-Randomizer | (Use "random" library to randomly select a card from the deck)
            ↳ Assigning Values to Royals (A, K, Q, J) | (Assign values through dictionary (type(str) : type(int)))
                ↳ Removing Card from Deck | (Once a card is selected it should no longer be in the deck. Remove itself.)
                    ↳ Reset Deck (NEW ROUND) | (Reset round deck back to original deck which was from reading the file)
                    
    ii) Player Data (Class)
        ↳ Dynamically Store and Read Data (BASED ON # OF PEOPLE) | (Create a new instance for each player registered)
            ↳ Player Tokens | (Hold token data --> Assign each player to their own amount of tokens)
                ↳ Round Betting System | (Track the players bet for the round)
                    ↳ Card Total System | (Track the sum of the cards they picked up throughout the round)
                    
    iii) Card Display
        ↳ Template for Display | (Blank template of a card for display)
            ↳ Dynamically Center Value | (For example, 10 is the only card with 2 characters. Need to consider spacing)
                ↳ Suit Display (HEART/SPADE/CLUB/DIAMOND) | (Select the suit from the random card)
                
    iv) Token System
        ↳ Token Distribution (Arithemetic Operations) | (Adder/Subtractor and BlackJack Multiplier)
        
    v) Game History
        ↳ Store Round Data (Build Game History) --> Output to a File!
    
'''

# ----------------------------------
# Libraries/Modules
# ----------------------------------

import random

# ------------------------------------
# Create Deck of Cards (File Input)
# ------------------------------------

originalDeck = []

with open ('deckofcards.txt', 'r') as file:
    lines = file.readlines()
    
    card_list = [line.strip() for line in lines]
    
    for card in card_list:
        card = card.split('|')
        originalDeck.append(card)
        
# ------------------------------------
# Round Statistics (File Output)
# ------------------------------------

resultsOutput = open("results.txt", "a+")

resultsOutput.write('BlackJack Game History | Developed by Dev Patel\n')

# ----------------------------------
# Player Data Class
# ----------------------------------

class Players():
    
    def __init__(self, name, points = 100, currentBet=0, roundSum = 0):
        self.name = name 
        self.points = points
        self.currentBet = currentBet
        self.roundSum = roundSum

    def __str__(self):
        #return(f'Player Name: {self.name} | Points: {self.points}')
        return(f'Player Name: {self.name} | Tokens: {self.points} | Bet: {self.currentBet}')
        
    def get_points(self):
        return self.points
    
    def update_points(self, points):
        self.points = points

    def get_bet(self):
        return self.currentBet
    
    def update_bet(self, currentBet):
        self.currentBet = currentBet
    
    def reset_bet(self, currentBet=0):
        self.currentBet = currentBet
    
    def update_cardSum(self, roundSum):
        self.roundSum += roundSum

    def reset_roundSum(self, roundSum=0):
        self.roundSum = roundSum
    
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
# Giving Values to Cards
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
    
    invalidInput = True
    invalidName = True
    
    while invalidInput:
        
        try:
            numberofPlayers = int(input('Enter number of players playing: '))
            print('')
            if numberofPlayers <= 0:
                raise ValueError
        except ValueError:
            print('Make sure to enter an integer above 0! You can\'t play a game with no one!')
            print('')
            invalidInput = True
        else:
            invalidInput = False
            
    for i in range(1, numberofPlayers+1):
        
        while invalidName:
            
            try:
                playerName = input(f'Enter Player {i} Name: ')
                    
                if not playerName:
                    raise EOFError
                
            except EOFError:
                print('Don\'t forget to enter your name!')
                print('')
            else:
                invalidName = False
        
        invalidName = True
            
        playerObj = Players(playerName)
        playerList.append(playerObj)
        
    print('')
    return playerList

# ----------------------------------
# Game Control System
# ----------------------------------

def main():
    
    print('')
    print('-'*50) 
    print('BlackJack in Python!')
    print('-'*50) 
    
    print('')
    print('Welcome to Blackjack in Python!')
    print('')
    print('Press Enter/Return to start playing!')
    
    notStarted = True
    
    while notStarted:
    
        try:
            beginGame = input()
            
            if beginGame:
                raise ValueError
        
        except ValueError:
            print('Press --> Enter/Return <--- on your keyboard to start!')
        
        else:
            notStarted = False
        
    if not beginGame:
        
        print('-'*50) 
        print(f'Player Setup')
        print('-'*50) 
        print('')
        
        playerList = []
        gameRunning = True
        round = 1
        
        playerSetup(playerList)
        
        for i in range(len(playerList)):
            print(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()}')
        
        print('')
        print('-'*50) 
        
        print('Begin Game?')
        
        while gameRunning:
            
            # print(f'Press Enter/Return To Start Round {round}!')
            # print('Any other key to end game and get final scores!')
            
            beginRound = input(f'Enter/Return to Start Round {round}!\nAny other key to quit and get final results! ')

            #beginRound = input()
            print('')
            
            if not beginRound:       

                print('-'*50) 
                print(f'Round {round} Started!')
                
                resultsOutput.write('\n')
                resultsOutput.write('-'*90)
                resultsOutput.write('\n')
                resultsOutput.write(f'Round {round} | Results\n')
                resultsOutput.write('-'*90)
                resultsOutput.write('\n')
                
                print('-'*50) 
                
                currentDeck = originalDeck.copy()
                #print('Now it is', len(currentDeck))
                print('')
                
                for i in range(0, len(playerList)):
                    
                    if playerList[i].get_points() >= 1:
                        invalidBet = True
                        currentBet = 0
                        print(f'{playerList[i].name}, it\'s your turn!')
                        print(f'You currently have {playerList[i].get_points()} tokens!')
                        
                        while invalidBet:
                            try: 
                                currentBet = int(input('How much would you like to bet?: '))
                                if currentBet <= 0:
                                    raise ValueError
                            except ValueError:
                                print('Make sure to enter an integer above 0 as your bet!')
                                print('')
                            else:
                                invalidBet = False
                                
                        playerList[i].update_bet(currentBet)
                        invalidBet = True
                        print('')
                        
                        if playerList[i].get_bet() > playerList[i].get_points():
                            playerList[i].update_bet(playerList[i].get_points())
                            print('')
                            print(f'Your bet has been set to {playerList[i].get_bet()} since you didn\'t have enough tokens!')
                        
                        playerList[i].update_points(playerList[i].get_points() - playerList[i].get_bet())
                
                        print(playerList[i])
                        print('')
                        
                    else:
                        print(f'{playerList[i].name}, you do not have any remaining tokens!')
                        print('')
                    
                    print('-'*50) 
                    print('')
                
                # print('-'*50) 
                # print(f'Round {round} Started!')
                # print('-'*50) 

                for i in range(0, len(playerList)):
                                        
                    if playerList[i].get_bet() == 0:
                        continue

                    else:
                        #print('')
                        print(f'{playerList[i].name}, your turn! ')
                        print('')
                        
                        currentRound = True

                        while currentRound == True:
                            
                            value = random.choice(currentDeck)
                            
                            type = Suit.get(value[1]) 

                            if value[2] == 'A' and (playerList[i].get_roundSum() + 11) > 21:
                                print('')
                                print('Favourable ACE! 1 has been added to your total to avoid going bust!')
                                print('')
                                playerList[i].update_cardSum(1)
                                
                            elif value[2] == 'A' and (playerList[i].get_roundSum() + 11) <= 21:
                                playerList[i].update_cardSum(CardValues[value[2]])
                            
                            else:
                                playerList[i].update_cardSum(CardValues[value[2]])
                                
                            #print(playerList[i].get_roundSum())
                            displayCard(value, type)
                            currentDeck.remove(value)
                            #print('Now it is', len(currentDeck))
                            
                            if playerList[i].get_roundSum() == 21:
                                print('')
                                print('BLACKJACK! You Hit 21! Let\'s see how the dealer does!')
                                break

                            elif playerList[i].get_roundSum() > 21:
                                print('')
                                print('Bust! You\'ve went over 21! Better luck next round!')
                                break
                                
                            print('-'*50)
                            
                            hitStand = ''
                            options = True
                            
                            while options ==  True:
                                
                                try:
                                    hitStand = input(f'Your total is {playerList[i].get_roundSum()}! Hit or Stand? (H/S) ')
                                    
                                    if hitStand not in 'HhSs' or (not hitStand):
                                        raise ValueError
                                    
                                except ValueError:
                                    print('Make sure to enter one of the options! (H/S) ')
                                    print('')
                                else:
                                    options = False
                            
                            if hitStand in ['S', 's']:
                                currentRound = False
                                        
                            print('-'*50) 
                        

                        if playerList[i].get_roundSum() < 21:
                            print('')    
                            print(f'{playerList[i].name}, your total is {playerList[i].get_roundSum()}!')
                        print('')
                        print('-'*50)
                        print('-'*50)
                        print('')    
                        
                print('Dealer\'s Turn!')
                print('')
                dealerSum = 0
                
                viewDealer = input('Press Enter to View the Dealer\'s Cards!')
                print('-'*50)
                print('')
                
                if not viewDealer:
                    while dealerSum <= 17:
                        value = random.choice(currentDeck)
                        #print(value)
                        type = Suit.get(value[1]) 
                        currentDeck.remove(value)
                        displayCard(value, type)
                        dealerSum += CardValues[value[2]]
                    
                    print('')
                    print('-'*50) 
                    print(f'The dealer is at {dealerSum}!')
                    print('-'*50) 
                    print('')
                    
                for i in range(len(playerList)):
                    
                    if 0 < playerList[i].get_roundSum() <= 21:
                        
                        if dealerSum == playerList[i].get_roundSum():
                            playerList[i].update_points(playerList[i].get_points() + \
                                playerList[i].get_bet())
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()} | Round Change: {0} Tokens (PUSH / NO-CHANGE)\n')
                            
                            print(f'{playerList[i].name}, you tied with the dealer! You get your tokens back.')
                            print('')
                            
                        elif (dealerSum < playerList[i].get_roundSum() < 21) or (dealerSum > 21 and playerList[i].get_roundSum() < 21):
                            playerList[i].update_points(playerList[i].get_points() + \
                                (2*playerList[i].get_bet()))
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()} | Round Change: {+playerList[i].get_bet()} Tokens (WIN)\n')
                            
                            print(f'{playerList[i].name}, nicely done! You won {playerList[i].get_bet()} tokens!')
                            print('')
                            
                        elif playerList[i].get_roundSum() == 21:
                            playerList[i].update_points(playerList[i].get_points() + \
                                (2*playerList[i].get_bet()) + int(1.5 * playerList[i].get_bet()))
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()} | Round Change: {+playerList[i].get_bet() + int(1.5 * playerList[i].get_bet())} Tokens (BLACKJACK WIN)\n')
                            
                            print(f'Amazing {playerList[i].name}! The blackjack won you a total of {playerList[i].get_bet() + int(1.5 * playerList[i].get_bet())} tokens!')
                            print('')
                            
                        else:     
                            print(f'Tough luck {playerList[i].name}. You lost your bet of {playerList[i].get_bet()}!')
                            print('')
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()} | Round Change: {-playerList[i].get_bet()} Tokens (LOSS)\n')
                    elif playerList[i].get_roundSum() > 21:
                        print(f'{playerList[i].name}, tough luck! Since you busted, you lost {playerList[i].get_bet()} tokens. Better luck next time!')
                        print('')
                        resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()} | Round Change: {-playerList[i].get_bet()} Tokens (LOSS/BUST)\n')

                    else:
                        resultsOutput.write(f'Player Name: {playerList[i].name} | (No Tokens)')
                        resultsOutput.write('\n')
                        
                print('-'*50)
                print(f'Round {round} | Results!')
                print('-'*50)
                
                zeroTokens = 0
                
                for i in range(len(playerList)):
                    playerList[i].reset_bet()
                    playerList[i].reset_roundSum()
                    print(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_points()}')
                    print('')
                    
                    if playerList[i].get_points() == 0:
                        zeroTokens += 1
                    
                print('-'*50)
                
                round += 1
                
                if zeroTokens == len(playerList):
                    print('')
                    print('All players have lost their tokens! That concludes the game!')
                    break
            else:
                break
  
    resultsOutput.write('\n')
    resultsOutput.write('-'*90)
    resultsOutput.write('\n')
    resultsOutput.write(f'Game | Final Results\n')
    resultsOutput.write('-'*90)
    resultsOutput.write('\n')
    
    for i in range(len(playerList)):
        resultsOutput.write(f'Player Name: {playerList[i].name} | Final Tokens: {playerList[i].get_points()} | Gain/Loss: {playerList[i].get_points() - 100}')
        resultsOutput.write('\n')
        
    resultsOutput.close()
    
    print('Thanks for playing! Make sure to check the results file for the game history!')
    print('')
    
if __name__ == '__main__':
    main()
    
    