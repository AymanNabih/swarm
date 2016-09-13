from random import *
from numpy import array
from math import *
from . import intelligence


class gs(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, G0=1, csi=0.1):

        super().__init__()

        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)

        Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
        Gbest = Pbest

        velocity = array([[0 for k in range(dimension)] for i in range(n)])

        csi = array([[csi for k in range(dimension)] for i in range(n)])

        for t in range(iteration):

            fitness = array([function(x) for x in self.__agents])
            m = array([(function(x) - max(fitness))/(min(fitness) - max(fitness)) if function(x) != max(fitness) else 0
                       for x in self.__agents])
            M = array([i/sum(m) for i in m])
            G = G0*exp(-0.9*t)
            F = array([random()*sum([G*M[i]*M[j]*(self.__agents[j] - self.__agents[i])
                                     /(sqrt(sum((self.__agents[i] - self.__agents[j])**2)) + random())
                                     for j in range(n) if i != j]) for i in range(n)])

            velocity = csi*velocity + array([F[i]/M[i] if M[i] != 0 else [0 for k in range(dimension)] for i in range(n)])
            self.__agents += velocity
            self.points(self.__agents)

            Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self.set_Gbset(Gbest)