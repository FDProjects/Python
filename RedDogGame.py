# ---------------------------------------------------------------
# Author: Frank Dong
# Date: October 15, 2013
# Purpose:
# ---------------------------------------------------------------
import random
import math
class twoCard:
    def __init__(self, Card1, Card2):
        self.Card1 = Card1
        self.Card2 = Card2
        
#sub-getCard====================================================
# Author: Frank Dong
# Parameters:
# Date: October 15, 2013
# Purpose: To return a random integer from 2 to 13
def getCard():
    intCard = random.randint(2,13)
    return intCard

#sub-getHand=====================================================
# Author: Frank Dong
# Parameters:
# Date: October 15, 2013
# Purpose: Returns the 2 card object
def getHand():
    return twoCard (getCard (),getCard ())

#sub-printHand===================================================
# Author: Frank Dong
# Parameters:
# Date: October 15, 2013
# Purpose:

def printHand (Hand):
    return ("Your hand is:", Hand.Card1, "and", Hand.Card2)

#sub-handType===================================================
# Author: Frank Dong
# Parameters:
# Date: October 15, 2013
# Purpose:
def handType(Hand):
    if Hand.Card1 == Hand.Card2:
        strType = "Pair"
    elif Hand.Card1 == Hand.Card2 + 1 or Hand.Card1 == Hand.Card2 - 1:
        strType = "Consecutive"
    else:
        strType = "Non-Consecutive"
    return strType

#sub-spread====================================================
# Author: Frank Dong
# Parameters:
# Date: October 15, 2013
# Purpose:
def spread(playerHand):
    if handType(playerHand) == "Consecutive" or handType(playerHand) == "Pair":
        intspread = 0
    elif playerHand.Card1 > playerHand.Card2:
        spread = (playerHand.Card1  - playerHand.Card2) - 1
    else:
        spread = (playerHand.Card2 - playerHand.Card1) - 1
    return spread 
#sub-payout====================================================
def payout(Payout):
    if Payout == 1:
        intAmount = 5
    elif Payout == 2:
        intAmount = 40
    elif Payout == 3:
        intAmount = 2
    else:
        intAmount = 1
    return intAmount

#sub-between===================================================
def between (Hand, Card):
    return Hand.Card1 < Card and Card < Hand.Card2 or Hand.Card2 < Card and Card < Hand.Card1

#sub-getBet=======================================================================
#Purpose: Return vaild positive integers
#Parameters: Low, High, Prompt
#Return: intResponse
def getBet(low,high,prompt=""):
    
    intResponse = low -1
    strPrompt = "Please enter your "+prompt+" bet between "+str(low)+" and "+str(high)+": "
    while intResponse < low or intResponse > high:
        strResponse = raw_input (strPrompt)
        if strResponse.isdigit():
            intResponse = int(strResponse)
    
    return intResponse

#Main==========================================================
strStart = "Yes"
intPurse = 100
while strStart == "Yes" or strStart == "yes" or strStart == "Y" and intPurse > 0:
    print ("Amount of money you have in Purse:", intPurse)
    intBet = input("How much do you wish to bet?: ")
    while not (0 < intBet <= intPurse):
        intBet = input("How much do you wish to bet?: ")
    objHand = getHand()
    print (printHand(objHand))
    strtype = handType(objHand)
    if strtype == "Pair":
        intthirdCard = getCard ()
        print ("Third card", intthirdCard)
        if intthirdCard == objHand.Card1 :
            print ("You Win!")
            intPurse += intBet * 11
            print ("Amount left in Purse:", intPurse)
        else:
            print ("The result was a tie.")
            print ("Amount left in Purse:", intPurse)
    elif strtype == "Consecutive":
        print ("Consecutive")
        print ("The result was a tie.")
        print ("Amount left in Purse:", intPurse)

    else:
        intBet2 = getBet(0,intPurse,"second")
        while intBet2 <= 0 and intBet2 < intPurse - intBet:
            intBet2 = getBet(0,intPurse,"second")
        intBet += intBet2
        intthirdCard = getCard()
        print ("Your third card is:", intthirdCard)
        if  between(objHand,intthirdCard):
            print ("You Win!")
            intPurse += intBet * payout(spread(objHand))
            print ("Amount left in Purse:", intPurse)
        else:
            print ("You Lose!")
            intPurse -= intBet
            print ("Amount left in Purse:", intPurse)
    print (" ")
    strStart = input("Do you want to play again?(Yes/No): ")
    while not (strStart == "Yes" or strStart == "yes" or strStart == "Y" or strStart == "no" or strStart == "N" or strStart == "No"):
        strStart = input("Do you want to play again?(Yes/No): ")
    if intPurse <= 0:
        intPurse = 100
