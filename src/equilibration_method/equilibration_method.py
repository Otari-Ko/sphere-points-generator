import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

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
    
    error = tol + 1

    while (error >= tol):
        tangent_forces_0 = total_tangent_forces(directions_0)

        directions_1 = directions_0 + dt * velocities_0 #trial step
        velocities_1 = velocities_0 + dt * (tangent_forces_0 - visc * velocities_0) #trial step

        #correction of the trial directions and velocities
        for i in range(init_directions.shape[0]):
            norm = np.linalg.norm(directions_1[i])
            directions_1[i] = directions_1[i] / norm
            velocities_1[i] = tangent_projection_on_sphere(directions_1[i], velocities_1[i])

        row_norms = np.linalg.norm(velocities_1 * dt, axis = 1)
        error = np.max(row_norms)
        print(error)
        velocities_0 = velocities_1.copy()
        directions_0 = directions_1.copy()

        print_fame(ax, directions_1)

    plt.show()
    return directions_1





