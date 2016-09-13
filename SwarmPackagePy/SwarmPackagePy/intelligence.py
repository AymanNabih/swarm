class sw:

    def __init__(self):

        self.__Positions = []
        self.__Gbest = []

    def set_Gbset(self, Gbest):
        self.__Gbest = Gbest

    def points(self, agents):
        self.__Positions.append([list(i) for i in agents])

    def get_agents(self):
        return self.__Positions

    def get_Gbest(self):
        return self.__Gbest