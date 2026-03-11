import numpy as np
import matplotlib.pyplot as plt

# The repulsive force exerted by the point1 on the point2
def repulsive_force(point1, point2, k = 2):
    vec = point2 - point1
    norm = np.linalg.norm(vec)
    return vec / norm ** k

# The total force exerted by the all directions on the point
# Note: one direction (dir) generates a primary (dir) and secondary (-dir) point on the unit sphere
def total_force(point, directions):
    result = np.zeros((1,3))
    for i in range(directions.shape[0]):
        dir = directions[i] 

        if not np.allclose(dir, point, atol=1e-12):
            result += repulsive_force(dir, point) # the force extanded by the primary point of direction on the "point"
            result += repulsive_force(-dir, point) # the force extanded by the secondary point of direction on the "point"

    return result

def total_tangent_forces(directions):
    result = np.zeros(directions.shape)

    for i in range(directions.shape[0]):
        dir = directions[i]
        result[i] = total_force(dir, directions)
        result[i] = tangent_projection_on_sphere(dir, result[i])

    return result

# computes the projection of a vector onto the tangent space of the unit sphere at a fixed point.
def tangent_projection_on_sphere(sphere_point, vector):
    normal_proj = sphere_point * np.dot(sphere_point, vector)
    return vector - normal_proj

def print_fame(ax, directions):
    ax.clear()
    ax.scatter(directions[:,0], directions[:,1], directions[:,2], c = 'blue', s = 50)
    ax.scatter(-directions[:,0], -directions[:,1], -directions[:,2], c = 'red', s = 50)
    plt.pause(0.1)
