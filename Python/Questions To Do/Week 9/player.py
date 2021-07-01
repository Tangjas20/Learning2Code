class Player:
    def __init__(self, name, xp, damage):
        self.name = name
        self.xp = xp
        self.damage = damage
    
    def add_xp(self, extra_xp):
        self.xp += extra_xp


    def calculate_score(self):
        return self.xp * self.damage
        


    def best_score(players):
        """From the given list of players, return the first
        player with the best score.
        """
        highest_score = 0
        highest_player = None

        for curr_player in players:
            print(curr_player.calculate_score())
            if curr_player.calculate_score() > highest_score:
                highest_score = curr_player.calculate_score
                highest_player = curr_player
        return highest_player

        pass


# Some sample code that uses the Player class.
p1 = Player('Ash Ketchum', 50, 1)
p2 = Player('Pikachu', 250, 2)
p3 = Player('Snorlax', 150, 3)

ls = [p1, p2, p3]

#assert Player.best_score(ls) == p2, "Clearly Pikachu does more work than Ash..."

# Add on another Player with the same score as Pikachu
ls.append(Player('Charizard', 100, 5))
assert Player.best_score(ls) == p2, "Charizard is cool and all, but Pikachu's \
cuteness wins out!"


best = Player.best_score(ls)
msg = '{} has the best score, with {} points!'.format(best.name, best.calculate_score())
print(msg) # Pikachu has the best score points!
