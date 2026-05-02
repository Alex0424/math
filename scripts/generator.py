import numpy as np
import matplotlib.pyplot as plt
import os

r = 1
t = np.linspace(0, 2*np.pi, 400)

x = r * np.cos(t)
y = r * np.sin(t)

plt.figure()

plt.plot(x, y)

theta = np.pi / 4 # diameter

x_d = [-r * np.cos(theta), r * np.cos(theta)]
y_d = [-r * np.sin(theta), r * np.sin(theta)]

plt.plot(x_d, y_d, color='green', linewidth=2)

plt.plot([0, r], [0, 0], color='red')

plt.scatter(0, 0, color='black', label='Origin')

plt.gca().set_aspect('equal')
plt.title("Circle with Radius and Diameter")
plt.grid()

plt.text(r + 0.2, 0.05, "r", color='red', ha='left')
plt.text(r + 0.2, -0.1, "d = 2r", color='green', ha='left')

output_dir = "../docs/images"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f"{output_dir}/circle.png", transparent=True)
plt.close()
