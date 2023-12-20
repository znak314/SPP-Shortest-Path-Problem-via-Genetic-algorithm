import random
from utils import POPULATION_SIZE, MUTATION_PROBABILITY

class Genetic_algo:
    def __init__(self, distance_matrix, start, end):
        self.distance_matrix = distance_matrix
        self.start_point = start
        self.finish_point = end
        self.population = []
        self.Paths = []
        self.results = []

    def create_population(self):
        size = len(self.distance_matrix) - 1
        count = 0
        while count < POPULATION_SIZE:
            current = self.start_point
            path = [current]
            path_value = 0
            while current != self.finish_point:
                possible_moves = []
                for i in range(size):
                    if self.distance_matrix[current][i] != 0 and i not in path:
                        possible_moves.append(i)

                if len(possible_moves) == 0:
                    path.clear()
                    break

                random_move = random.choice(possible_moves)
                while random_move in path:
                    random_move = random.choice(possible_moves)
                path.append(random_move)
                path_value += self.distance_matrix[current][random_move]
                current = random_move
            if len(path) > 10:
                self.population.append(path)
                self.Paths.append(path_value)
                count += 1
        count = 0
        for i in self.population:
            print(f"{count}",i)
            count += 1

    def find_solution(self, num_of_iterations):
        for i in range(num_of_iterations):
            min_index = self.find_best_path()
            self.results.append(self.Paths[min_index])
            S1 = self.population[min_index]
            random_index = self.generate_index(0,len(self.population) - 1,min_index)
            S2 = self.population[random_index]

            print(f"{i} :HERE")
            it = 0
            while not self.is_possible_cross(S1,S2):
                random_index = self.generate_index(0, len(self.population) - 1, min_index)
                S2 = self.population[random_index]
                it += 1
            print(f"{i} : Possible")

            x, y = self.is_possible_cross(S1, S2)
            S = self.crossover(S1,S2,x,y)
            if random.random() < MUTATION_PROBABILITY:
                S = self.mutation(S)
                print(f"{i} :mutated")

            # Add to population
            length = self.find_path_value(S)
            self.population.append(S)
            self.Paths.append(length)

            # Delete worst
            worst = self.find_worst_path()
            self.Paths.pop(worst)
            self.population.pop(worst)



    def generate_index(self,min,max, not_value):
        rand_ind = random.randint(min,max)
        while not_value == rand_ind:
            rand_ind = random.randint(0, max)
        return rand_ind

    def find_best_path(self):
        min_value = self.Paths[0]
        min_index = 0
        i = 1
        while i < len(self.Paths) - 1:
            if min_value > self.Paths[i]:
                min_value = self.Paths[i]
                min_index = i
            i += 1
        return min_index

    def is_possible_cross(self, best_path, rand_path):
        i = 1
        j = len(rand_path) - 1
        while i < len(best_path):
            while j != 0:
                if best_path[i] == rand_path[j]:
                    return i,j
                j -= 1
            i += 1
        return 0

    def crossover(self, S1, S2, first_ind, second_ind):
        S = []
        for i in range(first_ind):
            S.append(S1[i])
        i = second_ind
        while(i < len(S2)):
            S.append(S2[i])
            i += 1
        return S

    def mutation(self,gene):
        rand1 = random.randint(0, len(gene) - 2)
        rand2 = random.randint(rand1, len(gene) - 1)

        v1 = gene[rand1]
        v2 = gene[rand2]

        new_path = self.find_random_path(v1, v2)
        mutant = self.replace_path_part(gene,new_path, rand1, rand2)
        return gene


    def find_random_path(self, current_v, finish_v):
        path = [current_v]
        while current_v != finish_v:
            possible_moves = [
                i for i in range(len(self.distance_matrix))
                if self.distance_matrix[current_v][i] > 0 and i not in path
            ]
            if not possible_moves:
                break

            if finish_v in possible_moves:
                move = finish_v
            else:
                move = random.choice(possible_moves)
            path.append(move)
            current_v = move
        return path

    def replace_path_part(self, S, replacement, index1, index2):
        part1 = S[:index1 + 1]
        part2 = S[index2+1:]
        replaced = part1 + replacement + part2
        return replaced

    def find_worst_path(self):
        max_value = self.Paths[0]
        max_index = 0
        i = 1
        while i < len(self.Paths) - 1:
            if max_value < self.Paths[i]:
                max_value = self.Paths[i]
                max_index = i
            i += 1
        return max_index

    def find_path_value(self, vertexes):
        path_length = 0
        for i in range(len(vertexes) - 1):
            v1 = vertexes[i]
            v2 = vertexes[i + 1]
            path_length += self.distance_matrix[v1][v2]
        return path_length
