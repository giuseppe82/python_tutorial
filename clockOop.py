import random

class Solitaire(object):
    def __init__(self):
        self.cards = list(range(13)) * 4
        self.winner = False
        self.discards = []

    def __shuffle(self):
        random.shuffle(self.cards)

    def __deal(self):
        self.__shuffle()
        clockFace = {}
        for v in range(13):
            start = v*4
            end = start + 4
            clockFace[v] = self.cards[start:end]
        self.clockFace = clockFace


    def play(self):
        self.winner = False
        self.discards = []
        self.__deal()
        currentCard = self.clockFace[0].pop() 
        while len(self.discards) < 52:
            self.discards.append(currentCard)
            if len(self.discards) == 52:
                self.winner = True
                break
            if len(self.clockFace[currentCard]) == 0:
                break
            else:
                currentCard = self.clockFace[currentCard].pop(0)

def main():
    game = Solitaire()

    for i in range(100):
        game.play()
        print(game.winner)


if __name__ == "__main__":
    main()