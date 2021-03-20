

class TttContaner:
    player_turn = ""
    posities = []

    def __init__(self):
        self.player_turn = ""
        for x in range(3):
            t = []
            for y in range(3):
                t.append(0)
            self.posities.append(t)



    #plaats
    #inhoud
    #wie
