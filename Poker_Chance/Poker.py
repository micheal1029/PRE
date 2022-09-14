import Deck
from datetime import datetime

def trial(draws):
    results = {}
    for x in range(draws):
        d = Deck.Deck()
        d.shuffle()
        hand = d.deal()
        if hand in results:
            results[hand] += 1
        else:
            results[hand] = 1

    ratio = {}
    for x in results:
        ratio[x] = results[x]/draws
    return ratio

# Averages each trials and returns a dictionary with strings as keys and float as values
def run(trials, draws):
    total = {'royal flush': 0, 'straight flush': 0, 'four of a kind': 0, 'full house': 0, 'flush': 0, 
        'straight': 0, 'three of a kind': 0, 'two pairs': 0, 'pair': 0, 'high card': 0}

    n = 1
    for x in range(trials):
        print("Trial: " + str(n))
        t = trial(draws)
        for x in t:
            total[x] += t[x]
        n += 1

    average = {} #decimals
    for x in total:
        average[x] = total[x]/trials

    diff ={}
    reference = {'royal flush': 0.00000154, 'straight flush': .0000139, 'four of a kind': .0002401, 'full house': .001441, 'flush': .003925, 
        'straight': .003925, 'three of a kind': .021128, 'two pairs': .047539, 'pair': .422569, 'high card': .501177}
    for x in reference:
        diff[x] = average[x] - reference[x]

    print("Total Average Percentage:")
    print_percentage(average)
    print("Percentage Difference: ")
    data = print_percentage(diff)

    return data
                    
def print_percentage(ratio):
    l = ['royal flush', 'straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pairs', 'pair', 'high card']
    s = ""
    for x in l:
        print(x.upper() + ": " + f"{ratio[x]:.6%}")
        s += (x.upper() + ": " + f"{ratio[x]:.6%}\n")
    print()
    return s



def main():
    trials = 5
    draws = 1000000
    start = datetime.now()
    print(run(trials, draws))

    # for x in range(10):
    #     init_time = datetime.now().strftime("%m/%d/%y %H:%M:%S") #Month/Date/Year cuz I'm American
    #     data = run(trials, draws)
    #     with open('3million.txt', 'a') as f:
    #         f.write(init_time + "\n")
    #         f.write(data)
    #         f.write("\n")
    #         f.close()
    print("Total Runtime: " + str(datetime.now()-start))

    
    
if __name__ == "__main__":
    main()
