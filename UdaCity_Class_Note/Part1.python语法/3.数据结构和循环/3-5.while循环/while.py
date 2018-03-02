card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)


循环

#判断字符长度是否大于140，如果大于则break，然后切片前140个字符