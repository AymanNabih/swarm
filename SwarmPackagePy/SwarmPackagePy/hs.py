from random import *
from numpy import array
from . import intelligence


class hs(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, par=0.5, hmcr=0.5, bw=0.5):

        super().__init__()

        nn = n

        self.__agents = [[uniform(A, B) for k in range(dimension)] for i in range(n)]
        self.points(self.__agents)
        Gbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
        worst = array([function(x) for x in self.__agents]).argmax()


        for t in range(iteration):

            hnew = [0 for k in range(dimension)]

            for i in range(len(hnew)):
                if random() < hmcr:
                    hnew[i] = self.__agents[randint(0, nn-1)][i]
                    if random() < par:
                        hnew[i] = hnew[i] + uniform(-1, 1)*bw
                else:
                    hnew[i] = uniform(A, B)

            if function(hnew) < function(self.__agents[worst]):
                self.__agents[worst] = hnew
                worst = array([function(x) for x in self.__agents]).argmax()

            Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

            self.points(self.__agents)
        self.set_Gbset(Gbest)

