from random import *
from numpy import array
from math import *
from . import intelligence


class ba(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, r0=0.5, alpha=0.9, csi=0.9, A0=0.5, fmin=0, fmax=2):

        super().__init__()

        r1 = [r0 for i in range(n)]
        r = r1
        
        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)

        velocity = array([[0. for k in range(dimension)] for i in range(n)])
        A = [A0 for i in range(n)]

        Pbest = self.__agents[array([function(i) for i in self.__agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):
            sol = self.__agents
            f = [fmin + (fmin - fmin)*random() for i in range(n)]
            F = array([[i, i] for i in f])
            velocity += (self.__agents - Gbest)*F
            sol += velocity

            for i in range(n):
                if random() > r[i]:
                    sol[i] = Gbest + uniform(-1,1)*sum(A)/len(A)

            for i in range(n):
                if function(sol[i]) < function(self.__agents[i]) and random() < A[i]:
                    self.__agents[i] = sol[i]
                    A[i] *= alpha
                    r[i] *= (1 - exp(-csi*t))

            self.points(self.__agents)
            Pbest = self.__agents[array([function(i) for i in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
        self.set_Gbset(Gbest)