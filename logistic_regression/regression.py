import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from .utils import update_weights,sigmoid, cost_function

class LogisticRegression():
    def __init__(self, X, Y, train_size, iteration, learning_rate = 0.1, 
                                     threshold = 0.005, shuffle = False):
        self.train_X, self.test_X, self.train_Y, self.test_Y = train_test_split(X, Y,
                                          train_size = train_size, shuffle = shuffle)
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.iteration = iteration
        self.weights = np.zeros(self.train_X.shape[1])
        self.trained = False
        self.metrics = {
            "loss" : self.loss,
            "acurracy" : self.acurracy
        }

        

    def train(self):
        self.result_metrics = {metric:{"train" : [], "test" : []} for metric in self.metrics}

        for i in range(self.iteration):
            self.weights = update_weights(self.train_X, self.train_Y, self.weights,
                                                               self.learning_rate)
            for metric in self.result_metrics:
                result = lambda x,y,metric : self.metrics[metric](x, y, self.predict(x))

                self.result_metrics[metric]["train"].append(result(self.train_X, 
                                                            self.train_Y, metric))
                self.result_metrics[metric]["test"].append(result(self.test_X, 
                                                             self.test_Y, metric))

        self.trained = True

        return self.result_metrics

    def predict(self, x = None):
        if x is None:
            x = self.train_X
        
        return (sigmoid(x.dot(self.weights)) >= 0.5).astype(int)
    
    
    def acurracy(self, x = None, y = None, y_pred = None):
        if x is None and y is None:
            x = self.test_X
            y = self.test_Y

        return (y == y_pred).sum()/y.shape[0]

    def loss(self, x = None, y = None, y_pred = None):
        if x is None and y is None:
            x = self.test_X
            y = self.test_Y

        return cost_function(x, y, self.weights)
    
    def plot_train_test_results(self, metric = "loss"):
        if self.trained:
            if metric in  self.metrics:
                plt.plot(self.result_metrics[metric]["train"], label = "train")
                plt.plot(self.result_metrics[metric]["test"], label = "test")
                plt.legend()
                plt.show()
            
            else:
                raise Exception("Metric not found")

        else:
            raise Exception("Model not trained")
