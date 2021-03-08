#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
space = np.arange(0, 110, 10)
plt.hist(x=student_grades, bins=space, facecolor='blue', edgecolor='black')
plt.xticks(space)
plt.xlim(0, 100, 10)
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.ylim((0, 30))
plt.show()