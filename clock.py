import random


def dealCards(cards):
    clockFace = {}
    for v in range(13):
        start = v*4
        end = start + 4
        clockFace[v] = cards[start:end]
    return clockFace


def setupSolitaire():
    cards = list(range(13)) * 4
    random.shuffle(cards)
    clockFace = dealCards(cards)
    return clockFace


def playSolitaire(clockFace):
    winner = False
    discards = []
    currentCard = clockFace[0].pop() 
    for i in range(52):
        print(clockFace)
        discards.append(currentCard)
        if len(discards) == 52:
            winner = True
            break
        if len(clockFace[currentCard]) == 0:
            break
        else:
            currentCard = clockFace[currentCard].pop(0)
    return winner


def main():
    counter = 0
    wins = 0
    for i in range(1000):
        counter += 1
        clockFace = setupSolitaire()
        outcome = playSolitaire(clockFace)
        print(outcome)
        if outcome == True:
            wins += 1
        pWin = wins / counter
        #print(pWin)

    print(counter, wins, pWin)


if __name__ == "__main__":
    main()