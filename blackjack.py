'''
Project Name : BlackJack
Developed By : Dev Patel
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
        # ^ Since it reads in the form of 'COLOUR | SUIT | VALUE' 
            # ^ It splits it into a list with 3 values. [COLOUR, SUIT, VALUE]
            
        originalDeck.append(card)
        # ^ Then add that single-card into a list that will act as the deck.
# ------------------------------------
# Round Statistics (File Output)
# ------------------------------------

resultsOutput = open("results.txt", "a+")

resultsOutput.write('BlackJack Game History | Developed by Dev Patel\n')

# ----------------------------------
# Player Data Class
# ----------------------------------

class Players():
    
    def __init__(self, name, tokens = 100, currentBet=0, roundSum = 0):
        # ^ Initializes these instances to the object (player in this case)
            # ^ tokens, currentBet, roundSum set to their default values
                
        self.name = name 
        self.tokens = tokens
        self.currentBet = currentBet
        self.roundSum = roundSum
        
        # ^ Sets all the attributes as the instance of the class.
            # ^ So when calling player.name --> Looks at the self.name attribute

    def __str__(self):
        return(f'Player Name: {self.name} | Tokens: {self.tokens} | Bet: {self.currentBet}')
        # ^ When printing the player, calls the __str__ method to print the above
        
    def get_tokens(self):
        return self.tokens
        # ^ Returns the amount of tokens/tokens the player has.
        
    def update_tokens(self, tokens):
        self.tokens = tokens
        # ^ When called, updates tokens to whatever the point variable is from the argument.
        
    def get_bet(self):
        return self.currentBet
        # ^ Returns the bet from the round the player entered.
    
    def update_bet(self, currentBet):
        self.currentBet = currentBet
        # ^ Same as update tokens. Updates it to argument entered.
        
    def reset_bet(self, currentBet=0):
        self.currentBet = currentBet
        # ^ Sets current bet back to 0 (for new round)
    
    def update_cardSum(self, roundSum):
        self.roundSum += roundSum
        # ^ Adds the argument to the card total for the round.

    def reset_roundSum(self, roundSum=0):
        self.roundSum = roundSum
        # ^ Resets round total back to 0 (for new round)
    
    def get_roundSum(self):
        return self.roundSum
        # ^ Returns the card total the player had.

# --------------------------------
# Card Display Function
# --------------------------------

def displayCard(value, type):
        
        space = ' '
        
        if value[2] == '10':
            space = ''
        
        # ^ Since 10 is the only value with 2 characters, reduce by 1 whitespace.
        
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
            #^ Accesses each "row" in the template and joins each value in the list with a whitespace. 

            

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

#^ Used a dictionary for this as it'll help to give values to royals.
    # ^ Also helps to map string value to it's integer value.

# ----------------------------------
# Card Symbols to Name for Display
# ----------------------------------

SuitTuple = [('SPADE', '♠'), ('DIAMOND', '♦'), ('CLUB', '♣'), ('HEART', '♥')]
#^ For card display purposes.

# ----------------------------------
# Create Player Instance
# ----------------------------------

def playerSetup(playerList):
    
    invalidInput = True
    invalidName = True
    #^ Used invalid variables for temporary error checking in inputs.
    
    while invalidInput:
        
        try:
            numberofPlayers = int(input('Enter number of players playing: '))
            print('')
            
            if numberofPlayers <= 0:
                raise ValueError
                # ^ Raising ValueError even though negative values don't. Just for error purpose.
                
        except ValueError:
            print('Make sure to enter an integer above 0! You can\'t play a game with no one!')
            print('')
        
        else:
            invalidInput = False
            #^ If no error, sets it to false so while loop does not continue.
            
    for i in range(1, numberofPlayers+1):
        #^ Starting at 1 so it beings as player 1 and not 0.
        
        while invalidName:
            
            try:
                playerName = input(f'Enter Player {i} Name: ')
                    
                if not playerName:
                    raise EOFError
                    #^ When nothing is inputted. Accepting numbers as names!
                
            except EOFError:
                print('Don\'t forget to enter your name!')
                print('')
            else:
                invalidName = False
        
        invalidName = True
            
        playerObj = Players(playerName)
        #^ Creates object (gives in name of player and the class assigns necessary attributes)
        
        playerList.append(playerObj)
        #^ Adds the object(player) to the list of players for easy access.
        
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
                #^ If something is inputted then raise error. Looking for empty input!
                raise ValueError
        
        except ValueError:
            print('Press --> Enter/Return <--- on your keyboard to start!')
        
        else:
            notStarted = False
        
    if not beginGame:
        #^ Don't need this portion but keeping for easy code review.
            #^ beginGame will always be false since coming out of error check above.
        
        print('-'*50) 
        print(f'Player Setup')
        print('-'*50) 
        print('')
        
        playerList = []
        gameRunning = True
        round = 1
        
        playerSetup(playerList)
        #^ Sends the empty list to add players in the playerSetup() function.
        
        for i in range(len(playerList)):
            print(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()}')
        
        print('')
        print('-'*50) 
        
        print('Begin Game?')
        
        while gameRunning:
            
            beginRound = input(f'Enter/Return to Start Round {round}!\nAny other key to quit and get final results! ')
            print('')
            
            if not beginRound:       
                #^ Looks for empty input. (Enter/Return)
                
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
                #^ Create copy of originalDeck to use throughout the round.
                    #^ This way, no need to open the file everytime and create a deck
                    
                print('')
                
                for i in range(0, len(playerList)):
                    
                    if playerList[i].get_tokens() >= 1:
                        #^ Only accepts bet from players with more than 1 point. (Minimum)
                        invalidBet = True
                        currentBet = 0
                        print(f'{playerList[i].name}, it\'s your turn!')
                        print(f'You currently have {playerList[i].get_tokens()} tokens!')
                        
                        while invalidBet:
                            try: 
                                currentBet = int(input('How much would you like to bet?: '))
                                if currentBet <= 0:
                                    raise ValueError
                                    #^ Once again, hard-coding error of below 0.
                                        #^ If input is empty, it will also create an error.
                                    
                            except ValueError:
                                print('Make sure to enter an integer above 0 as your bet!')
                                print('')
                            else:
                                invalidBet = False
                                
                        playerList[i].update_bet(currentBet)
                        #^ Updates the player's bet depending on input.
                        
                        invalidBet = True
                        print('')
                        
                        if playerList[i].get_bet() > playerList[i].get_tokens():
                            playerList[i].update_bet(playerList[i].get_tokens())
                            #^ If the player bets an amount above the number of tokens they have, set it to max tokens.
                            
                            print('')
                            print(f'Your bet has been set to {playerList[i].get_bet()} since you didn\'t have enough tokens!')
                        
                        playerList[i].update_tokens(playerList[i].get_tokens() - playerList[i].get_bet())
                        #^ Update the amount of tokens the player has. (subtact total tokens by their bet for remianing.)
                        
                        print(playerList[i])
                        print('')
                        
                    else:
                        print(f'{playerList[i].name}, you do not have any remaining tokens!')
                        #^ If player has 0 tokens available.
                        print('')
                    
                    print('-'*50) 
                    print('')
                
                for i in range(0, len(playerList)):
                                        
                    if playerList[i].get_bet() == 0:
                        #^ In other words the bet will only be 0 if and only if player has zero tokens.
                        continue
                        #^ Skips to next iteration of loop. (next player)

                    else:
                
                        print(f'{playerList[i].name}, your turn! ')
                        print('')
                        
                        currentRound = True

                        while currentRound == True:
                            
                            value = random.choice(currentDeck)
                            #^ Randomly picks a card from the list.
                        
                            for suitIcon in SuitTuple:
                                if value[1] == suitIcon[0]:
                                    type = suitIcon[1]
                            #^ Get's the suit icon from the tupled list by finding the matching suit name from value.

                            if value[2] == 'A' and (playerList[i].get_roundSum() + 11) > 21:
                                #^ Since ACES can be 1 or 11, add 1 if player will bust with an 11 added to their total.
                                
                                print('')
                                print('Favourable ACE! 1 has been added to your total to avoid going bust!')
                                print('')
                                playerList[i].update_cardSum(1)
                                
                            elif value[2] == 'A' and (playerList[i].get_roundSum() + 11) <= 21:
                                playerList[i].update_cardSum(CardValues[value[2]])
                                #^ Otherwise just add 11 if player won't bust.
                            
                            else:
                                playerList[i].update_cardSum(CardValues[value[2]])
                                #^ If value is not an Ace, just add whatever the value the key is assigned to.
                                
                            displayCard(value, type)
                            currentDeck.remove(value)
                            #^ After displaying the card, remove the card (Value) from the deck.
                            
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
                                    
                                    if hitStand not in 'HhSs' or (not hitStand) or len(hitStand) > 1:
                                        #^ Accepting uppercase and lowercase values. If input is not in this, raise error.
                                            #^ Also making sure input is not above 2 characters such as 'HS' or 'hS'
                                
                                        raise ValueError
                                
                                except ValueError:
                                    print('Make sure to enter one of the options! (H/S) ')
                                    print('')
                                else:
                                    options = False
                            
                            if hitStand in ['S', 's']:
                                currentRound = False
                                #^ When player stands (S), no more bets should be asked and the next player's turn begins.
                                        
                            print('-'*50) 
                        

                        if playerList[i].get_roundSum() < 21:
                            print('')    
                            print(f'{playerList[i].name}, your total is {playerList[i].get_roundSum()}!')
                            #^ Displays player's final card total for the round.
                            
                        print('')
                        print('-'*50)
                        print('-'*50)
                        print('')    
                        
                print('Dealer\'s Turn!')
                print('')
                dealerSum = 0
                
                viewDealer = input('Press Any Key to View the Dealer\'s Cards!')
                print('-'*50)
                print('')
                
                if not viewDealer or viewDealer:
                    while dealerSum <= 17:
                        value = random.choice(currentDeck)
                        #print(value)
                        
                        for suitIcon in SuitTuple:
                                if value[1] == suitIcon[0]:
                                    type = suitIcon[1]
                                    
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
                        #^ If player did not bust and doesn't have 0 tokens...
                        
                        if dealerSum == playerList[i].get_roundSum():
                            #^ Checks if totals are equal. In which case "PUSH" (Get's tokens back)
                            playerList[i].update_tokens(playerList[i].get_tokens() + \
                                playerList[i].get_bet())
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()} | Round Change: {0} Tokens (PUSH / NO-CHANGE)\n')
                            #^ Writes the round result for the player in game history file.
                            
                            print(f'{playerList[i].name}, you tied with the dealer! You get your tokens back.')
                            print('')
                            
                        elif (dealerSum < playerList[i].get_roundSum() < 21) or (dealerSum > 21 and playerList[i].get_roundSum() < 21):
                            #^ If the player's total is above the dealer but not bust..
                                #^ OR if dealer busted but player didnt..
                                    #^ Then add 2 times their bet twice. (Get their original tokens back + bet)
                                    
                            playerList[i].update_tokens(playerList[i].get_tokens() + \
                                (2*playerList[i].get_bet()))
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()} | Round Change: {+playerList[i].get_bet()} Tokens (WIN)\n')
                            #^ Writes the round result for the player in game history file.

                            print(f'{playerList[i].name}, nicely done! You won {playerList[i].get_bet()} tokens!')
                            print('')
                            
                        elif playerList[i].get_roundSum() == 21:
                            playerList[i].update_tokens(playerList[i].get_tokens() + \
                                (2*playerList[i].get_bet()) + int(1.5 * playerList[i].get_bet()))
                                #^ If blackjack (21), give a multiplier of 1.5 but int type to avoid float numbers.
                            
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()} | Round Change: {+playerList[i].get_bet() + int(1.5 * playerList[i].get_bet())} Tokens (BLACKJACK WIN)\n')
                            
                            print(f'Amazing {playerList[i].name}! The blackjack won you a total of {playerList[i].get_bet() + int(1.5 * playerList[i].get_bet())} tokens!')
                            print('')
                            
                        else:     
                            print(f'Tough luck {playerList[i].name}. You lost your bet of {playerList[i].get_bet()}!')
                            print('')
                            resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()} | Round Change: {-playerList[i].get_bet()} Tokens (LOSS)\n')
                            #^ Write a LOSS in game history if none of the above conditions are true.
                            
                    elif playerList[i].get_roundSum() > 21:
                        print(f'{playerList[i].name}, tough luck! Since you busted, you lost {playerList[i].get_bet()} tokens. Better luck next time!')
                        print('')
                        resultsOutput.write(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()} | Round Change: {-playerList[i].get_bet()} Tokens (LOSS/BUST)\n')
                        #^ Finally, if player busts (over 21), write in game history as bust.
                        
                    else:
                        resultsOutput.write(f'Player Name: {playerList[i].name} | (No Tokens)')
                        resultsOutput.write('\n')
                        #^ For players that did not have tokens to begin with (already lost them)
                            #^ Write as no tokens in game history.
                        
                print('-'*50)
                print(f'Round {round} | Results!')
                print('-'*50)
                
                zeroTokens = 0
                
                for i in range(len(playerList)):
                    playerList[i].reset_bet()
                    playerList[i].reset_roundSum()
                    print(f'Player Name: {playerList[i].name} | Tokens: {playerList[i].get_tokens()}')
                    print('')
                    
                    #^ Reset bet and card total for the player (to prep for next round)
                    
                    if playerList[i].get_tokens() == 0:
                        zeroTokens += 1
                    #^ If player has zero tokens add one to the total.
                    
                print('-'*50)
                
                round += 1
                
                if zeroTokens == len(playerList):
                    print('')
                    print('All players have lost their tokens! That concludes the game!')
                    #^ If the number of players with zero tokens equals the total amount of players
                    break
                    #^ Break out of game (no more bets can be made therefore game is over.)
                else:
                    zeroTokens = 0
                    #^ Sets it back to zero to let other players continue playing.
            else:
                break
  
    resultsOutput.write('\n')
    resultsOutput.write('-'*90)
    resultsOutput.write('\n')
    resultsOutput.write(f'Game | Final Results\n')
    resultsOutput.write('-'*90)
    resultsOutput.write('\n')
    
    for i in range(len(playerList)):
        resultsOutput.write(f'Player Name: {playerList[i].name} | Final Tokens: {playerList[i].get_tokens()} | Gain/Loss: {playerList[i].get_tokens() - 100}')
        resultsOutput.write('\n')
        #^ Write final scores if all players have zero tokens or purposely ended the game.
        
    resultsOutput.close()
    
    print('-'*50)
    print('Game Ended!')
    print('-'*50)
    print('')
    print('Thanks for playing! Make sure to check the results file for the game history!')
    print('')
    
if __name__ == '__main__':
    main()
    #^ Starts the script. 
    
