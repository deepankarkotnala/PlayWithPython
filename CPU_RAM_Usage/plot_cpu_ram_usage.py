import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('cpu_ram_data.csv')
    x = data['x_value']
    y1 = data['cpu_usage']
    y2 = data['ram_usage']

    plt.cla()

    plt.plot(x, y1, label='CPU Usage')
    plt.plot(x, y2, label='RAM Usage')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()