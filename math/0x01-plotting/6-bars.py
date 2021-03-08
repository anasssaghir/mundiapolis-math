#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

fig, px = plt.subplots()

people_labels = ['Farrah', 'Fred', 'Felicia']
fruits_labels = ('apples', 'bananas', 'oranges', 'peaches')
colors = ('red', 'yellow', '#ff8000', '#ffe5b4')
width = 0.5
sub_total = np.zeros(3)

for i, n_fruits in enumerate(fruit):
    px.bar(
        people_labels,
        n_fruits,
        width,
        bottom=sub_total,
        label=fruits_labels[i],
        color=colors[i]
    )
    sub_total += n_fruits

px.set_ylabel('Quantity of Fruit')
px.set_ylim(0, 80)
px.set_title('Number of Fruit per Person')
px.legend()

plt.show()