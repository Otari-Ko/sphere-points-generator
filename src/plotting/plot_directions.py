import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Читаем CSV (header=0 = первый ряд заголовок)
data = pd.read_csv('directions.csv')
x = data['x'].values
y = data['y'].values
z = data['z'].values

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Точки
ax.scatter(x, y, z, c='blue', s=120, alpha=0.8)
ax.scatter(-x, -y, -z, c='red', s=120, alpha=0.8)

# Сфера
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
sphere_x = np.outer(np.cos(u), np.sin(v))
sphere_y = np.outer(np.sin(u), np.sin(v))
sphere_z = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(sphere_x, sphere_y, sphere_z, alpha=0.15, color='gray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Направления на сфере (N={len(x)})')

plt.savefig('directions_3d.png', dpi=300, bbox_inches='tight')  # Автосохранение
plt.show()
