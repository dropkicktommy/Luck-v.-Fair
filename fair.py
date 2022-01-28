import numpy as np
import matplotlib.pyplot as plt

player_count = 100
initial_cash = 100
total_battles = 500000

# randomly assign wallet balances to all fighters
wallets = np.random.randint(25, 174, size=player_count)
alive = np.arange(0, player_count)

# run the simulation
for battle in range(total_battles):
    # choose 2 random fighters from the list of survivors
    fighters = np.random.choice(alive, 2)
    # load each fighters balance from the wallet log
    fighter_1_balance = wallets[fighters[0]]
    fighter_2_balance = wallets[fighters[1]]
    if fighter_1_balance == fighter_2_balance:
        # use a straight coin toss if both fighters are equal
        toss = np.random.choice([0, 1], 1)
    else:
        # use a weighted coin toss in the case of a weaker fighter
        if fighter_1_balance > fighter_2_balance:
            fighters[0], fighters[1] = fighters[1], fighters[0]
        fighter_1_balance = wallets[fighters[0]]
        fighter_2_balance = wallets[fighters[1]]
        handicap = fighter_1_balance * 1 / (fighter_1_balance + fighter_2_balance)
        toss = np.random.choice([0, 1], 1, p=[1 - handicap, handicap])
    # decide the winner of the coin toss
    if toss == 0:
        winner, loser = fighters[0], fighters[1]
    else:
        winner, loser = fighters[1], fighters[0]
    # fighters exchange money
    wallets[winner] += 1
    wallets[loser] -= 1
    # if a fighter's balances reaches zero, the fighter is dead
    if wallets[loser] <= 0:
        alive = np.delete(alive, np.where(alive == loser))
        print("Fighter " + str(loser) + " has died.")

plt.hist(wallets)
plt.show()
print(str(len(alive)) + " fighter(s) still in the game")
