from random import *
from numpy import array
from . import intelligence


class pso(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, w=0.5, c1=1, c2=1):

        super().__init__()

        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        velocity = array([[0 for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)
        Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):
            velocity = w*velocity + c1*random()*(Pbest - self.__agents) + c2*random()*(Gbest - self.__agents)
            self.__agents += velocity
            self.points(self.__agents)

            Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
        self.set_Gbset(Gbest)