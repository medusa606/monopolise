from threading import activeCount

from fontTools.mtiLib import build

from utils import dice, player, constants, board, chance, state
import random

# for debugging
from icecream import ic
# random.seed = 0

def factorial(input, n):
    for n in range(n-1):
        input = input * 2
    return input

def player_in_jail(active_player, ROLL_DOUBLE):

    if ROLL_DOUBLE:
        if VERBOSE: print(f"{active_player.name} is in Jail but rolled a double and is released")
        active_player.out_jail()
        return 0
    elif active_player.remaining_sentence == 1:
        if VERBOSE: print(f"This is {active_player.name}'s last day in jail, you are free")
        active_player.out_jail()

    elif active_player.remaining_sentence > 1 and active_player.balance > constants.jail_release_fee:
        if VERBOSE: print(f"{active_player.name} still has {active_player.remaining_sentence} days in jail")
        if VERBOSE: print(f"You can pay £{constants.jail_release_fee} to be released today?")
        # if CLI
        # ans = input(f"Type Y to pay or N to stay in Jail")
        # else
        ans = random.sample(["Y", "N"], 1)
        if ans[0] in ["y", "Y" ,"Yes" ,"YES"]:
            active_player.transaction(-constants.jail_release_fee)
            active_player.out_jail()
            if VERBOSE: print(f"{active_player.name} has paid his bond and is released from jail")
        if ans[0] in ["n", "N", "No", "NO"]:
            active_player.remaining_sentence -= 1
            if VERBOSE: print(f"{active_player.name} now has {active_player.remaining_sentence} days in jail")
    # if VERBOSE: input("jail dialog")

def special_space(active_player):
    pos = active_player.position

    if pos in [3, 18, 34]:
        # take_community_chest(active_player)
        if VERBOSE: print("take_community_chest(active_player)")
    if pos in [8,23,37]:
        # take_chance_card(active_player)
        card = chance.deal_card(active_player)
        if VERBOSE: print(chance.outcome)
    if pos in [5, 39]:
        if pos == 5:
            active_player.transaction(-100)
            board.free_parking += 100
            if VERBOSE: print(f"{active_player.name} pays £{100} in Tax")
        else:
            active_player.transaction(-200)
            board.free_parking += 200
            if VERBOSE: print(f"Ouch, {active_player.name} pays £{200} in Tax")
    if pos == 11:
        if VERBOSE: print("Just visiting jail")
    if pos == 21:
        if board.free_parking > 0:
            active_player.transaction(board.free_parking)
            board.free_parking = 0
            if VERBOSE: print(f"{active_player.name} receives £{board.free_parking} from Free Parking")
    if pos == 31:
        active_player.to_jail()
        if VERBOSE: print(f"{active_player.name} has been sent to jail")
    if pos == 0:
        if VERBOSE: print(f"{active_player.name} has passed Go!")

def purchase_space(active_player):

    pos = active_player.position
    space_name = board.spaces[pos]
    site_cost = board.site_cost[pos]
    bank = active_player.balance
    site_group = board.groups[pos]
    # ic(pos)
    # ic(space_name)
    # ic(site_cost)
    # ic(bank)
    # ic(site_group)
    # ic(active_player.complete_set[site_group])

    if board.owner[pos] == 'none':
        if VERBOSE: print(f"{active_player.name} with balance {bank} has option to buy {space_name} costing {site_cost}")
        if bank >= site_cost:
            if VERBOSE: print(f"{active_player.name} do you wish to purchase?")
            # ans = random.sample(["Y", "N"], 1)
            ans = "Y"
            if ans[0] == "Y":
                # purchase site, update board, debit balance
                active_player.transaction(-site_cost)
                active_player.no_sites += 1
                board.owner[pos] = active_player.id
                if VERBOSE: print(f"{active_player.name} is now the proud owner of {space_name}!")
                # determine if ap holds set, update player class
                active_player.site_colours[site_group] += 1

                # check player holds set
                if site_group in ['brown', 'purple']:
                    if active_player.site_colours[site_group] == 2:
                        active_player.complete_set[site_group] = True
                        if VERBOSE: print(f"Look out, {active_player.name} holds a monopoly of {site_group} sites!")
                if site_group in ['blue' ,'pink', 'orange', 'red','yellow', 'green']:
                    if active_player.site_colours[site_group] == 3:
                        active_player.complete_set[site_group] = True
                        if VERBOSE: print(f"Look out, {active_player.name} holds a monopoly of {site_group} sites!")

            if ans[0] == "N":
                if VERBOSE: print(f"{active_player.name} has chosen not to buy this dump, a wise move!")

