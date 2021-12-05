import random

def helpRule ():    
    basicRules = '''Basic Rules of the Paired Card\n1 Distrubute 5 cards for each\n2 Objective to make all the cards double \n3 first player need to take one car and check wheather it is paired or not,\n4 one card need to throw\n5 Continue the game untill you get all cards paired, then you will win\n'''
    print(basicRules)
helpRule()

#name of the player

user1 = input("Player1 Please give your name\n")
user2 = input("Player1 Please give your name\n")
player = user1

#distrbute the Card to the Player
def distributeCard ():
    deck = []
    faceCard = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']
    for i in range(5):
        randNo = random.randint(0,12)
        deck.append(faceCard[randNo])
    return deck 
#Convert list of card into dict
def conListToDic (var):
    deckDic = {}
    for i in var:
        if i in deckDic:
            deckDic[i] += 1
        else:
            deckDic[i] = 1
    return deckDic

#take one card
def getCard():
    getCardList =[]
    faceCard = ['2','3','4','5','6','7','8','9','10','A','J','Q','K']    
    randUser = random.randint(0,12)      
    #getCardList.append(faceCard[randUser])
    getNewVar = faceCard[randUser]
    #var.append(faceCard[randUser])
    return getNewVar
#the pop out function
def throwOddCaard():
    chooseCard = input("please select the card to throw from Your Card \n")
    chooseCard1 = chooseCard.upper()

    return chooseCard1

deck1 = distributeCard()
deck2 = distributeCard()


while(True):   
    if player == user1:
        print(user1," its your turn")
        helpGuide = input("Do you want Help Yes or No\n") #help guide
        askHelp = helpGuide.lower()

        if askHelp == 'yes':
            helpRule()
                
        print("to check 1",deck1)
        user1Move1 = deck1.append(getCard())
        user1Move1_Dic = conListToDic(deck1)
        print("dic for user 1 = ",user1Move1_Dic)       
        #testResult = all(x==2 for x in user1Move1_Dic.values())
        res = True   
        # extracting value to compare 
        test_val = 2
  
        for ele in user1Move1_Dic: 
            if user1Move1_Dic[ele] != test_val: 
                res = False 
                break
        if res == True :
            print(user1,"you win the Game")
            break
        print("please choose the card from, ",deck1)
        valueToIndex = deck1.index(throwOddCaard())
        print("to find index=",valueToIndex)
        deck1.pop(valueToIndex)
        print("after thrown user 1 card, ",deck1)   
        player = user2
        print("player =", player)
        
    
    if player == user2: 
        print(user2," its your turn") 
        helpGuide2 = input("Do you want Help Yes or No\n") #help guide
        askHelp2 = helpGuide2.lower()

        if askHelp2 == 'yes':
            helpRule()
                     
        user2Move1 = deck2.append(getCard())
        user2Move1_Dic = conListToDic(deck2)
        print("dic for user 2=",user2Move1_Dic)
        
        res2 = True   
        # extracting value to compare 
        test_val2 = 2
  
        for ele in user2Move1_Dic: 
            if user2Move1_Dic[ele] != test_val2: 
                res2 = False 
                break
        if res2 == True :
            print(user2,"you win the Game")
            break
        valueToIndex2 = deck2.index(throwOddCaard())
        deck2.pop(valueToIndex2)
        print("after throw user 2=",user2Move1_Dic)   
        player = user1




    
 
