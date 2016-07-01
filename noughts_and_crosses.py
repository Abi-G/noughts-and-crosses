
def make_grid():
    grid = ["."] * 9
    return grid


def show_grid(grid):
    for slot in grid[0:3]:
        print(slot, " ", end="")
    print("\n")
    for slot in grid[3:6]:
        print(slot, " ", end="")
    print("\n")
    for slot in grid[6:8]:
        print(slot, " ", end="")
    for slot in grid[8]:
        print(slot)


def make_move(grid, player):
    while True:
        print("Player %s please make your move by typing 1-9:\n>" % player, end="")
        move = int(input())
        symbols = {
            1: "X",
            2: "0"
        }
        if grid[move - 1] != ".":
            print("Invalid move, please play again")
        else:
            grid[move - 1] = symbols[player]
            return grid


def play(grid):
    winner = False
    cur_player = 2
    while not winner:
        if cur_player == 1:
            cur_player = 2
        else:
            cur_player = 1
        newgrid = make_move(grid, cur_player)
        show_grid(newgrid)
        winner = check_win(newgrid)
    print("Congratulations Player %s" % cur_player)


def check_hor(grid):
    indices = [1, 4, 7]
    for ix in indices:
        if (grid[ix] != ".") and (grid[ix - 1] == grid[ix] == grid[ix + 1]):
            return True
    return False


def check_ver(grid):
    indices = [3, 4, 5]
    for ix in indices:
        if (grid[ix] != ".") and (grid[ix - 3] == grid[ix] == grid[ix + 3]):
            return True
    return False


def check_diag(grid):
    if grid[4] != ".":
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
