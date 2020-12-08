import numpy as np

#step function
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

#sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#ReLU function
def relu(x):
    return np.maximum(0, x)

print("hello python")
