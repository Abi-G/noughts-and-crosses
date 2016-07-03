import random
import sys


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


def user_move(grid, player):
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


def minimax(grid, player):
    grid = grid[:]
    branches = get_scores(grid, player, 0)
    wins = []
    draws = []
    for (ix, val) in branches.items():
        if val == player:
            wins.append(ix)
        if val == 0:
            draws.append(ix)
    if wins:
        move = random.choice(wins)
    elif draws:
        move = random.choice(draws)
    else:
        move = random.choice(list(branches.keys()))
    print("CPU move:", (move + 1))
    grid[move] = player
    return grid


def get_scores(grid, player, depth):
    scores = {}
    for (ix, val) in enumerate(grid):
        if val != 0:
            continue
        newgrid = grid[:]
        newgrid[ix] = player
        result = check_win(newgrid)
        if result != 0:
            if result == 2:
                scores[ix] = 0
            else:
                scores[ix] = result
        else:
            scores[ix] = get_scores(newgrid, player * -1, depth + 1)
    if depth == 0:
        return scores
    if player == 1:
        return max(scores.values())
    else:
        return min(scores.values())


def play(grid, p1func, p2func):
    cur_player = 1
    while True:
        if cur_player == 1:
            grid = p1func(grid, cur_player)
        else:
            grid = p2func(grid, cur_player)
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


def choose_players():
    nargs = len(sys.argv)
    if nargs == 1:
        return (user_move, minimax)
    if nargs == 3:
        pl_options = {
            "user": user_move,
            "random": random_ai,
            "minimax": minimax
        }
        try:
            p1func = pl_options[sys.argv[1]]
            p2func = pl_options[sys.argv[2]]
        except KeyError:
            print("\nPlease select player 1 and player 2 options from the following:")
            print(list(pl_options.keys()))
            sys.exit(1)
        return (p1func, p2func)
    else:
        print("\nPlease either enter options for both players, or leave the player options blank\n")
        sys.exit(1)


def main():
    p1func, p2func = choose_players()
    grid = make_grid()
    show_grid(grid)
    play(grid, p1func, p2func)


if __name__ == "__main__":
    main()
