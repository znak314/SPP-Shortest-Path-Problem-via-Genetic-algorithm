from random import *
from utils import *

class Graph:
    def __init__(self):
        self.size = VERTEXES
        self.distances_matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.fill_matrix()

    def fill_matrix(self):
        # put minimum in each row
        self.put_minimum()
        while(not self.can_exist()):
            self.distances_matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
            self.put_minimum()
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random() < MAX_DEGREE / self.size and self.can_put(i, j):
                    distance = randint(MIN_DIST, MAX_DIST)
                    self.distances_matrix[i][j] = distance
                    self.distances_matrix[j][i] = distance

    def can_put(self, row, column):
        if row == column:
            return False

        roads_in_column = sum(1 for i in range(len(self.distances_matrix)) if self.distances_matrix[i][column] != 0)
        roads_in_row = sum(1 for i in range(len(self.distances_matrix)) if self.distances_matrix[row][i] != 0)

        return roads_in_row < MAX_DEGREE and roads_in_column < MAX_DEGREE

    def put_minimum(self):
        rand = Random()
        for i in range(len(self.distances_matrix)):
            column = rand.randint(0, len(self.distances_matrix) - 1)
            while column == i:
                column = rand.randint(0, len(self.distances_matrix) - 1)
            distance = rand.randint(MIN_DIST, MAX_DIST)
            self.distances_matrix[i][column] = distance
            self.distances_matrix[column][i] = distance

    def can_exist(self):
        for i in range(len(self.distances_matrix)):
            roads = 0
            for j in range(len(self.distances_matrix)):
                if self.distances_matrix[i][j] != 0:
                    roads += 1
            if roads > MAX_DEGREE or roads == 0:
                return False
        return True

    def print_distances_matrix(self):
        for row in self.distances_matrix:
            print(' '.join(f"{elem: <4}" for elem in row))