from random import *
from numpy import array
from . import intelligence

class gwo(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration):

        super().__init__()

        self.__function = function

        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)

        for t in range(iteration):
            a = array(2-2*t/iteration)
            alpha, beta, delta = self.__get_abd()
            r1, r2 = array(round(random(), 5)), round(random(), 5)
            A1 = 2*r1*a-a
            C1 = 2*r2

            r1, r2 = round(random(), 5), round(random(), 5)
            A2 = 2*r1*a-a
            C2 = 2*r2

            r1, r2 = round(random(), 5), round(random(), 5)
            A3 = 2*r1*a-a
            C3 = 2*r2

            Dalpha = abs(C1*alpha-self.__agents)
            Dbeta = abs(C2*beta-self.__agents)
            Ddelta = abs(C3*delta-self.__agents)

            X1, X2, X3 = array([alpha - A1*x for x in Dalpha]), array([beta - A2*x for x in Dbeta]), \
                         array([delta - A3*x for x in Ddelta])

            self.__agents = (X1+X2+X3)/3
            self.points(self.__agents)

        alpha, beta, delta = self.__get_abd()
        self.set_Gbset(alpha)
        self.__leaders = alpha, beta, delta

    def __get_abd(self):
        agents = list(self.__agents)
        alpha = agents[array([self.__function(x) for x in agents]).argmin()]
        beta = agents[array([self.__function(x) for x in agents]).argmin()]
        delta = agents[(array([self.__function(x) for x in agents]).argmin())]
        return alpha, beta, delta

    def get_ledears(self):
        return self.__leaders