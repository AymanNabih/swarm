from random import *
from numpy import array
from . import intelligence

class aba(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration):

        super().__init__()

        self.__function = function

        self.__scout = [[uniform(A, B) for k in range(dimension)] for i in range(n)]
        self.points(self.__scout)

        Pbest = self.__scout[array([function(x) for x in self.__scout]).argmin()]
        Gbest = Pbest

        if n <= 10:
            count = n - n//2, 1, 1, 1
        else:
            a = n//10
            b = 5
            c = (n -a*b - a)//2
            d = 2
            count = a, b, c, d

        for t in range(iteration):
            fitness = [function(x) for x in self.__scout]
            sort_fitness = [function(x) for x in self.__scout]
            sort_fitness.sort()
            best = [self.__scout[i] for i in [fitness.index(x) for x in sort_fitness[:count[0]]]]
            selected = [self.__scout[i] for i in [fitness.index(x) for x in sort_fitness[count[0]:count[2]]]]
            newbee = self.__new(best, count[1], A, B) + self.__new(selected, count[3], A, B)
            self.__scout = newbee + [[uniform(A, B) for k in range(dimension)] for i in range(n - len(newbee))]
            self.points(self.__scout)

            Pbest = self.__scout[array([function(x) for x in self.__scout]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
        self.set_Gbset(Gbest)


    def __new(self, l, c, A, B):
        bee = []
        for i in l:
            new = [self.__neighbor(i, A, B) for k in range(c)]
            bee += new
        bee += l
        return bee

    def __neighbor(self, who, A, B):
        neighbor = array(who) + uniform(-1, 1)*(array(who) - array(self.__scout[randint(0, len(self.__scout) - 1)]))
        for i in neighbor:
            if i < A:
                i = A
            elif i > B:
                i = B
        return list(neighbor)