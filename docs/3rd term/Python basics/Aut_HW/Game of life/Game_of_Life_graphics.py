"""Game of Life"""

# старая посылка
# https://contest.yandex.ru/contest/29167/run-report/54247495/

# новая посылка
# https://contest.yandex.ru/contest/29167/run-report/54829714/

import pygame

# параметры экрана
DISPLAY_WIDTH = 620
DISPLAY_HEIGHT = 480
# размер клетки
CELL_SIZE = 20
# цвета
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
SILVER = (192, 192, 192, 255)


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


def draw_generation(display, generation):
    for row in range(len(generation)):
        for col in range(len(generation[0])):
            # в условиях прописано != BLACK/WHITE чтобы
            # не рисовать уже существующие клетки
            if cell(generation, row, col) == 1\
                and display.get_at((
                                    row*CELL_SIZE+1,
                                    col*CELL_SIZE+1
                                    )) != BLACK:
                # +/- 1 для избежания перекрытия с сеткой
                pygame.draw.rect(display, BLACK, [row*CELL_SIZE+1,
                                                  col*CELL_SIZE+1,
                                                  CELL_SIZE-1,
                                                  CELL_SIZE-1])

            elif cell(generation, row, col) == 0\
                and display.get_at((
                                    row*CELL_SIZE+1,
                                    col*CELL_SIZE+1
                                    )) != WHITE:
                pygame.draw.rect(display, WHITE, [row*CELL_SIZE+1,
                                                  col*CELL_SIZE+1,
                                                  CELL_SIZE-1,
                                                  CELL_SIZE-1])


def game_loop():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Game of Life')

    # сетка
    for i in range(0, DISPLAY_HEIGHT, CELL_SIZE):
        pygame.draw.line(gameDisplay, SILVER, (0, i), (DISPLAY_WIDTH, i))
    for i in range(0, DISPLAY_WIDTH, CELL_SIZE):
        pygame.draw.line(gameDisplay, SILVER, (i, 0), (i, DISPLAY_HEIGHT))

    # задаем начальную генерацию,
    gen = [[0]*(DISPLAY_HEIGHT//CELL_SIZE)
           for i in range(DISPLAY_WIDTH//CELL_SIZE)]
    # для удобства изначально прописаны циклы длины 2 и 3
    for i, j in Cycle_3:
        gen[i][j] = 1

    draw_generation(gameDisplay, gen)
    pygame.display.update()

    finished = 0
    while not finished:
        for event in pygame.event.get():
            # блок клавиш
            if event.type == pygame.KEYDOWN:
                # новое поколение при RIGHT
                if event.key == pygame.K_RIGHT:
                    gen = get_next_generation(gen)
                    draw_generation(gameDisplay, gen)

                # отчистка поля при SPACE
                elif event.key == pygame.K_SPACE:
                    gen = [[0]*(DISPLAY_HEIGHT//CELL_SIZE)
                           for i in range(DISPLAY_WIDTH//CELL_SIZE)]
                    draw_generation(gameDisplay, gen)

            # блок мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # при нажати LMB, если клетка не черная/живая/1,
                # на перекрашивается в черный и gen[row][col] = 1
                if event.button == 1\
                        and gameDisplay.get_at(event.pos) != BLACK:
                    row, col = map(lambda x: x//CELL_SIZE, event.pos)
                    gen[row][col] = 1
                    pygame.draw.rect(gameDisplay, BLACK, [row*CELL_SIZE+1,
                                                          col*CELL_SIZE+1,
                                                          CELL_SIZE-1,
                                                          CELL_SIZE-1])

                # при нажати RMB, если клетка не белая/мертвая/0,
                # на перекрашивается в белый и gen[row][col] = 0
                elif event.button == 3\
                        and gameDisplay.get_at(event.pos) != WHITE:
                    row, col = map(lambda x: x//CELL_SIZE, event.pos)
                    gen[row][col] = 0
                    pygame.draw.rect(gameDisplay, WHITE, [row*CELL_SIZE+1,
                                                          col*CELL_SIZE+1,
                                                          CELL_SIZE-1,
                                                          CELL_SIZE-1])

            elif event.type == pygame.QUIT:
                finished = 1

            pygame.display.update()
    pygame.quit()


Cycle_2 = [[4, 4], [4, 5], [4, 6]]
Cycle_3 = [[2, 4], [2, 5], [2, 6],
           [2, 10], [2, 11], [2, 12],
           [4, 2], [5, 2], [6, 2],
           [4, 7], [5, 7], [6, 7],
           [4, 9], [5, 9], [6, 9],
           [4, 14], [5, 14], [6, 14],
           [7, 4], [7, 5], [7, 6],
           [7, 10], [7, 11], [7, 12],
           [9, 4], [9, 5], [9, 6],
           [9, 10], [9, 11], [9, 12],
           [10, 2], [11, 2], [12, 2],
           [10, 7], [11, 7], [12, 7],
           [10, 9], [11, 9], [12, 9],
           [10, 14], [11, 14], [12, 14],
           [14, 4], [14, 5], [14, 6],
           [14, 10], [14, 11], [14, 12]]

if __name__ == "__main__":
    game_loop()
