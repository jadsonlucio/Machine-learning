import numpy as np

def sigmoid(x):
    return np.maximum(np.minimum(1/(1+np.exp(x)), 0.9999), 0.0001)

def cost_function(x, y, weights):
    t = x.dot(weights)

    return np.sum(y * np.log(sigmoid(t)) + (1 - y) * np.log(1 - sigmoid(t)))/x.shape[0]

def gradient_cost_function(x, y, weights):
    t = x.dot(weights)

    return x.T.dot(y - sigmoid(t))/x.shape[0]

def update_weights(x, y, weights, learning_rate):
    return weights + learning_rate * gradient_cost_function(x, y, weights)
