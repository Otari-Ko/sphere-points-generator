import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import SphericalVoronoi, geometric_slerp
from initial_directions import random_directions
from equilibration_method import equilib_method
num = 100

directions = random_directions(num)
equilib_method(directions, 0.1/num, 1, tol = 1e-12, animate=True)
points = np.concatenate([directions,-directions])

vcels = SphericalVoronoi(points)
vcels.sort_vertices_of_regions()


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

x = points[:,0]
y = points[:,1]
z = points[:,2]

ax.scatter(x, y, z, c='blue', s=50, alpha=0.8)
ax.scatter(-x, -y, -z, c='red', s=50, alpha=0.8)

param = np.linspace(0, 1, 5);
for region in vcels.regions:
    #region -- вектор индексок вершин ячейки Вороного
    vertices = vcels.vertices[region] #массив вершин ячейки
    num = len(vertices) #количество вершин ячейки Вороного
    
    for i in range(num):
        #v = vertices[i]
        #ax.scatter(v[0], v[1], v[2], c='black', s=50, alpha=0.8)
        
        start = vertices[i]
        end = vertices[(i + 1) % num]

        line = geometric_slerp(start, end, param)
        ax.plot(line[:,0], line[:,1], line[:,2], c='k')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
