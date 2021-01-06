import pathlib
import random

import json

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, size: Tuple[int, int], randomize: bool=True,
        max_generations: Optional[float]=float('inf')) -> None:

        self.rows, self.cols = size

        self.prev_generation = self.create_grid()

        self.curr_generation = self.create_grid(randomize=randomize)

        self.max_generations = max_generations

        self.n_generation = 1

    def create_grid(self, randomize: bool=False) -> Grid:
        # Copy from previous assignment
        grid = []

        for i in range(self.rows):
            new_line = []
            for j in range(self.cols):
                if randomize:
                    new_line.append(random.randint(0, 1))
                else:
                    new_line.append(0)
            grid.append(new_line)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        list_of_neighbors = []
        for i in range(cell[0] - 1, cell[0] + 2):
            if i >= self.rows or i < 0:
                continue
            for j in range(cell[1] - 1, cell[1] + 2):
                if j >= self.cols or j < 0:
                    continue
                if i == cell[0] and j == cell[1]:
                    continue
                list_of_neighbors.append(self.curr_generation[i][j])
        return list_of_neighbors

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        temp_grid = self.create_grid(randomize=False)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.curr_generation[i][j] == 1:
                    if 2 <= sum(self.get_neighbours((i, j))) <= 3:
                        temp_grid[i][j] = 1
                    else:
                        temp_grid[i][j] = 0
                else:
                    if sum(self.get_neighbours((i, j))) == 3:
                        temp_grid[i][j] = 1
                    else:
                        temp_grid[i][j] = 0
        return temp_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.n_generation += 1

    @property
    def is_max_generations_exceed(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return (self.n_generation >= self.max_generations)

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        rows = len(self.prev_generation)
        for i in range(rows):
            cols = len(self.prev_generation[i])
            for j in range(cols):
                if self.curr_generation[i][j] != self.prev_generation[i][j]:
                    return True
        return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename) as file:
            data = json.load(file)

        game = GameOfLife((data['rows'], data['cols']),
                          randomize=False,
                          max_generations=data['max_generations'])

        game.prev_generation = data['prev_generation']
        game.curr_generation = data['curr_generation']
        game.n_generation = data['n_generation']

        return game



    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        json_data = {
            'prev_generation': self.prev_generation,
            'curr_generation': self.curr_generation,
            'max_generations': self.max_generations,
            'rows': self.rows, 'cols': self.cols,
            'n_generation': self.n_generation
        }

        with open(filename, 'w') as file:
            json.dump(json_data, file)
