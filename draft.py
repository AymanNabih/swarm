import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animat
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from numpy import linspace, meshgrid, array, ravel
import time
import multiprocessing
from multiprocessing import cpu_count
from multiprocessing.dummy import Pool
from random import *

class pso:

    def __init__(self, n, function, A, B, dimension, iteration, w=0.5, c1=1, c2=1):

        self.agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        velocity = array([[0 for k in range(dimension)] for i in range(n)])
        Pbest = self.agents[array([function(x) for x in self.agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):
            velocity = w * velocity + c1 * random() * (Pbest - self.agents) + c2 * random() * (Gbest - self.agents)
            self.agents += velocity
            Pbest = self.agents[array([function(x) for x in self.agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

def PS(args):
    return pso(*args)



f = tf.sphere_function

"""Without multiprocessing"""
t1 = time.time()
res1 = [pso(100, f, -10, 10, 20, 200) for i in range(1000)]
t2 = time.time()
print('Without multiprocessing: {}'.format(t2 - t1))

"""With multiprocessing"""
t3 = time.time()
p = multiprocessing.Pool(cpu_count())
res2 = p.map(PS, [[100, f, -10, 10, 20, 200]] * 1000)
p.close()
p.join()
t4 = time.time()
print('With multiprocessing: {}'.format(t4 - t3))