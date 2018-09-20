import matplotlib.pyplot as plt

class MackeyGlass(object):

    def __init__(self, beta=0.2, y=0.1, n=10.0, tau=25, x = 1.5):
        self.beta = beta
        self.y = y
        self.n = n
        self.tau = tau
        self.x = [x]
        for i in range(len(self.x), self.tau):
            next = self.x[i-1] - y * self.x[i-1]
            self.x.append(next)
         
    def generateSerie(self, t):
        if t < 0:
            return 0
        else:
            try:
                aux = self.x[t]
            except IndexError:
                aux = 0
            if aux:
                return aux
            else:
                for i in range(len(self.x),t+1):
                    next = self.x[i-1] + ((self.beta*self.x[i-self.tau-1])/(1+self.x[i-self.tau-1]**10))-self.y * self.x[i-1]
                    self.x.append(next)
                return self.x[t]
    def plotGraph(self,min, max, toggle = 0):
        X = []
        Y = []
        for i in range(min,max+1):
            X.append(i)
            Y.append(self.generateSerie(i))
        if toggle:
            return X,Y
        else:
            plt.plot(X,Y,"b",markersize = 2)
            plt.show()
    def generateData(self, min, max):
        Samples = []
        Labels = []
        for i in range(min, max+1):
            Labels.append(self.generateSerie(i+5))
            Samples.append([self.generateSerie(i-20),self.generateSerie(i-15), self.generateSerie(i-10), self.generateSerie(i-5), self.generateSerie(i)])
        return Samples,Labels
    
