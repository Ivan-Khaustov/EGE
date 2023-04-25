"""
    heap  - размер кучи в данный момент
    moves - номер тукущего хода
    to    - номер хода, который мы исследуем (Петя: 1 - 3 - 5; Ваня: 2 - 4 - 6)
    p     - предыдущий ход Пети
    v     - предыдущий ход Вани

    1 - +1 | 2 - +2 | 3 - *2
"""
def game(heap, moves, to, p, v):
    if heap >= 21:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    if (moves + 1) % 2 != 0:
        if p == 1:
            result = [game(heap + 2, moves + 1, to, 2, v), game(heap * 2, moves + 1, to, 3, v)]
        elif p == 2:
            result = [game(heap + 1, moves + 1, to, 1, v), game(heap * 2, moves + 1, to, 3, v)]
        elif p == 3:
            result = [game(heap + 2, moves + 1, to, 2, v), game(heap + 1, moves + 1, to, 1, v)]
        else:
            result = [game(heap + 1, moves + 1, to, 1, v), game(heap + 2, moves + 1, to, 2, v),
                      game(heap * 2, moves + 1, to, 3, v)]
    else:
        if v == 1:
            result = [game(heap + 2, moves + 1, to, p, 2), game(heap * 2, moves + 1, to, p, 3)]
        elif v == 2:
            result = [game(heap + 1, moves + 1, to, p, 1), game(heap * 2, moves + 1, to, p, 3)]
        elif v == 3:
            result = [game(heap + 2, moves + 1, to, p, 2), game(heap + 1, moves + 1, to, p, 1)]
        else:
            result = [game(heap + 1, moves + 1, to, p, 1), game(heap + 2, moves + 1, to, p, 2),
                      game(heap * 2, moves + 1, to, p, 3)]
    # any(<массив>) - функция, которая возвращает true, если хотя бы одно значение в массиве истинно
    # Обычное условие, не накладывающее безусловный выигрыш.
    # return any(h)
    # Условие, которое не допускает ни одной возможности победы противника ("гарантированно", "независимо от того", и пр.)
    # all(<массив>) - функция, которая возвращает true, если все значения в массиве истины
    return any(result) if (moves + 1) % 2 == to % 2 else all(result)

print(f'19: {min(s for s in range(1, 21) if not game(s, 0, 1, 0, 0) and game(s, 0, 3, 0, 0))}')
print(f'20: {[s for s in range(1, 21) if not game(s, 0, 2, 0, 0) and game(s, 0, 4, 0, 0)]}')
print(f'21: {max(s for s in range(1, 21) if not game(s, 0, 1, 0, 0) and not game(s, 0, 3, 0, 0) and game(s, 0, 5, 0, 0))}')
