from utils import player, board
from icecream import ic
def game_state(turn, Player, Board):
    p = Player
    b = Board
    name_length = b.max_len
    # ic(turn, p.name, p.d1, p.d2, p.position)
    # print(b.spaces[p.position])
    # print(b.spaces[11])
    # ic(p.doubles_rolled)
    # ic(p.balance)
    # ic(p.remaining_sentence)
    # ic(p.chance_id)

    if turn%10==0 or turn==0:
        print("Turn   Name   D1 D2 P   Space                   DOUB  Balance   JAIL Chance  ")
    print(f"{turn:05d}, {p.name:5}, {p.d1}, {p.d2}, {p.position:02d}, {b.spaces[(p.position)]:21}, {p.doubles_rolled:5}, {p.balance:7}, {p.remaining_sentence:5}, {p.chance_id:2}")

