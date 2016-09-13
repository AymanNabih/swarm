from random import *
from numpy import array
from math import *
from . import intelligence

class fa(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, csi=1, alpha=0.48):

        super().__init__()

        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)

        Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):
            fitness = [function(x) for x in self.__agents]
            for i in range(len(fitness)):
                fitness = [function(x) for x in self.__agents]
                for j in range(0, i):
                    if fitness[i] > fitness[j]:
                        self.__move(i, j, t, csi, alpha)
                    else:
                        self.__agents[i] += array([normalvariate(0, 0.1), normalvariate(0, 0.1)])

            self.points(self.__agents)

            Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
        self.set_Gbset(Gbest)

    def __move(self, i, j, t, csi, alpha):
        r = sqrt(sum((self.__agents[i] - self.__agents[j])**2))
        beta = csi/(1 + r**2)
        self.__agents[i] = self.__agents[j] + beta*(self.__agents[i] - self.__agents[j]) + \
                           alpha*exp(-t)*array([normalvariate(0, 1), normalvariate(0, 1)])