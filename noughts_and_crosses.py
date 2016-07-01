
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
    print(symbols[slot])


def make_move(grid, player):
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


def play(grid):
    winner = False
    cur_player = -1
    while not winner:
        cur_player *= -1
        newgrid = make_move(grid, cur_player)
        show_grid(newgrid)
        winner = check_win(newgrid)
    print("Congratulations Player %s" % cur_player)


def check_hor(grid):
    indices = [1, 4, 7]
    for ix in indices:
        if (grid[ix] != 0) and (grid[ix - 1] == grid[ix] == grid[ix + 1]):
            return True
    return False


def check_ver(grid):
    indices = [3, 4, 5]
    for ix in indices:
        if (grid[ix] != 0) and (grid[ix - 3] == grid[ix] == grid[ix + 3]):
            return True
    return False


def check_diag(grid):
    if grid[4] != 0:
        if grid[0] == grid[4] == grid[8]:
            return True
        elif grid[2] == grid[4] == grid[6]:
            return True
    return False


def check_win(grid):
    winhor = check_hor(grid)
    winver = check_ver(grid)
    windiag = check_diag(grid)
    if winhor or winver or windiag:
        return True
    else:
        return False


def main():
    grid = make_grid()
    show_grid(grid)
    play(grid)


if __name__ == "__main__":
    main()
