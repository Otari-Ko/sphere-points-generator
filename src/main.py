import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import SphericalVoronoi, geometric_slerp
from equilibration_method import random_directions, equilib_method

num_directions = 100
time_step = 1 / num_directions
visc = 15.0

init_directions = random_directions(num_directions)
directions = equilib_method(init_directions, time_step, visc)
points = np.concatenate([directions,-directions])

v_cels = SphericalVoronoi(points)
v_cels.sort_vertices_of_regions()


# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# x = points[:,0]
# y = points[:,1]
# z = points[:,2]

# ax.scatter(x, y, z, c='blue', s=50, alpha=0.8)
# ax.scatter(-x, -y, -z, c='red', s=50, alpha=0.8)

# param = np.linspace(0, 1, 5);
# for region in vcels.regions:
#     #region -- вектор индексок вершин ячейки Вороного
#     vertices = vcels.vertices[region] #массив вершин ячейки
#     num = len(vertices) #количество вершин ячейки Вороного
    
#     for i in range(num):
#         # v = vertices[i]
#         #ax.scatter(v[0], v[1], v[2], c='black', s=50, alpha=0.8)
        
#         start = vertices[i]
#         end = vertices[(i + 1) % num]

#         line = geometric_slerp(start, end, param)
#         ax.plot(line[:,0], line[:,1], line[:,2], c='k')


# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.show()
