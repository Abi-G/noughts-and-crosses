import random


def make_grid():
    grid = [0] * 9
    return grid


def show_grid(grid):
    symbols = {
        0: ".",
        1: "X",
        -1: "0"
    }
    for slot in grid[0:3]:
        print(symbols[slot], " ", end="")
    print("\n")
    for slot in grid[3:6]:
        print(symbols[slot], " ", end="")
    print("\n")
    for slot in grid[6:8]:
        print(symbols[slot], " ", end="")
    print(symbols[grid[8]])


def make_move(grid, player):
    grid = grid[:]   # copy grid
    while True:
        playerprint = 2 if player == -1 else 1
        print("Player %s please make your move by typing 1-9:\n>" % playerprint, end="")
        try:
            move = int(input())
        except ValueError:
            print("Invalid move")
            continue
        if not (0 < move <= 9):
            print("Invalid move - out of range")
        elif grid[move - 1] != 0:
            print("Invalid move, please play again")
        else:
            grid[move - 1] = player
            return grid


def random_ai(grid, player):
    grid = grid[:]   # copy grid
    possible_movs = []
    for (ix, val) in enumerate(grid):
        if val == 0:
            possible_movs.append(ix)
    choice = random.choice(possible_movs)
    print("CPU move:", choice)
    grid[choice] = player
    return grid


def play(grid, tpg):
    cur_player = 1
    while True:
        if cur_player == -1 and not tpg:
            grid = random_ai(grid, cur_player)
        else:
            grid = make_move(grid, cur_player)
        show_grid(grid)
        result = check_win(grid)
        if result != 0:
            break
        cur_player *= -1
    if result == 2:
        print("It's a draw!")
    else:
        playerprint = 2 if cur_player == -1 else 1
        print("Congratulations Player %s" % playerprint)


def check_hor(grid):
    for ix in [1, 4, 7]:
        if abs(grid[ix - 1] + grid[ix] + grid[ix + 1]) == 3:
            return grid[ix]
    return 0


def check_ver(grid):
    for ix in [3, 4, 5]:
        if abs(grid[ix - 3] + grid[ix] + grid[ix + 3]) == 3:
            return grid[ix]
    return 0


def check_diag(grid):
    if abs(grid[0] + grid[4] + grid[8]) == 3:
        return grid[4]
    if abs(grid[2] + grid[4] + grid[6]) == 3:
        return grid[4]
    return 0


def check_win(grid):
    winhor = check_hor(grid)
    winver = check_ver(grid)
    windiag = check_diag(grid)
    winner = winhor or winver or windiag
    if winner:
        return winner
    if 0 not in grid:
        return 2
    return 0


def main():
    grid = make_grid()
    show_grid(grid)
    play(grid, False)


if __name__ == "__main__":
    main()
