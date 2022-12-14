from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange

x_data, y_data = [], []

figure = plt.figure()

line, = plt.plot_date(x_data, y_data, '-')
# line = plt.plot_date(x_data, y_data, '-')[0]

print(type(line))
print(f"{line=}")

def update(frame):
    x_data.append(datetime.now())
    y_data.append(randrange(0, 100))
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=1000)

plt.show()