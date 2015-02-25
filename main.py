from random import randint
import math
import numpy

class Point(object):
    x = None
    y = None
    def __init__(self, x=None, y=None):
        self.x = float(x)
        self.y = float(y)

class Circle(object):
    x = None
    y = None
    radius = None
    def __init__ (self,x=0,y=0,radius=1):
        self.x = x
        self.y = y
        self.radius = radius

def is_point_in_circle(circle=None, point=None):
    origin_x = circle.x
    origin_y = circle.y
    r = circle.radius
    point_x = point.x
    point_y = point.y
    if ((point_x - origin_x)**2) + ((point_y - origin_y)**2) < (r**2):
        return True
    return False

my_circle = Circle(x=200,y=300,radius=55)

def generate_random_point_on_circle(circle):
    origin_x = circle.x
    origin_y = circle.y
    r = circle.radius
    rand_deg = randint(1, 360)
    x = origin_x + (r * math.cos(rand_deg)) + (randint(-100, 100)/100)
    y = origin_y + (r * math.sin(rand_deg)) + (randint(-100, 100)/100)
    random_point = Point(x,y)
    return random_point

def generate_file_with_100_points():  
    f = open('random_points.csv', 'w')
    for i in range(100):
        random_point = generate_random_point_on_circle(circle=my_circle)
        x = random_point.x
        y = random_point.y
        line = str(x) + ", " + str(y) + "\n"
        f.write(line)
    f.close()
    
#generate_file_with_100_points()

def get_list_of_points_from_file():
    f = open('random_points.csv', 'r')
    points = []
    for line in f.readlines():
        line = line.strip('\n')
        parts = line.split(',')
        x = parts[0]
        y = parts[1].strip(' ')
        points.append(Point(x,y))
    return points

points = get_list_of_points_from_file()

xo = 206
yo = 309
ro = 59

def solve_general():
    A = numpy.matrix([[0, 0, 0],])
    A = numpy.delete(A, (0), axis=0)
    B = numpy.matrix([[0, 0],])
    B = numpy.delete(B, (0), axis=0)
    W = numpy.matrix([[0],])
    W = numpy.delete(W, (0), axis=0)
    i = 1
    for point in points:
        x_prov = -2 * (point.x - xo)
        y_prov = -2 * (point.y - yo)
        r_prov = 2 * ro
        x_obs = 2 * (point.x - xo)
        y_obs = 2 * (point.y - yo)
        a_row = [x_prov, y_prov, r_prov]
        A = numpy.vstack([A, a_row])
        w_row = ((point.x - xo)**2) + ((point.y - yo)**2) - (ro**2)
        W = numpy.vstack([W, w_row])

        b_row = []
        if i == 1:
            b_row = [x_obs, y_obs]
            B = numpy.vstack([B, b_row])
        else:
            b_row = [0] * ((i * 2) -2)
            B = numpy.vstack([B, b_row])
            b_col = [[0]] * (i - 1)
            b_col.append([x_obs])
            B = numpy.hstack((B, b_col))
            b_col[-1] = [y_obs]
            B = numpy.hstack((B, b_col))
        i += 1
    X = - (A.T*(B*B.T).I*A).I * A.T * (B*B.T)*W
    return X


for i in range(2):
    X = solve_general()
    print(X)
    xo += X.item(0,0)
    yo += X.item(0,1)
    ro += X.item(0,2)
    
            
 
        
    


exit()


def solve_parametric():
    A = numpy.matrix([[0, 0, 0],])
    A = numpy.delete(A, (0), axis=0)
    L = numpy.matrix([[0],])
    L = numpy.delete(L, (0), axis=0)
    
    for point in points:
        sqrt = ((ro**2) - ((point.x - xo)**2))
        if sqrt > 0 and point.y > yo:
            x = (point.x - xo) / math.sqrt(sqrt)
            y = 1
            r = ro / math.sqrt(sqrt)
            row = [x, y, r]
            o = point.y
            c = math.sqrt(sqrt) + yo
            A = numpy.vstack([A, row])
            L = numpy.vstack([L, o-c])
    X = (A.T*A).I * (A.T * L)
    return A, X, L

A = None
X = None
L = None
for i in range(7):
    sol = solve_parametric()
    A = sol[0]
    X = sol[1]
    L = sol[2]  
    xo = xo + X.item(0,0)
    yo = yo + X.item(1,0)
    ro = ro + X.item(2,0)

V = A*X - L
apriori = float((V.T*V) / (len(L) - len(X)))
M = (A.T*A).I
# stdev unkonws
sqx = apriori * M
# stdev adjusted unknowns
qx = A*M*A.T
print(xo, yo, ro)




