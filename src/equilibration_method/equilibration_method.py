import numpy as np
import matplotlib.pyplot as plt

from .utils import *

def equilib_method(init_directions, dt, visc, tol = 0.0005, animate=True):
    velocities_0 = np.zeros(init_directions.shape)
    velocities_1 = np.zeros(init_directions.shape)

    directions_0 = init_directions.copy()
    directions_1 = init_directions.copy()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_zlim(-1.2, 1.2)
    
    iter = 1
    max_displ = tol + 1

    while (max_displ >= tol):
        tangent_forces_0 = total_tangent_forces(directions_0)

        directions_1 = directions_0 + dt * velocities_0 #trial step
        velocities_1 = velocities_0 + dt * (tangent_forces_0 - visc * velocities_0) #trial step

        #correction of the trial directions and velocities
        for i in range(init_directions.shape[0]):
            norm = np.linalg.norm(directions_1[i])
            directions_1[i] = directions_1[i] / norm
            velocities_1[i] = tangent_projection_on_sphere(directions_1[i], velocities_1[i])

        displs = np.linalg.norm(velocities_1 * dt, axis = 1)
        max_displ = np.max(displs)
        
        print(f'iteration: {iter}')
        print(f'maximum displacement: {max_displ} \n')
        print_fame(ax, directions_1)

        velocities_0 = velocities_1.copy()
        directions_0 = directions_1.copy()
        iter += 1

    return directions_1





