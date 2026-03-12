import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import SphericalVoronoi, geometric_slerp
from mayavi import mlab

def print_vcels(vcels):
    vcels.sort_vertices_of_regions()

    fig = plt.figure(figsize=(20, 16))
    ax = fig.add_subplot(111, projection='3d')
    
    points = vcels.points

    x = points[:,0]
    y = points[:,1]
    z = points[:,2]
    
    ax.scatter(x, y, z, c = 'black', s = 20)
    params = np.linspace(0, 1, 5)


    for region in vcels.regions:
        #region -- вектор индексов вершин ячейки Вороного
        vertices = vcels.vertices[region] #массив вершин ячейки
        num = len(vertices) #количество вершин ячейки Вороного
        
        for i in range(num):    
            start = vertices[i]
            end = vertices[(i + 1) % num]

            line = geometric_slerp(start, end, params)
            ax.plot(line[:,0], line[:,1], line[:,2], c='black')
    

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def print_vcels_mayavi(vcels, vcels_areas, point_scale_factor = 0.03, arc_radius = 0.01, mode = 'fast', text_mode = 'false'):
    vcels.sort_vertices_of_regions()
    
    mlab.figure(size=(1200, 900), bgcolor=(1,1,1))
    
    phi, theta = np.mgrid[0:np.pi:50j, 0:2*np.pi:100j]
    r = 1.001
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    
    mlab.mesh(x, y, z, color=(1,1,1))
    
    points = vcels.points
    mlab.points3d(points[:,0], points[:,1], points[:,2], color = (0,0,0), scale_factor = point_scale_factor)
    
    if text_mode == 'true':
        for point, area in zip(points, vcels_areas):
            eps = 0.1
            point += point * eps
            mlab.text3d(point[0], point[1], point[2], f"{area:.2f}", scale=0.1, color=(0,0,1))
        
    all_arcs = np.empty((0, 3))
    params = np.linspace(0, 1, 10)
    for region in vcels.regions:
        vertices = vcels.vertices[region]
        num = len(vertices)
        for i in range(num):
            start = vertices[i]
            end = vertices[(i + 1) % num]
            arc = geometric_slerp(start, end, params)
            if mode == 'slow':
                mlab.plot3d(arc[:,0], arc[:,1], arc[:,2],
                    color=(0,0,0), reset_zoom=False, tube_sides=6, tube_radius=arc_radius)
            elif mode == 'fast':
                all_arcs = np.concatenate([all_arcs, arc])

    if mode == 'fast':
        mlab.plot3d(all_arcs[:,0], all_arcs[:,1], all_arcs[:,2],
                    color=(0,0,0), tube_sides=6, tube_radius=arc_radius)
    
    mlab.axes()
    mlab.show()
