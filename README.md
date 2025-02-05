def horse2(position):

    # Возможные ходы

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    # Позиция коня

    x = ord(position[0]) - ord("a")
    y = int(position[1]) - 1

    # На какие позиции может ходить

    total_moves = []

    for move in moves:
        ord_x = x + move[0]
        int_y = y + move[1]

        if 0 <= ord_x < 8 and 0 <= int_y < 8:
            new_position = chr(ord_x + ord("a")) + str(int_y + 1)

            total_moves.append(new_position)

    return total_moves


print(horse2("e4"))
