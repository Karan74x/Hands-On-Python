class Player:

    # Class Variable
    total_players = 0

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):
        self.name = name
        self.team = team
        self.role = role
        self.credits = credits
        self.points_scored = points_scored

        # Increment total players
        Player.total_players += 1

    # Method
    def get_fantasy_points(self):
        return self.points_scored

    # String Method
    def display(self):
        return f"{self.name}, ({self.team}) , {self.role} , {self.credits} credits"


# Child Class
class Captain(Player):

    # Constructor
    def __init__(self, name, team, role, credits, points_scored):
        super().__init__(name, team, role, credits, points_scored)

    # Method Overriding
    def get_fantasy_points(self):
        return self.points_scored * 2


# Driver Code

p1 = Player("Virat Kohli", "RCB", "Batsman", 9.5, 80)
p2 = Player("Jasprit Bumrah", "MI", "Bowler", 8.5, 60)
c1 = Captain("Rohit Sharma", "MI", "Batsman", 9.5, 70)

print(p1.display())
print("Fantasy Points :", p1.get_fantasy_points())

print(p2.display())
print("Fantasy Points :", p2.get_fantasy_points())


print(c1.display())
print("Fantasy Points :", c1.get_fantasy_points())

print("Total Players :", Player.total_players)
