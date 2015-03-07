from random import randint
import math
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Solution(object):
    a = None
    x = None
    w = None
    b = None
    k = None
    reference_variance = None
    var_covar_x = None
    v = None

    def __init__(self, a, x, w, b, k, v, reference_variance, var_covar_x):
        self.a = a
        self.x = x
        self.w = w
        self.b = b
        self.k = k
        self.v = v
        self.reference_variance = reference_variance
        self.var_covar_x = var_covar_x
    
class Point(object):
    x = None
    y = None
    z = None
    def __init__(self, x=None, y=None, z=None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "point<x:{0}><y:{1}><z:{2}>".format(self.x, self.y, self.z)
        

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

def plot_hemisphere(x, y, z, r):
    pass

def generate_random_point_on_hemishpere():
    origin_x = 0
    origin_y = 0
    origin_z = 0
    r = 100
    theta = math.radians(randint(0, 360))
    phi = math.radians(randint(0, 90))
    x = origin_x + r * math.cos(theta) * math.sin(phi) + randint(-100,100)/100
    y = origin_y + r * math.sin(theta) * math.sin(phi) + randint(-100,100)/100
    z = origin_z + r * math.cos(phi) + randint(-100,100)/100
    random_point = Point(x,y,z)
    return random_point

def generate_file_from_list_of_points(list_of_points=None, path='random_points.csv'):  
    f = open(path, 'w')
    for point in list_of_points:
        x = point.x
        y = point.y
        z = point.z
        line = str(x) + ", " + str(y) + ", " + str(z) + "\n"
        f.write(line)
    f.close()

def generate_list_of_points(n=100):
    list_of_points = []
    for i in range(n):
        list_of_points.append(generate_random_point_on_hemishpere())
    return list_of_points

def get_list_of_points_from_file(path='random_points.csv'):
    f = open(path, 'r')
    list_of_points = []
    for line in f.readlines():
        line = line.strip('\n')
        parts = line.split(',')
        x = parts[0]
        y = parts[1].strip(' ')
        z = parts[2].strip(' ')
        list_of_points.append(Point(x,y,z))
    return list_of_points
    
def solve_general(list_of_points, xo, yo, zo, ro):
    a_width = 4
    b_width = 3
    number_of_observations = len(list_of_points)
    number_of_unknowns = 4
    A = numpy.matrix([[0] * a_width,])
    A = numpy.delete(A, (0), axis=0)
    B = numpy.matrix([[0] * b_width,])
    B = numpy.delete(B, (0), axis=0)
    W = numpy.matrix([[0],])
    W = numpy.delete(W, (0), axis=0)
    i = 1
    for point in list_of_points:
        x_prov = -2 * (point.x - xo)
        y_prov = -2 * (point.y - yo)
        z_prov = -2 * (point.z - zo)
        r_prov = -2 * ro
        
        x_obs = 2 * (point.x - xo)
        y_obs = 2 * (point.y - yo)
        z_obs = 2 * (point.z - zo)
        
        a_row = [x_prov, y_prov, z_prov, r_prov]
        A = numpy.vstack([A, a_row])
        
        w_row = ((point.x - xo)**2) + ((point.y - yo)**2) + ((point.z - zo)**2) - (ro**2)
        W = numpy.vstack([W, w_row])

        b_row = []
        if i == 1:
            b_row = [x_obs, y_obs, z_obs]
            B = numpy.vstack([B, b_row])
        else:
            b_row = [0] * ((i * b_width) - b_width)
            B = numpy.vstack([B, b_row])
            b_col = [[0]] * (i)
            
            b_col[-1] = [x_obs]
            B = numpy.hstack((B, b_col))
            b_col[-1] = [y_obs]
            B = numpy.hstack((B, b_col))
            b_col[-1] = [z_obs]
            B = numpy.hstack((B, b_col))
        i += 1
        
    M = B*B.T
    X = - (A.T*(M).I*A).I * A.T * (M).I*W
    k = -M.I * ( A * X + W)
    v = B.T * k
    # Reference variance.
    reference_variance = float((v.T * v) / number_of_observations - number_of_unknowns)
    # Variance-Covariance Matrix of the Unknowns x
    var_covar_x = reference_variance * (A.T *(M.I)*A).I
    solution = Solution(
        w=W,
        x=X,
        b=B,
        a=A,
        k=k,
        v=v,
        reference_variance=reference_variance,
        var_covar_x=var_covar_x,
        )
    return solution

list_of_points = get_list_of_points_from_file('data_assignment1.csv')
#plot_list_of_points(list_of_points)
#generate_file_from_list_of_points(generate_list_of_points(n=500))

xo = 0
yo = 0
zo = 0
ro = 100

for i in range(1):
    solution = solve_general(list_of_points, xo, yo, zo, ro)
    xo += solution.x.item(0,0)
    yo += solution.x.item(1,0)
    zo += solution.x.item(2,0)
    ro += solution.x.item(3,0)

print (xo, yo, zo, ro)


