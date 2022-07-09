import random

#########################
#   returns list of tuples
def draw_hand():
    random.seed()
    hand = []
    for i in range(5):
        a = random.randrange(52)
        while deck[a] in hand:
            a = random.randrange(52)
        hand.append(deck[a])
    return hand

def isRoyalFlush(num_mem):
    if len(num_mem) != 5:
        return False
    sort = sorted(num_mem)
    num = 10
    if sort[0] != num:
        return False
    for x in sort[1:]:
        if x != num:
            return False
        num += 1
    return True

def isSequence(l):
    a = l[0]
    for x in range(1,len(l)):
        if x != a + 1:
            return False
        a = x
    return True

def isStraight(num_mem):
    if len(num_mem) != 5:
        return False
    sort = sorted(num_mem)
    num = sort[0]
    if num == 1:
        if isSequence(sort):
            return True
        else:
            for i in range(1,5):
                if sort[i] != num + 1:
                    break
                num += 1
            a = 9 + i
            while a != 14:
                if sort[i] != a:
                    return False
                a += 1
                i += 1
            return True
    else:
        if isSequence(sort):
            return True
        return False

def isFour(num_mem):
    for x in num_mem:
        if num_mem[x] == 4:
            return True
    return False

def isThree(num_mem):
    for x in num_mem:
        if num_mem[x] == 3:
            return True
    return False

def count_pair(num_mem):
    count = 0
    for x in num_mem:
        if num_mem[x] == 2:
            count += 1
    return count

def combo(hand):
    num_mem = {}
    suit_mem = {}
    flush = False
    for x in hand:
        if x[0] in suit_mem:
            suit_mem[x[0]] += 1
        else:
            suit_mem[x[0]] = 1

        if x[1] in num_mem:
            num_mem[x[1]] += 1
        else:
            num_mem[x[1]] = 1
    # check for Royal Flush and Straight Flush
    if len(suit_mem) == 1:
        if isRoyalFlush(num_mem):
            return "Royal Flush"
        elif isStraight(num_mem):
            return "Straight Flush"
        else:
            flush = True
    
    # check for Four of a Kind and Full House
    if len(num_mem) == 2:
        if isFour(num_mem):
            return "Four of a Kind"
        else:
            return "Full House"

    #check for Flush
    if flush:
        return "Flush"

    #check for Straight
    if isStraight(num_mem):
        return "Straight"

    #check for Three of a Kind
    if isThree(num_mem):
        return "Three of a Kind"
    
    num_pairs = count_pair(num_mem)
    if num_pairs == 2:
        return "Two Pair"
    elif num_pairs == 1:
        return "Pair"
    else:
        return "Single"
    
    
###########################
deck = []
suits = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
for x in suits:  
    for i in range(1,14):
        deck.append((x, i))
#hand = draw_hand()
#print(hand)
#print(combo(hand))
d = {"Royal Flush":0, "Straight Flush":0, "Four of a Kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a Kind":0, 
        "Two Pair":0, "Pair":0, "Single":0}
reference = {"Royal Flush": "0.000154%", "Straight Flush":"0.00139%", "Four of a Kind":"0.02401%", "Full House":"0.1441%", 
                "Flush":"0.1965%", "Straight":"0.3925%", "Three of a Kind":"2.1128%", "Two Pair":"4.7539%", "Pair":"42.2569%", 
                "Single":"50.1177%"}
Sample = 100000
for x in range(Sample):
    hand = draw_hand()
    d[combo(hand)] += 1
print("Sample: ", Sample)
for x in d:
    print(x, ": ",d[x]/Sample * 100, "% (", d[x], ") || expected: ", reference[x])
#hand = [("HEARTS", 4),("DIAMOND", 3),("CLUBS", 5),("HEARTS", 6),("SPADES", 2)]
#test = {12 : 1, 13:1, 1:1, 8:1, 11:1}
#l = sorted(test)
#print(type(l))
#print(isStraight(test))




