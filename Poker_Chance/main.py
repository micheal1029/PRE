import random
from operator import *

def main():
    def isSequence(l):
        first = l[0]
        for i in range(1,5):
            if l[i] != first + 1:
                return False
            first = l[i]
        return True

    class Card(object):
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value

        def __repr__(self):
            suit_dict = {0:"spades", 1:"hearts", 2:"diamonds", 3:"clubs"}
            value_dict = {0:"ace", 1:"king", 2:"queen", 3:"jack", 4:"10", 5:"9", 6:"8", 7:"7", 8:"6", 9:"5", 10:"4", 11:"3", 12:"2"}
            suit_name = suit_dict[self.suit]
            value_name = value_dict[self.value]
            return value_name + " of " + suit_name
            
    class Deck(list): 
        def __init__(self):
            super().__init__()
            suits = list(range(4))
            values = list(range(13))
            [[self.append(Card(i,j)) for j in values] for i in suits]

        def shuffle(self):
            random.shuffle(self)

        def deal(self):
            hand = self[:5]
            suit_count = {}
            value_count = {}
            for x in hand:
                if x.value in value_count:
                    value_count[x.value] += 1
                else:
                    value_count[x.value] = 1
                
                if x.suit in suit_count:
                    suit_count[x.suit] += 1
                else: 
                    suit_count[x.suit] = 1
            print(value_count)
            print(suit_count)
            l = list(value_count.keys())
            if len(l) == 5:
                sequence = isSequence(l)
            else:
                sequence = False

            if sequence:
                if l[0] == 0 and len(suit_count) == 1:
                    return "royal flush"
                elif len(suit_count) == 1:
                    return "straight flush"
                else:
                    return "straight"
            else:
                if len(suit_count) == 1:
                    return "flush"
                  
            if 4 in value_count.values():
                return "four of a kind"
            elif 3 in value_count.values():
                if 2 in value_count.values():
                    return "full house"
                else:
                    return "three of a kind"
            elif 2 in value_count.values():
                if countOf(value_count.values(), 2) == 2:
                    return "two pairs"
                else:
                    return "pair"
            else: 
                return "high card"

    d = Deck()
    d.shuffle()
    print(d[:5])
    print(d.deal())
    
    







if __name__ == "__main__":
    main()
#look more into this block





#########################
#   returns list of tuples
# def draw_hand():
#     random.seed()
#     hand = []
#     for i in range(5):
#         a = random.randrange(52)
#         while deck[a] in hand:
#             a = random.randrange(52)
#         hand.append(deck[a])
#     return hand

# def isRoyalFlush(num_mem):
#     if len(num_mem) != 5:
#         return False
#     sort = sorted(num_mem)
#     num = 10
#     if sort[0] != num:
#         return False
#     for x in sort[1:]:
#         if x != num:
#             return False
#         num += 1
#     return True

# def isSequence(l):
#     a = l[0]
#     for x in range(1,len(l)):
#         if x != a + 1:
#             return False
#         a = x
#     return True

# def isStraight(num_mem):
#     if len(num_mem) != 5:
#         return False
#     sort = sorted(num_mem)
#     num = sort[0]
#     if num == 1:
#         if isSequence(sort):
#             return True
#         else:
#             for i in range(1,5):
#                 if sort[i] != num + 1:
#                     break
#                 num += 1
#             a = 9 + i
#             while a != 14:
#                 if sort[i] != a:
#                     return False
#                 a += 1
#                 i += 1
#             return True
#     else:
#         if isSequence(sort):
#             return True
#         return False

# def isFour(num_mem):
#     for x in num_mem:
#         if num_mem[x] == 4:
#             return True
#     return False

# def isThree(num_mem):
#     for x in num_mem:
#         if num_mem[x] == 3:
#             return True
#     return False

# def count_pair(num_mem):
#     count = 0
#     for x in num_mem:
#         if num_mem[x] == 2:
#             count += 1
#     return count

# def combo(hand):
#     num_mem = {}
#     suit_mem = {}
#     flush = False
#     for x in hand:
#         if x[0] in suit_mem:
#             suit_mem[x[0]] += 1
#         else:
#             suit_mem[x[0]] = 1

#         if x[1] in num_mem:
#             num_mem[x[1]] += 1
#         else:
#             num_mem[x[1]] = 1
#     # check for Royal Flush and Straight Flush
#     if len(suit_mem) == 1:
#         if isRoyalFlush(num_mem):
#             return "Royal Flush"
#         elif isStraight(num_mem):
#             return "Straight Flush"
#         else:
#             flush = True
    
#     # check for Four of a Kind and Full House
#     if len(num_mem) == 2:
#         if isFour(num_mem):
#             return "Four of a Kind"
#         else:
#             return "Full House"

#     #check for Flush
#     if flush:
#         return "Flush"

#     #check for Straight
#     if isStraight(num_mem):
#         return "Straight"

#     #check for Three of a Kind
#     if isThree(num_mem):
#         return "Three of a Kind"
    
#     num_pairs = count_pair(num_mem)
#     if num_pairs == 2:
#         return "Two Pair"
#     elif num_pairs == 1:
#         return "Pair"
#     else:
#         return "Single"
    
    
# ###########################
# deck = []
# suits = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
# for x in suits:  
#     for i in range(1,14):
#         deck.append((x, i))
# #hand = draw_hand()
# #print(hand)
# #print(combo(hand))
# d = {"Royal Flush":0, "Straight Flush":0, "Four of a Kind":0, "Full House":0, "Flush":0, "Straight":0, "Three of a Kind":0, 
#         "Two Pair":0, "Pair":0, "Single":0}
# reference = {"Royal Flush": "0.000154%", "Straight Flush":"0.00139%", "Four of a Kind":"0.02401%", "Full House":"0.1441%", 
#                 "Flush":"0.1965%", "Straight":"0.3925%", "Three of a Kind":"2.1128%", "Two Pair":"4.7539%", "Pair":"42.2569%", 
#                 "Single":"50.1177%"}
# Sample = 100000
# for x in range(Sample):
#     hand = draw_hand()
#     d[combo(hand)] += 1
# print("Sample: ", Sample)
# for x in d:
#     print(x, ": ",d[x]/Sample * 100, "% (", d[x], ") || expected: ", reference[x])
# #hand = [("HEARTS", 4),("DIAMOND", 3),("CLUBS", 5),("HEARTS", 6),("SPADES", 2)]
# #test = {12 : 1, 13:1, 1:1, 8:1, 11:1}
# #l = sorted(test)
# #print(type(l))
# #print(isStraight(test))




