maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]
visited = []
exits = []


def not_valid_point(x, y):
    return y < 0 or x < 0 or x >= len(maze[0]) or y >= len(maze) or maze[y][x] == "#"


def find_exits(x, y):
    if not_valid_point(x, y):
        return

    if (x, y) not in visited:
        visited.append((x, y))
    else:
        return

    if maze[y][x] != " " and maze[y][x] not in exits:
        exits.append(maze[y][x])

    find_exits(x, y + 1)
    find_exits(x, y - 1)
    find_exits(x + 1, y)
    find_exits(x - 1, y)


x, y = map(int, input().split())

if not_valid_point(x, y):
    print("Неверные координаты")
    exit(0)

find_exits(x, y)

if len(exits) == 0:
    print("Выходов нет")
else:
    for i in exits:
        print(i, end=' ')
    print()
