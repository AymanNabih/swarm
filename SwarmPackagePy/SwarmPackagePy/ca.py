from random import *
from numpy import array
from . import intelligence

class ca(intelligence.sw):

    def __init__(self, n, function, A, B, dimension, iteration, mr, smp=2, spc=False, cdc=1, srd=0.5, w=0.6, c=2.05, csi=0.6):

        super().__init__()

        self.__agents = array([[uniform(A, B) for k in range(dimension)] for i in range(n)])
        velocity = array([[0 for k in range(dimension)] for i in range(n)])
        self.points(self.__agents)
        Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
        Gbest = Pbest

        flag = self.__set_flag(n, mr)
        if spc:
            sm = smp -1
        else:
            sm = smp

        for t in range(iteration):

            for i in range(n):
                if flag[i] == 0:
                    if spc:
                        cop = self.__change_copy([self.__agents[i]], cdc, srd)[0]
                        tmp = [self.__agents[i] for j in range(sm)]
                        tmp.append(cop)
                        copycat = array(tmp)
                    else:
                        copycat = array([self.__agents[i] for j in range(sm)])
                    copycat = self.__change_copy(copycat, cdc, srd)
                    if copycat.all() == array([copycat[0] for j in range(sm)]).all():
                        P = array([1 for j in range(len(copycat))])
                    else:
                        fb = min([function(j) for j in copycat])
                        fmax = max([function(j) for j in copycat])
                        fmin = min([function(j) for j in copycat])
                        P = array([abs(function(j) - fb)/(fmax - fmin) for j in copycat])
                    self.__agents[i] = copycat[P.argmax()]
                else:
                    ww = w + (iteration - t)/(2*iteration)
                    cc = c - (iteration - t)/(2*iteration)
                    r = random()
                    velocity[i] = ww*array(velocity[i]) + r*cc*(array(Pbest) - array(self.__agents[i]))
                    vinf, cinf = self.__get_inf(i, velocity, self.__agents, csi)
                    self.__agents[i] = list(1/2*(vinf + cinf))


            Pbest = self.__agents[array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest
            flag = self.__set_flag(n, mr)
            self.points(self.__agents)
        self.set_Gbset(Gbest)

    def __set_flag(self, n, mr):
        flag = [0 for i in range(n)]
        m = mr
        while m > 0:
            tmp = randint(0, n-1)
            if flag[tmp] == 0:
                flag[tmp] = 1
                m = m - 1
        return flag

    def __change_copy(self, copycat, cdc, crd):
        for i in range(len(copycat)):
            flag = [0 for k in range(len(copycat[i]))]
            c = cdc
            while c > 0:
                tmp = randint(0, len(copycat[i])-1)
                if flag[tmp] == 0:
                    c = c - 1
                    copycat[i][tmp] = copycat[i][tmp] + choice([-1, 1])*crd
        return copycat

    def __get_inf(self, i, velocity, cat, csi):
        if i == 0:
            vinf = array(velocity[i]) + (csi*array(velocity[1]) + (1-csi)*array(velocity[2]))/2 + \
                   (csi*array(velocity[-1]) + (1-csi)*array(velocity[-2]))/2
            cinf = array(cat[i]) + (csi*array(cat[1]) + (1-csi)*array(cat[2]))/2 + \
                   (csi*array(cat[-1]) + (1-csi)*array(cat[-2]))/2
        elif i == 1:
            vinf = array(velocity[i]) + (csi*array(velocity[2]) + (1-csi)*array(velocity[3]))/2 + \
                   (csi*array(velocity[0]) + (1-csi)*array(velocity[-1]))/2
            cinf = array(cat[i]) + (csi*array(cat[2]) + (1-csi)*array(cat[3]))/2 + \
                   (csi*array(cat[0]) + (1-csi)*array(cat[-1]))/2
        elif i == len(velocity)-1:
            vinf = array(velocity[i]) + (csi*array(velocity[0]) + (1-csi)*array(velocity[1]))/2 + \
                   (csi*array(velocity[i-1]) + (1-csi)*array(velocity[i-2]))/2
            cinf = array(cat[i]) + (csi*array(cat[0]) + (1-csi)*array(cat[1]))/2 + \
                   (csi*array(cat[i-1]) + (1-csi)*array(cat[i-2]))/2
        elif i == len(velocity)-2:
            vinf = array(velocity[i]) + (csi*array(velocity[i+1]) + (1-csi)*array(velocity[0]))/2 + \
                   (csi*array(velocity[i-1]) + (1-csi)*array(velocity[i-2]))/2
            cinf = array(cat[i]) + (csi*array(cat[i+1]) + (1-csi)*array(cat[0]))/2 + \
                   (csi*array(cat[i-1]) + (1-csi)*array(cat[i-2]))/2
        else:
            vinf = array(velocity[i]) + (csi*array(velocity[i+1]) + (1-csi)*array(velocity[i+2]))/2 + \
                   (csi*array(velocity[i-1]) + (1-csi)*array(velocity[i-2]))/2
            cinf = array(cat[i]) + (csi*array(cat[i+1]) + (1-csi)*array(cat[i+2]))/2 + \
                   (csi*array(cat[i-1]) + (1-csi)*array(cat[i-2]))/2
        return vinf, cinf
