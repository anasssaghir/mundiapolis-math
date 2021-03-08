#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

size = "x-small"
fig = plt.figure()
px1 = plt.subplot2grid((3, 2), (0, 0))
px2 = plt.subplot2grid((3, 2), (0, 1))
px3 = plt.subplot2grid((3, 2), (1, 0))
px4 = plt.subplot2grid((3, 2), (1, 1))
px5 = plt.subplot2grid((3, 2), (2, 0), colspan=2)

px1.plot(y0, 'r')

px2.scatter(x1, y1, s=6, color='m')
px2.set_title("Men's Height vs Weight", size=size)
px2.set_xlabel("Height (in)", size=size)
px2.set_ylabel("Weight (lbs)", size=size)

px3.plot(x2, y2)
px3.set_title("Exponential Decay of C-14", size=size)
px3.set_ylabel("Fraction Remaining", size=size)
px3.set_xlabel("Time (years)", size=size)
px3.set_yscale('log')
px3.set_xlim((0, 28650))

px4.plot(x3, y31, '--', color='r', label='C-14')
px4.plot(x3, y32, color='g', label='Ra-226')
px4.set_title('Exponential Decay of Radioactive Elements', size=size)
px4.set_xlabel('Time (years)', size=size)
px4.set_xlim((0, 20000))
px4.set_ylabel('Fraction Remaining', size=size)
px4.set_ylim((0, 1))
px4.legend(prop={'size': size})

px5.hist(student_grades, edgecolor='black')
px5.set_title("Project A", size=size)
px5.set_xlabel("Grades", size=size)
px5.set_xlim(0, 100)
px5.set_xticks(np.arange(0, 110, 10))
px5.set_ylabel("Number of Students", size=size)
px5.set_ylim(0, 30)

fig.suptitle('All in One')
plt.show()