import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_list_of_points(list_of_points):
    x, y, z = [], [], []
    for point in list_of_points:
        x.append(point.x)
        y.append(point.y)
        z.append(point.z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
