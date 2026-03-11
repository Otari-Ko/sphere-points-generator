import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from itertools import count  # Для итераций

# the repulsive force exerted by the point1 on the point2
def repulsive_force(point1, point2, k = 2):
    vec = point2 - point1
    norm = np.linalg.norm(vec)
    return vec / norm ** k

def total_force(point, directions):
    result = np.zeros((1,3))
    for i in range(directions.shape[0]):
        dir = directions[i]
        if not np.allclose(dir, point, atol=1e-12):
            result += repulsive_force(dir, point)
            result += repulsive_force(-dir, point)

    return result

def total_tangent_forces(directions):
    result = np.zeros(directions.shape)

    for i in range(directions.shape[0]):
        dir = directions[i]
        result[i] = total_force(dir, directions)
        result[i] = tangent_projection_on_sphere(dir, result[i])

    return result

def tangent_projection_on_sphere(sphere_point, vec):
    normal_proj = sphere_point * np.dot(sphere_point, vec)
    return vec - normal_proj

def equilib_method(init_directions, dt, visc, tol = 1e-12, animate=True):
    velocities0 = np.zeros(init_directions.shape)
    velocities1 = np.zeros(init_directions.shape)

    directions0 = init_directions.copy()
    directions1 = init_directions.copy()


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-1.2,1.2); ax.set_ylim(-1.2,1.2); ax.set_zlim(-1.2,1.2)
    
    scat_pos = ax.scatter([], [], [], c='blue', s=100)   # directions
    scat_neg = ax.scatter([], [], [], c='red', s=100)    # -directions
    error = tol + 1

    while (error >= tol):
        tangent_forces0 = total_tangent_forces(directions0)
        directions1 = directions0 + dt * velocities0 #trial step
        velocities1 = velocities0 + dt * (tangent_forces0 - visc * velocities0) #trial step

        for i in range(init_directions.shape[0]):
            norm = np.linalg.norm(directions1[i])
            directions1[i] = directions1[i] / norm
            velocities1[i] = tangent_projection_on_sphere(directions1[i], velocities1[i])

        row_norms = np.linalg.norm(velocities1, axis = 1)
        error = np.max(row_norms)

        velocities0 = velocities1.copy()
        directions0 = directions1.copy()

        pos_xyz = directions0.T      # directions
        neg_xyz = (-directions0).T   # -directions  
        scat_pos._offsets3d = (pos_xyz[0], pos_xyz[1], pos_xyz[2])
        scat_neg._offsets3d = (neg_xyz[0], neg_xyz[1], neg_xyz[2])
        
        plt.pause(0.1)  # Показать кадр
        print(error)
        

    plt.show()

    return directions1





