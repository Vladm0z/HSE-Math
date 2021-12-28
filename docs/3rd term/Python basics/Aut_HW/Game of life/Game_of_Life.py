"""This module does blah blah."""


# cell(r, c) возвращает состояние клетки
# функция сделана для того, чтобы клетки вне доски считались мертвыми
def cell(generation, row, col):
    if 0 <= row < len(generation):
        if 0 <= col < len(generation[0]):
            return generation[row][col]
    return 0


# подсчет количества живых соседних клеток
# считается сумма состояний клеток матрицы 3*3\
# с центром в выбранной за исключением ее самой
def num_alive(generation, row, col):
    return cell(generation, row+1, col+1)\
        + cell(generation, row+1, col)\
        + cell(generation, row+1, col-1)\
        + cell(generation, row, col+1)\
        + cell(generation, row, col-1)\
        + cell(generation, row-1, col+1)\
        + cell(generation, row-1, col)\
        + cell(generation, row-1, col-1)


# следующее поколение
def get_next_generation(generation):
    # создание пустого поля
    next_generation = [[0]*len(generation[0]) for i in range(len(generation))]
    for row in range(len(generation)):
        for col in range(len(generation[0])):
            # замена 0 на 1, если клетка соответствует условиям

            if num_alive(generation, row, col) == 3:
                next_generation[row][col] = 1

            elif (cell(generation, row, col) == 1
                    and num_alive(generation, row, col) == 2):
                next_generation[row][col] = 1

    return next_generation


generation = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
]

next_generation = get_next_generation(generation)
print(next_generation)
