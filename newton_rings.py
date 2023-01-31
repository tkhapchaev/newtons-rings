import numpy as np
import matplotlib.pyplot as plt

m = 1
r1 = 1
labda = (550 * (10**(-9)))  # зелёный

r2 = np.arange(-10, 10, 0.001)
rm = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))

plt.plot(r2, rm)
plt.xlabel("R₂")
plt.ylabel("rₘₐₓ (R₂)")
plt.title("Зависимость радиуса m-го светлого кольца" + "\n" + "от радиуса кривизны второй линзы")
plt.grid(True)
plt.savefig("max_dependency_graph.png")

plt.cla()
plt.clf()

rm = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))

plt.plot(r2, rm)
plt.xlabel("R₂")
plt.ylabel("rₘᵢₙ (R₂)")
plt.title("Зависимость радиуса m-го тёмного кольца" + "\n" + "от радиуса кривизны второй линзы")
plt.grid(True)
plt.savefig("min_dependency_graph.png")

minimums = []
maximums = []

plt.cla()
plt.clf()

r2 = 5
for m in range(1, 17):
    rmin = np.sqrt(m * labda * ((r1 * r2) / (r1 + r2)))
    rmax = np.sqrt(((2 * m + 1) / 2) * labda * ((r1 * r2) / (r1 + r2)))
    minimums.append(rmin)
    maximums.append(rmax)

for i in minimums:
    ring = plt.Circle((0, 0), i, color='black', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

plt.axis('scaled')
plt.savefig("interference_minima.png")
plt.cla()
plt.clf()

for j in maximums:
    ring = plt.Circle((0, 0), j, color='blue', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

plt.axis('scaled')
plt.savefig("interference_maxima.png")
plt.cla()
plt.clf()

for i in minimums:
    ring = plt.Circle((0, 0), i, color='black', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

for j in maximums:
    ring = plt.Circle((0, 0), j, color='blue', fill=False)
    ax = plt.gca()
    ax.add_patch(ring)

plt.axis('scaled')
plt.savefig("interference_pattern.png")
