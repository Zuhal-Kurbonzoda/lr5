import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_polyhedron(vertices, faces, ax, color, edge_color, offset=[0, 0, 0]):
    vertices = vertices + offset
    poly3d = [[vertices[vert_id] for vert_id in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, edgecolors=edge_color, alpha=.25))

def hexahedron():
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]]
    return vertices, faces

def octahedron():
    vertices = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    faces = [[0, 2, 4], [0, 2, 5], [0, 3, 4], [0, 3, 5], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5]]
    return vertices, faces

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices, faces = hexahedron()
plot_polyhedron(vertices, faces, ax, color='blue', edge_color='black', offset=[-2, 0, 0])

vertices, faces = octahedron()
plot_polyhedron(vertices, faces, ax, color='red', edge_color='black', offset=[2, 0, 0])

ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 4])

plt.show()