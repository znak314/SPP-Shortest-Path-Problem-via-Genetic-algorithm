import matplotlib.pyplot as plt

def show_plot(iterations_x, results_y):
    plt.plot(iterations_x, results_y)
    plt.ylabel('Path length')
    plt.xlabel('Iterations')
    plt.show()