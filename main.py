import random
from tqdm import tqdm

def generateCard():
    card = [[0 for x in range(5)] for y in range(5)]
    for col in range(5):
        numbers = random.sample(range(col*15+1, (col+1)*15+1), 5)

        for row in range(5):
            card[row][col] = numbers[row]

    card[2][2] = "F"
    return card

def simulateGame(players):
    cards = [generateCard() for _ in range(players)]
    rowfilled = [[0, 0, 1, 0, 0] for _ in range(players)]
    colfilled = [[0, 0, 1, 0, 0] for _ in range(players)]

    balls = list(range(1, 76))
    random.shuffle(balls)
    for ball in balls:
        any_row_win = False
        any_col_win = False
        for i, card in enumerate(cards):
                for row in range(5):
                    for col in range(5):
                        if card[row][col] == ball:
                            rowfilled[i][row] += 1
                            colfilled[i][col] += 1

                row_win = 5 in rowfilled[i]
                col_win = 5 in colfilled[i]

                if row_win and col_win:
                    any_row_win = True
                    any_col_win = True
                elif row_win:
                    any_row_win = True
                elif col_win:
                    any_col_win = True
        if any_row_win and any_col_win:
            return 2
        elif any_col_win:
            return 1
        elif any_row_win:
            return 0

def main():
    seed_in = input("Seed (blank=random): ").strip()
    if seed_in:
        random.seed(int(seed_in))
    runs = int(input("How many simulations of the Bingo Game? "))
    win = [0,0,0]
    players = int(input("How many players? "))
    for _ in tqdm(range(runs), desc = "Running simulations"):
        win[simulateGame(players)] += 1
    print("Row wins:", win[0])
    print("Column wins:", win[1])
    print("Ties:", win[2])
    row_win_pct = (win[0] + win[2] / 2) / runs * 100
    print(f"Row win %: {row_win_pct:.2f}%")


if __name__ == "__main__":
    main()
