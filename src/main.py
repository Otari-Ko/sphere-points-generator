import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import SphericalVoronoi

from equilibration_method import random_directions, equilib_method
from voronoi_cels import print_vcels_mayavi

num_directions = 100
time_step = 1 / num_directions
visc = 15.0

init_directions = random_directions(num_directions)
#directions = init_directions

directions = equilib_method(init_directions, time_step, visc, tol = 0.0005)
points = np.concatenate([directions,-directions])

vcels = SphericalVoronoi(points)
vcels.sort_vertices_of_regions()

print_vcels_mayavi(vcels)

