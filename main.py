from graph import Graph
from generator import Genetic_algo
from utils import ITERATIONS
from Plot import *



def main():
    graph = Graph()
    graph.print_distances_matrix()
    solver = Genetic_algo(graph.distances_matrix,1,5)
    solver.create_population()

    # Вибір найкращого + рандома
    # При виборі врахувати умову, схрещення, якщо не можна схрестити - беремого іншого
    # Умова схрещення: є спільна точка з відповідним значенням

    # Схрещуємо по спільний точці посередині

    #print(solver.find_best_path())
    solver.find_solution(ITERATIONS)
    show_plot(list(range(1, ITERATIONS + 1)), solver.results)
    print(solver.Paths[solver.find_best_path()])

if __name__ == "__main__":
    main()