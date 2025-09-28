import random
from abc import ABC, abstractmethod
from Maze import Maze, Cell, State
from Maze_generator import MazeGenerator


class DfsGenerator(MazeGenerator):

    @classmethod
    def get_neighbours(cls, cell, width, height, used):
        """
        Возвращает список непосещённых соседних клеток на расстоянии 2 шага.
        :param cell: Текущая клетка, для которой ищутся соседи
        :param width: Ширина лабиринта
        :param height: Высота лабиринта
        :param used: Матрица посещённых клеток
        :return: Список непосещённых соседних клеток на расстоянии 2 шага
        """
        # Записывает в neighbours непосещённых соседей cell
        neighbours = []
        x = cell.x
        y = cell.y
        if x + 2 < height and used[x + 2][y] == 0:
            neighbours.append(Cell(x + 2, y))
        if y + 2 < width and used[x][y + 2] == 0:
            neighbours.append(Cell(x, y + 2))
        if x - 2 >= 0 and used[x - 2][y] == 0:
            neighbours.append(Cell(x - 2, y))
        if y - 2 >= 0 and used[x][y - 2] == 0:
            neighbours.append(Cell(x, y - 2))
        return neighbours

    @classmethod
    def create(cls, width, height, rand):
        """
        Создание лабиринта
        :param width: Ширина создаваемого лабиринта
        :param height: Высота создаваемого лабиринта
        :param rand: Объект для генерации случайных чисел
        :return: Лабиринт
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Ширина и высота должны быть целочисленными значениями.")
        if width <= 2 or height <= 2:
            raise ValueError("Минимальные размеры лабиринта должны быть больше 2.")

        if rand is not None and not isinstance(rand, random.Random):
            raise TypeError("Аргумент rand должен быть объектом random.Random или None.")

        maze = Maze(width, height)
        # Создаем used внутри метода вместо классовой переменной
        used = []
        for i in range(maze.height):
            used.append([0 for i in range(maze.width)])

        stack = [Cell(1, 1)]
        used[1][1] = 1
        curr = Cell(1, 1)

        while len(stack) > 0:
            neighbours = cls.get_neighbours(curr, maze.width, maze.height, used)
            if len(neighbours) > 0:
                stack.append(curr)
                k = neighbours[random.randint(0, len(neighbours) - 1)]
                new = Cell((curr.x + k.x) // 2, (curr.y + k.y) // 2)  # Стена между двумя клетками
                maze.set(new, State.space)
                used[k.x][k.y] = 1
                curr = k
            else:
                curr = stack.pop()
        maze.set_doors(rand)
        return maze