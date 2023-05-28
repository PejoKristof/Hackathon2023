import itertools

def generate_dobble_deck(n):
    symbols = list(range(1, n + 1))
    deck = []
    for i in range(n):
        card = [i + 1]
        for j in range(n - 1):
            symbol = symbols[(j + i) % (n - 1)]
            card.append(symbol)
        deck.append(card)
    for i in range(n, 2 * n):
        card = [i + 1]
        for j in range(n - 1):
            symbol = symbols[(j + i - n) % (n - 1)]
            card.append(symbol + n)
        deck.append(card)
    return deck


def print_dobble_deck(deck):
    for card in deck:
        print(' '.join(str(symbol) for symbol in card))


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: python main.py n')
    else:
        n = int(sys.argv[1])
        deck = generate_dobble_deck(n)
        print_dobble_deck(deck)