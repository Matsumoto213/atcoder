def card_rank(card):
    rank_dict = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
    suit_dict = {
            "s": 3,
            "h": 2,
            "d": 1,
            "c": 0,
        }
    return int(rank_dict.get(card[0], card[0]))*4 + suit_dict[card[1]]


card_list = ["Ks", "7d", "Ah",  "3c", "2s", "Td", "Kc"]

# ソート前の並び
print(card_list)
# ['Ks', '7d', 'Ah', '3c', '2s', 'Td', 'Kc']

# 強い順にソート
card_list.sort(key=card_rank, reverse=True)
print(card_list)
# ['Ah', 'Ks', 'Kc', 'Td', '7d', '3c', '2s']