from mackeyglass import MackeyGlass as mac
from sklearn.neural_network import MLPRegressor 
import matplotlib.pyplot as plt
import numpy as np

test = mac()
X,Y = test.generateData(301,1200)
Samples = np.asarray(X)
Labels = np.asarray(Y)
clf = MLPRegressor(alpha=0.1, hidden_layer_sizes = (50,), max_iter = 1000, 
                    activation = 'logistic', verbose = 'True', learning_rate = 'constant', learning_rate_init = 0.01)
a = clf.fit(Samples,Labels)

X1 = []
Y1 = []

for i in range(1201,1501):
    x = np.array([test.generateSerie(i-20),test.generateSerie(i-15),test.generateSerie(i-10),test.generateSerie(i-5),test.generateSerie(i)])
    x = x.reshape(1,-1)
    X1.append(i)
    aux = clf.predict(x)
    Y1.append(aux)
p1,p2 = test.plotGraph(0,1500,1)
plt.plot(p1,p2,"r",markersize = 2)
plt.plot(X1,Y1,"b",markersize = 2)
plt.show()