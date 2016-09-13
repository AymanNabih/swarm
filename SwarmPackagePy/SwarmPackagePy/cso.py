from random import *
from numpy import array
from math import *
from . import intelligence

class cso(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, pa=0.5, nest=100):

        super().__init__()

        self.__Nests = []

        beta = 3/2
        sigma = (gamma(1 + beta)*sin(pi*beta/2)/(gamma((1+beta)/2)*beta*2**((beta-1)/2)))**(1/beta)
        u = array([normalvariate(0, 1), normalvariate(0, 1)])*sigma
        v = array([normalvariate(0, 1), normalvariate(0, 1)])
        step = u/abs(v)**(1/beta)

        self.__cuckoos = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        self.__nests = array([[uniform(A, B) for k in range(dimension)] for i in range(nest)])
        Pbest = self.__nests[array([function(x) for x in self.__nests]).argmin()]
        Gbest = Pbest
        self.points(self.__cuckoos)

        for t in range(iteration):

            for i in self.__cuckoos:
                tmp = randint(0, nest-1)
                if function(i) < function(self.__nests[tmp]):
                    self.__nests[tmp] = i

            for i in self.__nests:
                if random() < pa:
                    i = [round(uniform(A, B), 5), round(uniform(A, B), 5)]

            Pbest = self.__nests[array([function(x) for x in self.__nests]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
            self.__Levyfly(step, Pbest, n)
            self.points(self.__cuckoos)
            self.__nest()
        self.set_Gbset(Gbest)

    def __nest(self):
        self.__Nests.append([list(i) for i in self.__nests])

    def __Levyfly(self, step, Pbest, n):
        for i in range(n):
            stepsize = 0.2*step*(self.__cuckoos[i] - Pbest)
            self.__cuckoos[i] += stepsize*array([normalvariate(0, 1), normalvariate(0, 1)])

    def get_nests(self):
        return  self.__Nests