import numpy as np
import matplotlib.pyplot as plt

r1 = 1
r2 = 5
labda = (550 * (10**(-9)))  # зелёный

minimums = []
maximums = []

for m in range(1, 17):
    rmin = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))
    rmax = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))
    minimums.append(rmin)
    maximums.append(rmax)

for i in minimums:
    ring = plt.Circle((0, 0), i, color='black', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

minimums.clear()
maximums.clear()

labda = (560 * (10**(-9)))
for m in range(1, 17):
    rmin = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))
    rmax = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))
    minimums.append(rmin)
    maximums.append(rmax)

for i in minimums:
    ring = plt.Circle((0, 0), i, color='red', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

plt.axis('scaled')
plt.savefig("interference_pattern_min.png")
plt.clf()
plt.cla()
labda = (550 * (10**(-9)))

for m in range(1, 17):
    rmin = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))
    rmax = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))
    minimums.append(rmin)
    maximums.append(rmax)

for i in maximums:
    ring = plt.Circle((0, 0), i, color='black', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

minimums.clear()
maximums.clear()

labda = (560 * (10**(-9)))
for m in range(1, 17):
    rmin = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))
    rmax = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))
    minimums.append(rmin)
    maximums.append(rmax)

for i in maximums:
    ring = plt.Circle((0, 0), i, color='blue', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

plt.axis('scaled')
plt.savefig("interference_pattern_max.png")
