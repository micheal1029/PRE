import Deck
from datetime import datetime

def trial(draws):
    start = datetime.now()
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
    print("Trial Runtime: " + str(datetime.now()-start))
    print_percentage(ratio)
    return ratio

# Averages each trials and returns a dictionary with strings as keys and float as values
def run(trials, draws):
    init_time = datetime.now().strftime("%m/%d/%y %H:%M:%S") #Month/Date/Year cuz I'm American
    start=datetime.now()
    total = {}
    n = 1
    for x in range(trials):
        print("Trial: " + str(n))
        t = trial(draws)
        if(len(total) == 0):
            total = t
        else:
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

    print("Total Runtime: " + str(datetime.now()-start))
    print("Total Average Percentage:")
    print_percentage(average)
    print("Percentage Difference: ")
    data = print_percentage(diff)

    with open('3million.txt', 'a') as f:
        f.write(init_time + "\n")
        f.write(data)
        f.write("\n")

    return average
                    
def print_percentage(ratio):
    l = ['royal flush', 'straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pairs', 'pair', 'high card']
    s = ""
    for x in l:
        if (x not in ratio):
            print(x.upper() + ": N/A")
            s += (x.upper() + ": N/A\n")
        else:
            print(x.upper() + ": " + f"{ratio[x]:.6%}")
            s += (x.upper() + ": " + f"{ratio[x]:.6%}\n")
    print()
    return s



def main():
    trials = 3
    draws = 1000000
    run(trials, draws)

    
    
if __name__ == "__main__":
    main()
