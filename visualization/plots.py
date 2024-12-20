import matplotlib.pyplot as plt

def plot_epidemic_curve(results):
    days = [step['day'] for step in results]
    infected = [step['infected'] for step in results]
    plt.plot(days, infected)
    plt.xlabel("Días")
    plt.ylabel("Número de Infectados")
    plt.show()