def opponent_owns(active_player, players):
    pos = active_player.position
    space_name = board.spaces[pos]
    bank = active_player.balance
    buildings = ['brown', 'blue', 'pink', 'orange', 'red', 'yellow', 'green', 'purple']
    utilities = ['utility']
    stations = ['station']
    site_owner_id = board.owner[pos]
    site_owner = players[site_owner_id]
    site_group = board.groups[pos]

    # ic(pos)
    # ic(space_name)
    # ic(bank)
    # ic(site_owner_id)
    # ic(site_owner.name)
    # ic(site_group)

    if VERBOSE: print(f"{active_player.name} has landed on {space_name} owned by {site_owner.name}")
    if site_group in buildings:
        if site_owner.site_colours[site_group] < 3: # land rent only due
            rent = board.rents[pos][0]
            if VERBOSE: print(f"Phew, {active_player.name} only owes £{rent} in rent, got off lightly!")
        elif site_owner.site_colours[site_group] == 3: # player holds set
            no_houses = board.no_houses[pos]
            if no_houses == 0:
                rent = board.rents[pos][0] * 2
                if VERBOSE: print(f"Could be worse, {active_player.name} owes £{rent} in rent.")
            elif no_houses > 0:
                rent = board.rents[pos][no_houses]
                if VERBOSE: print(f"Ouch, {active_player.name} owes £{rent} in rent, better pay up!")
        if site_group in utilities:
            if site_owner.site_colours[site_group] == 1:
                rent = 4 * active_player.d1 + active_player.d2
                if VERBOSE: print(f"Could be worse, {active_player.name} owes £{rent} in utilities.")
            elif site_owner.site_colours[site_group] == 2:
                rent = 10 * active_player.d1 + active_player.d2
                if VERBOSE: print(f"Ouch, {active_player.name} owes £{rent} in utilities, time to cough up!")
        if site_group in stations:
                no_stations = site_owner.site_colours[site_group]
                # factorial to get station rent
                rent = factorial(25, no_stations)
                if VERBOSE: print(f"{active_player.name} owes £{rent} in station fees.")

        # debit ap, credit site owner
        active_player.balance -= rent
        site_owner.balance += rent
        # handle bankrupcy
        if active_player.balance < 0:
            if VERBOSE: print(f"{active_player.name} is bankrupt and is out of the game :( ")
            active_player.BANKRUPT = True
            # game ends now? highest balance + assets wins?
        input("#opponent_owns")

# config
no_players = 3
assert no_players <= constants.max_players, "Too many players allocated!"
names = ['Alice', 'Bob', 'Craig']
assert no_players <= len(names), "Not enough player names given!"
# print([len(name) for name in names])
# assert len(names)<6, "Max 5 characters in player names"
game_active = True
VERBOSE = True                  #additional print statements

# create a meeples order without repeat
meeples = ['hat','dog', 'car','thimble', 'iron']
meeples_list = random.sample(meeples, len(meeples))
# ic(meeples_list)

# cards, die & boards
chance = chance.Chance()
dice = dice.Dice()
board = board.Board()

# max_len = max([len(x) for x in board.spaces])
# ic(max_len)
# input()

# create play order, this becomes player ID
turn_order = random.sample(range(no_players),no_players)
# ic(turn_order)

# create a list of player objects, allocate names and meeples based on prior random lists
players = list()
for i in range(no_players):
    players.append(player.Player(names[turn_order[i]], meeples_list[i]))
    players[i].id = turn_order[i]
    # ic(players[i].name, players[i].meeple, players[i].id)

# start in player order
i: int = 0                  # player turn indexing
ROLL_DOUBLE = False          # player gets another die roll
IN_JAIL = False             # player in jail
turn: int = 0               # count turns

while game_active == True:

    # select the active player
    ap = players[i]
    if VERBOSE: print(f"It is {ap.name}'s turn")

    # player rolls die
    ROLL_DOUBLE = ap.roll_dice(dice)       # returns True if double

    # check if player is already in jail
    if ap.in_jail: IN_JAIL = True
    else: IN_JAIL = False

    if ap.BANKRUPT == True:
        continue

    if IN_JAIL:
        player_in_jail(ap, ROLL_DOUBLE)
        #TODO need to handle get out of jail card

    else:
        if VERBOSE: print(f"{ap.name} rolled {ap.d1} and {ap.d2} to move {ap.d1 + ap.d2}")
        ap.move()
        pos = ap.position
        if VERBOSE: print(f"{ap.name} moves to {board.spaces[pos]}")

        # player can take actions based on space condition
        # ic(pos)
        # ic(board.owner[pos])
        # ic(len(board.owner))
        # input("check owner")

        # test membership of player position in special spaces list
        if pos in board.special:
            special_space(ap)

        # not special
        else:
            if board.owner[pos] == 'none':                       # space not owned
                if VERBOSE: print("space_not_owned()")
                purchase_space(ap)
            elif board.owner[pos] == ap.name:      # space owned by active player
                if VERBOSE: print("active_player_owns()")
            else:      # space owned by another player
                if VERBOSE: print("opponent_owns()")
                opponent_owns(ap, players)

        # buy or sell houses
        holds_complete_set = any(value == True for value in ap.complete_set.values())
        if holds_complete_set and not ap.in_jail:
            if VERBOSE: print(f"{ap.name} is eligible to purchase houses")
            if VERBOSE: print("property_purchase(active_player)")

        # turn counter
        state.game_state(turn, ap, board)
        turn += 1

    if ROLL_DOUBLE:
        i = i
        ROLL_DOUBLE = False
        if VERBOSE: print("Player has another Roll")
    else:
        ap.doubles_rolled = 0
        i = (i + 1) % no_players

    if VERBOSE: print("check_game_active()")
    if turn % 100 == 0:
        input("Game break")




